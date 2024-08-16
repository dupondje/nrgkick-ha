"""NRGKick coordinator class."""

from collections.abc import Callable
from datetime import timedelta
import logging
from typing import Any

import aiohttp

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class NRGKickCoordinator(DataUpdateCoordinator):
    """NRGKick coordinator."""

    def __init__(
        self, hass: HomeAssistant, url: str, login: str, password: str
    ) -> None:
        """Initialize NRGKick."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.unsub: Callable | None = None
        self._url = url
        self._auth = None
        if login is not None:
            self._auth = aiohttp.BasicAuth(login, password)

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        data: Any = {}
        try:
            async with aiohttp.ClientSession(
                base_url=self._url, auth=self._auth, timeout=aiohttp.ClientTimeout(5)
            ) as session:
                async with session.get("/info") as resp:
                    info = await resp.json()
                async with session.get("/control") as resp:
                    control = await resp.json()
                async with session.get("/values") as resp:
                    values = await resp.json()

            data["info"] = info
            data["control"] = control
            data["values"] = values
        except Exception as ex:
            # Most likely a connection issue. Retry later
            raise UpdateFailed from ex

        return data

    async def set(self, endpoint: str, parameter: str, value: str):
        """Set a value via the API."""
        params = {parameter: value}
        async with (
            aiohttp.ClientSession(
                base_url=self._url, auth=self._auth, timeout=aiohttp.ClientTimeout(5)
            ) as session,
            session.get("/" + endpoint, params=params) as resp,
        ):
            await resp.json()
