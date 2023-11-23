"""Config flow for NRGKick integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN
from .websocket import NRGKickWebsocket

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("ip"): cv.string,
        vol.Optional("pin"): cv.string,
        vol.Optional("uuid"): cv.string,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """

    uuid = data.get("uuid")
    nrgkicksocket = NRGKickWebsocket(data["ip"], uuid)
    details = None

    try:
        nrgkicksocket.connect()
        # If no UUID was given, we need to create a new UUID for HA
        if not uuid:
            pin = data.get("pin")
            if not pin:
                raise MissingUUIDorPin()
            uuid = await nrgkicksocket.create_uuid(data["pin"])
            if not uuid:
                raise CannotCreateUUID()
        details = await nrgkicksocket.get_device_control_info()
    except (MissingUUIDorPin, CannotCreateUUID):
        nrgkicksocket.stop()
        raise
    except Exception:  # pylint: disable=broad-except
        nrgkicksocket.stop()
        raise CannotConnect

    # Return info that you want to store in the config entry.
    if details is None:
        raise CannotConnect
    return {
        "serial": details.serialNumber,
        "name": details.deviceName.value,
        "uuid": uuid,
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
                user_input["uuid"] = info["uuid"]
                user_input["serial"] = info["serial"]
                user_input["name"] = info["name"]
            except MissingUUIDorPin:
                errors["base"] = "missing_uuid_or_pin"
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except CannotCreateUUID:
                errors["base"] = "cannot_create_uuid"
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


class MissingUUIDorPin(HomeAssistantError):
    """Error to indicate UUID and PIN are not set."""


class CannotCreateUUID(HomeAssistantError):
    """Error to indicate we failed to create a uuid."""
