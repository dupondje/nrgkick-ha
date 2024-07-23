"""Config flow for NRGKick integration."""

from __future__ import annotations

import logging
from typing import Any

import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("url"): cv.string,
        vol.Optional("login"): cv.string,
        vol.Optional("password"): cv.string,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """

    login = data.get("login")
    password = data.get("password")
    url = data.get("url")
    info = None

    auth = None
    if login is not None:
        auth = aiohttp.BasicAuth(login, password)

    try:
        async with (
            aiohttp.ClientSession(
                auth=auth, timeout=aiohttp.ClientTimeout(5)
            ) as session,
            session.get(url + "/info") as resp,
        ):
            info = await resp.json()
    except aiohttp.ClientResponseError:
        raise
    except Exception as err:  # pylint: disable=broad-except
        raise CannotConnect from err

    # Return info that you want to store in the config entry.
    if info is None:
        raise CannotConnect

    return {
        "serial": info["general"]["serial_number"],
        "name": info["general"]["device_name"],
        "model": info["general"]["model_type"],
        "login": login,
        "password": password,
    }


class NRGKickConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for NRGKick."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                user_input["login"] = info["login"]
                user_input["password"] = info["password"]
                user_input["serial"] = info["serial"]
                user_input["name"] = info["name"]
                user_input["model"] = info["model"]
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=info["name"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""
