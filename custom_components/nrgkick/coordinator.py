"""NRGKick coordinator class."""

import asyncio
from collections.abc import Callable
from datetime import timedelta
import logging
from typing import Any

from websockets import InvalidHandshake, InvalidURI

from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN
from .websocket import NRGKickWebsocket

_LOGGER = logging.getLogger(__name__)


class NRGKickCoordinator(DataUpdateCoordinator):
    """NRGKick coordinator."""

    def __init__(self, hass: HomeAssistant, websocket: NRGKickWebsocket) -> None:
        """Initialize NRGKick."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.unsub: Callable | None = None
        self.websocket = websocket

    async def _setup_websocket(self) -> None:
        """Start WebSocket Connection."""
        try:
            async with asyncio.timeout(15):
                await self.websocket.connect()
        except InvalidURI as exception:
            self.logger.error("Invalid URL for %s: %s", self.name, exception)
            if self.unsub:
                self.unsub()
                self.unsub = None
            self.last_update_success = False
            self.async_update_listeners()
        except (TimeoutError, asyncio.TimeoutError) as exception:
            self.logger.warning(
                "Timed out waiting for %s. Will retry: %s",
                self.name,
                exception,
            )
            self.last_update_success = False
            self.async_update_listeners()
        except (OSError, InvalidHandshake) as exception:
            self.logger.error("Connection failed for %s: %s", self.name, exception)
            if self.unsub:
                self.unsub()
                self.unsub = None
            self.last_update_success = False
            self.async_update_listeners()

        self.last_update_success = True
        self.async_update_listeners()

        async def close_websocket(_) -> None:
            """Close WebSocket connection."""
            await self.websocket.close()

        # Clean disconnect WebSocket on Home Assistant shutdown
        self.unsub = self.hass.bus.async_listen_once(
            EVENT_HOMEASSISTANT_STOP, close_websocket
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            if not self.websocket.connected:
                await self._setup_websocket()

            data: Any = {}
            data["cc_dv"] = await self.websocket.get_charge_control_dynamic_values()
            data["cc_s"] = await self.websocket.get_charge_control_settings()
            data["w_s"] = await self.websocket.get_wifi_status()
            return data
        except Exception:
            # Most likely a connection issue. Retry later
            raise UpdateFailed
