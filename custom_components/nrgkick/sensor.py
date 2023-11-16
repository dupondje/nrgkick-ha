"""NRGKick sensor class."""

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfElectricCurrent,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import NRGKickCoordinator
from .const import DOMAIN
from .entity import NRGKickEntity
from .proto import nrgcp_pb2 as nrgcp


@dataclass
class NRGKickMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], StateType]


@dataclass
class NRGKickSensorEntityDescription(SensorEntityDescription, NRGKickMixin):
    """Describes the NRGKick Sensor Entity."""


SENSORS = [
    NRGKickSensorEntityDescription(
        key="current_grid_frequency",
        translation_key="current_grid_frequency",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.FREQUENCY,
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.gridFrequency,
    ),
    NRGKickSensorEntityDescription(
        key="peak_charging_power",
        translation_key="peak_charging_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.peakPower,
    ),
    NRGKickSensorEntityDescription(
        key="current_charging_power",
        translation_key="current_charging_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.chargingPower,
    ),
    NRGKickSensorEntityDescription(
        key="charged_energy",
        translation_key="charged_energy",
        state_class=SensorStateClass.TOTAL,
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        suggested_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        suggested_display_precision=3,
        value_fn=lambda data: data["cc_dv"].chargingData.chargedEnergy,
    ),
    NRGKickSensorEntityDescription(
        key="total_charged_energy",
        translation_key="total_charged_energy",
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        suggested_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        suggested_display_precision=3,
        value_fn=lambda data: data["cc_dv"].chargingData.totalChargedEnergy,
    ),
    NRGKickSensorEntityDescription(
        key="current_charging_power_phase_a",
        translation_key="current_charging_power_phase_a",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.phaseA.power,
    ),
    NRGKickSensorEntityDescription(
        key="current_charging_power_phase_b",
        translation_key="current_charging_power_phase_b",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.phaseB.power,
    ),
    NRGKickSensorEntityDescription(
        key="current_charging_power_phase_c",
        translation_key="current_charging_power_phase_c",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_dv"].chargingData.phaseC.power,
    ),
    # Charge Control Settings
    NRGKickSensorEntityDescription(
        key="current_charging_current",
        translation_key="current_charging_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_s"].chargeCurrent.value,
    ),
    NRGKickSensorEntityDescription(
        key="charge_current_limit",
        translation_key="charge_current_limit",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["cc_s"].chargeCurrent.userSet,
    ),
    NRGKickSensorEntityDescription(
        key="charging_state",
        translation_key="charging_state",
        value_fn=lambda data: nrgcp.NrgcpTypes.ChargingState.Name(
            data["cc_s"].chargingState.value
        ),
    ),
    NRGKickSensorEntityDescription(
        key="total_charging_cycles",
        translation_key="total_charging_cycles",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data["cc_s"].chargingCycle,
    ),
    ### Wifi Status
    NRGKickSensorEntityDescription(
        key="wifi_network",
        translation_key="wifi_network",
        value_fn=lambda data: data["w_s"].ap.ssid,
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the NRGKick sensor."""

    coordinator: NRGKickCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    async_add_entities(NRGKickSensor(coordinator, sensor) for sensor in SENSORS)


class NRGKickSensor(NRGKickEntity, SensorEntity):
    """An NRGKickSensor."""

    entity_description: NRGKickSensorEntityDescription

    @property
    def native_value(self) -> StateType:
        """Return the value reported by the sensor."""
        return self.entity_description.value_fn(self.coordinator.data)
