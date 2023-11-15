"""Number platform for NRGKick."""

from collections.abc import Callable, Coroutine
from dataclasses import dataclass
import logging
from typing import Any

from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntity,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfElectricCurrent
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import NRGKickCoordinator
from .entity import NRGKickEntity

_LOGGER = logging.getLogger(__name__)


@dataclass
class NRGKickRequiredKeysMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], float | int | None]
    api_fn: Callable[[Any, float | int], Coroutine[Any, Any, Any]]


@dataclass
class NRGKickNumberEntityDescription(NumberEntityDescription, NRGKickRequiredKeysMixin):
    """Describes NRGKick number entity."""


NUMBERS: list[NRGKickNumberEntityDescription] = [
    NRGKickNumberEntityDescription(
        key="charge_current_limit",
        translation_key="charge_current_limit",
        device_class=NumberDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        native_max_value=32.0,
        native_min_value=6.0,
        native_step=1.0,
        mode=NumberMode.SLIDER,
        value_fn=lambda data: data["cc_s"].chargeCurrent.userSet,
        api_fn=lambda c, v: c.set_charge_current_limit(v),
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
        return self.entity_description.value_fn(self.coordinator.data)

    async def async_set_native_value(self, value: float) -> None:
        """Update to the cable."""
        _LOGGER.debug(
            "Settings charge level to '%s'",
            value,
        )
        await self.entity_description.api_fn(self.coordinator.websocket, value)
        await self.coordinator.async_refresh()
