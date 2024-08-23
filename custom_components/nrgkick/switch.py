"""Switch platform for NRGKick."""

import asyncio
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


@dataclass(frozen=True)
class NRGKickRequiredKeysMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], bool]
    switch_fn: Callable[[Any, float | int], Coroutine[Any, Any, Any]]


@dataclass(frozen=True)
class NRGKickSwitchEntityDescription(SwitchEntityDescription, NRGKickRequiredKeysMixin):
    """Describes NRGKick switch entity."""


SWITCHES: list[NRGKickSwitchEntityDescription] = [
    NRGKickSwitchEntityDescription(
        key="charge_pause",
        device_class=SwitchDeviceClass.SWITCH,
        value_fn=lambda data: data["control"]["charge_pause"] == 1,
        switch_fn=lambda c, v: c.set("control", "charge_pause", v),
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
        try:
            return self.entity_description.value_fn(self.coordinator.data)
        except KeyError:
            return False

    async def async_turn_on(self):
        """Turn on charging."""
        await self.entity_description.switch_fn(self.coordinator, 1)
        # There is some delay between the response on the SET
        # and the CHARGECONTROL_SETTINGS_GET value to get updated
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self):
        """Turn off charging."""
        await self.entity_description.switch_fn(self.coordinator, 0)
        # There is some delay between the response on the SET
        # and the CHARGECONTROL_SETTINGS_GET value to get updated
        # Sleep 2 seconds to make sure the device status is updated
        await asyncio.sleep(2)
        await self.coordinator.async_request_refresh()
