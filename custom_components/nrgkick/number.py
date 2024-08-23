"""Number platform for NRGKick."""

import asyncio
from collections.abc import Callable, Coroutine
from dataclasses import dataclass
import logging
from typing import Any

from homeassistant.components.number import (
    DEFAULT_MAX_VALUE,
    DEFAULT_MIN_VALUE,
    NumberDeviceClass,
    NumberEntity,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfElectricCurrent, UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import NRGKickCoordinator
from .entity import NRGKickEntity

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class NRGKickRequiredKeysMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], float | int | None]
    api_fn: Callable[[Any, float | int], Coroutine[Any, Any, Any]]


@dataclass(frozen=True)
class NRGKickNumberEntityDescription(NumberEntityDescription, NRGKickRequiredKeysMixin):
    """Describes NRGKick number entity."""

    native_max_value_fn: Callable[[Any], float] | None = None
    native_min_value_fn: Callable[[Any], float] | None = None


NUMBERS: list[NRGKickNumberEntityDescription] = [
    NRGKickNumberEntityDescription(
        key="current_set",
        device_class=NumberDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        native_max_value_fn=lambda data: data["info"]["general"]["rated_current"],
        native_min_value=6.0,
        native_step=0.1,
        mode=NumberMode.SLIDER,
        value_fn=lambda data: data["control"]["current_set"],
        api_fn=lambda c, v: c.set("control", "current_set", v),
    ),
    NRGKickNumberEntityDescription(
        key="energy_limit",
        device_class=NumberDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        native_max_value=1000000,
        native_min_value=0,
        native_step=1,
        mode=NumberMode.BOX,
        value_fn=lambda data: data["control"]["energy_limit"],
        api_fn=lambda c, v: c.set("control", "energy_limit", int(v)),
    ),
    NRGKickNumberEntityDescription(
        key="phase_count",
        native_max_value=3,
        native_min_value=1,
        native_step=1,
        mode=NumberMode.SLIDER,
        value_fn=lambda data: data["control"]["phase_count"],
        api_fn=lambda c, v: c.set("control", "phase_count", int(v)),
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the NRGKick number from config entry."""
    coordinator: NRGKickCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    async_add_entities(NRGKickNumber(coordinator, number) for number in NUMBERS)


class NRGKickNumber(NRGKickEntity, NumberEntity):
    """Representation of NRGKick Number entity."""

    entity_description: NRGKickNumberEntityDescription

    @property
    def native_value(self) -> float | None:
        """Return the entity value to represent the entity state."""
        try:
            return self.entity_description.value_fn(self.coordinator.data)
        except KeyError:
            return None

    @property
    def native_min_value(self) -> float:
        """Return the minimum value."""
        if self.entity_description.native_min_value_fn is not None:
            return self.entity_description.native_min_value_fn(self.coordinator.data)
        if self.entity_description.native_min_value is not None:
            return self.entity_description.native_min_value
        return DEFAULT_MIN_VALUE

    @property
    def native_max_value(self) -> float:
        """Return the maximum value."""
        if self.entity_description.native_max_value_fn is not None:
            return self.entity_description.native_max_value_fn(self.coordinator.data)
        if self.entity_description.native_max_value is not None:
            return self.entity_description.native_max_value
        return DEFAULT_MAX_VALUE

    async def async_set_native_value(self, value: float) -> None:
        """Update to the cable."""
        _LOGGER.debug(
            "Settings charge level to '%s'",
            value,
        )
        await self.entity_description.api_fn(self.coordinator, value)
        # Sleep 2 seconds to make sure the device status is updated
        await asyncio.sleep(2)
        await self.coordinator.async_refresh()
