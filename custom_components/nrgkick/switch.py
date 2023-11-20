"""Switch platform for NRGKick."""

from collections.abc import Callable, Coroutine
from dataclasses import dataclass
import logging
from typing import Any

from homeassistant.components.switch import (
    SwitchDeviceClass,
    SwitchEntity,
    SwitchEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import NRGKickCoordinator
from .entity import NRGKickEntity

_LOGGER = logging.getLogger(__name__)


@dataclass
class NRGKickRequiredKeysMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], bool]
    switch_fn: Callable[[Any, float | int], Coroutine[Any, Any, Any]]


@dataclass
class NRGKickSwitchEntityDescription(SwitchEntityDescription, NRGKickRequiredKeysMixin):
    """Describes NRGKick switch entity."""


SWITCHES: list[NRGKickSwitchEntityDescription] = [
    NRGKickSwitchEntityDescription(
        key="charging_state",
        translation_key="charging_state",
        device_class=SwitchDeviceClass.SWITCH,
        value_fn=lambda data: data["cc_s"].chargingState.value == 1,
        switch_fn=lambda c, v: c.set_charging_state_bool(v),
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the NRGKick switch from config entry."""
    coordinator: NRGKickCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    async_add_entities(NRGKickSwitch(coordinator, switch) for switch in SWITCHES)


class NRGKickSwitch(NRGKickEntity, SwitchEntity):
    """Representation of NRGKick Switch entity."""

    entity_description: NRGKickSwitchEntityDescription

    @property
    def is_on(self) -> bool:
        """Return the charging state."""
        return self.entity_description.value_fn(self.coordinator.data)

    async def async_turn_on(self):
        """Turn on charging."""
        await self.entity_description.switch_fn(self.coordinator.websocket, True)
        # There is some delay between the response on the SET
        # and the CHARGECONTROL_SETTINGS_GET value to get updated
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self):
        """Turn off charging."""
        await self.entity_description.switch_fn(self.coordinator.websocket, False)
        # There is some delay between the response on the SET
        # and the CHARGECONTROL_SETTINGS_GET value to get updated
        await self.coordinator.async_request_refresh()