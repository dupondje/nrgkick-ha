"""NRGKick coordinator class."""

from datetime import timedelta
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class NRGKickCoordinator(DataUpdateCoordinator):
    """NRGKick coordinator."""

    def __init__(self, hass: HomeAssistant, websocket) -> None:
        """Initialize NRGKick."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.websocket = websocket

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            data = {}
            data["cc_dv"] = await self.websocket.get_charge_control_dynamic_values()
            data["cc_s"] = await self.websocket.get_charge_control_settings()
            data["w_s"] = await self.websocket.get_wifi_status()
            return data
        except Exception:
            # Most likely a connection issue. Retry later
            raise UpdateFailed
