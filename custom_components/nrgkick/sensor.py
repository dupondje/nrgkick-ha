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
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    UnitOfApparentPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfReactivePower,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import NRGKickCoordinator
from .const import DOMAIN
from .entity import NRGKickEntity


@dataclass(frozen=True)
class NRGKickMixin:
    """Mixin for required keys."""

    value_fn: Callable[[Any], StateType]


@dataclass(frozen=True)
class NRGKickSensorEntityDescription(SensorEntityDescription, NRGKickMixin):
    """Describes the NRGKick Sensor Entity."""


SENSORS = [
    # INFO - General
    NRGKickSensorEntityDescription(
        key="rated_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["info"]["general"]["rated_current"],
    ),
    # INFO - Connector
    NRGKickSensorEntityDescription(
        key="connector_phase_count",
        value_fn=lambda data: data["info"]["connector"]["phase_count"],
    ),
    NRGKickSensorEntityDescription(
        key="connector_max_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["info"]["connector"]["max_current"]
        if "max_current" in data["info"]["connector"]
        else data["info"]["connector"]["max_current:"],
    ),
    NRGKickSensorEntityDescription(
        key="connector_type",
        value_fn=lambda data: data["info"]["connector"]["type"],
    ),
    NRGKickSensorEntityDescription(
        key="connector_serial",
        value_fn=lambda data: data["info"]["connector"]["serial"],
    ),
    # INFO - Grid
    NRGKickSensorEntityDescription(
        key="grid_voltage",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=2,
        value_fn=lambda data: data["info"]["grid"]["voltage"],
    ),
    NRGKickSensorEntityDescription(
        key="grid_frequency",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.FREQUENCY,
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        suggested_display_precision=2,
        value_fn=lambda data: data["info"]["grid"]["frequency"]
        if "frequency" in data["info"]["grid"]
        else data["info"]["grid"]["frequency:"],
    ),
    NRGKickSensorEntityDescription(
        key="grid_phases",
        value_fn=lambda data: data["info"]["grid"]["phases"],
    ),
    # INFO - Network
    NRGKickSensorEntityDescription(
        key="network_ip_address",
        value_fn=lambda data: data["info"]["network"]["ip_address"],
    ),
    NRGKickSensorEntityDescription(
        key="network_mac_address",
        value_fn=lambda data: data["info"]["network"]["mac_address"],
    ),
    NRGKickSensorEntityDescription(
        key="network_ssid",
        value_fn=lambda data: data["info"]["network"]["ssid"],
    ),
    NRGKickSensorEntityDescription(
        key="network_rssi",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        value_fn=lambda data: data["info"]["network"]["rssi"],
    ),
    # INFO - Versions
    NRGKickSensorEntityDescription(
        key="versions_sw_sm",
        value_fn=lambda data: data["info"]["versions"]["sw_sm"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_hw_sm",
        value_fn=lambda data: data["info"]["versions"]["hw_sm"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_sw_ma",
        value_fn=lambda data: data["info"]["versions"]["sw_ma"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_hw_ma",
        value_fn=lambda data: data["info"]["versions"]["hw_ma"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_sw_to",
        value_fn=lambda data: data["info"]["versions"]["sw_to"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_hw_to",
        value_fn=lambda data: data["info"]["versions"]["hw_to"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_sw_st",
        value_fn=lambda data: data["info"]["versions"]["sw_st"],
        entity_registry_enabled_default=False,
    ),
    NRGKickSensorEntityDescription(
        key="versions_hw_st",
        value_fn=lambda data: data["info"]["versions"]["hw_st"],
        entity_registry_enabled_default=False,
    ),
    # Control
    NRGKickSensorEntityDescription(
        key="current_set",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["control"]["current_set"],
    ),
    NRGKickSensorEntityDescription(
        key="charge_pause",
        value_fn=lambda data: data["control"]["charge_pause"],
    ),
    NRGKickSensorEntityDescription(
        key="energy_limit",
        state_class=SensorStateClass.TOTAL,
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        suggested_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        suggested_display_precision=3,
        value_fn=lambda data: round(data["control"]["energy_limit"], 3),
    ),
    NRGKickSensorEntityDescription(
        key="phase_count",
        value_fn=lambda data: data["control"]["phase_count"],
    ),
    # VALUES - Energy
    NRGKickSensorEntityDescription(
        key="energy_total_charged_energy",
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        suggested_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        suggested_display_precision=3,
        value_fn=lambda data: data["values"]["energy"]["total_charged_energy"],
    ),
    NRGKickSensorEntityDescription(
        key="energy_charged_energy",
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.ENERGY,
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        suggested_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        suggested_display_precision=3,
        value_fn=lambda data: data["values"]["energy"]["charged_energy"],
    ),
    # VALUES - Powerflow
    NRGKickSensorEntityDescription(
        key="powerflow_charging_voltage",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["charging_voltage"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_charging_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["charging_current"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_grid_frequency",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.FREQUENCY,
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["grid_frequency"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_peak_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["peak_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_total_active_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["total_active_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_total_reactive_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.REACTIVE_POWER,
        native_unit_of_measurement=UnitOfReactivePower.VOLT_AMPERE_REACTIVE,
        value_fn=lambda data: data["values"]["powerflow"]["total_reactive_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_total_apparent_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.APPARENT_POWER,
        native_unit_of_measurement=UnitOfApparentPower.VOLT_AMPERE,
        value_fn=lambda data: data["values"]["powerflow"]["total_apparent_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_total_total_power_factor",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: data["values"]["powerflow"]["total_power_factor"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_voltage",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["voltage"]
        if "voltage" in data["values"]["powerflow"]["l1"]
        else data["values"]["powerflow"]["l1"]["voltage:"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["current"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_active_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["active_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_reactive_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.REACTIVE_POWER,
        native_unit_of_measurement=UnitOfReactivePower.VOLT_AMPERE_REACTIVE,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["reactive_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_apparent_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.APPARENT_POWER,
        native_unit_of_measurement=UnitOfApparentPower.VOLT_AMPERE,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["apparent_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l1_power_factor",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: data["values"]["powerflow"]["l1"]["power_factor"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_voltage",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["voltage"]
        if "voltage" in data["values"]["powerflow"]["l2"]
        else data["values"]["powerflow"]["l2"]["voltage:"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["current"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_active_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["active_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_reactive_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.REACTIVE_POWER,
        native_unit_of_measurement=UnitOfReactivePower.VOLT_AMPERE_REACTIVE,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["reactive_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_apparent_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.APPARENT_POWER,
        native_unit_of_measurement=UnitOfApparentPower.VOLT_AMPERE,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["apparent_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l2_power_factor",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: data["values"]["powerflow"]["l2"]["power_factor"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_voltage",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["voltage"]
        if "voltage" in data["values"]["powerflow"]["l3"]
        else data["values"]["powerflow"]["l3"]["voltage:"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["current"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_active_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["active_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_reactive_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.REACTIVE_POWER,
        native_unit_of_measurement=UnitOfReactivePower.VOLT_AMPERE_REACTIVE,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["reactive_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_apparent_power",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.APPARENT_POWER,
        native_unit_of_measurement=UnitOfApparentPower.VOLT_AMPERE,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["apparent_power"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_l3_power_factor",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: data["values"]["powerflow"]["l3"]["power_factor"],
    ),
    NRGKickSensorEntityDescription(
        key="powerflow_n_current",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_display_precision=2,
        value_fn=lambda data: data["values"]["powerflow"]["n"]["current"],
    ),
    # VALUES - General
    NRGKickSensorEntityDescription(
        key="general_charging_rate",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["values"]["general"]["charging_rate"],
    ),
    NRGKickSensorEntityDescription(
        key="general_vehicle_connect_time",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        value_fn=lambda data: data["values"]["general"]["vehicle_connect_time"],
    ),
    NRGKickSensorEntityDescription(
        key="general_vehicle_charging_time",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        value_fn=lambda data: data["values"]["general"]["vehicle_charging_time"],
    ),
    NRGKickSensorEntityDescription(
        key="general_status",
        value_fn=lambda data: data["values"]["general"]["status"],
    ),
    NRGKickSensorEntityDescription(
        key="general_charge_permitted",
        value_fn=lambda data: data["values"]["general"]["charge_permitted"],
    ),
    NRGKickSensorEntityDescription(
        key="general_relay_state",
        value_fn=lambda data: data["values"]["general"]["relay_state"],
    ),
    NRGKickSensorEntityDescription(
        key="general_charge_count",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data["values"]["general"]["charge_count"],
    ),
    NRGKickSensorEntityDescription(
        key="general_rcd_trigger",
        value_fn=lambda data: data["values"]["general"]["rcd_trigger"],
    ),
    NRGKickSensorEntityDescription(
        key="general_warning_code",
        value_fn=lambda data: data["values"]["general"]["warning_code"],
    ),
    NRGKickSensorEntityDescription(
        key="general_error_code",
        value_fn=lambda data: data["values"]["general"]["error_code"],
    ),
    # VALUES - Temperatures
    NRGKickSensorEntityDescription(
        key="temperatures_housing",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["housing"],
    ),
    NRGKickSensorEntityDescription(
        key="temperatures_connector_l1",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["connector_l1"],
    ),
    NRGKickSensorEntityDescription(
        key="temperatures_connector_l2",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["connector_l2"],
    ),
    NRGKickSensorEntityDescription(
        key="temperatures_connector_l3",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["connector_l3"],
    ),
    NRGKickSensorEntityDescription(
        key="temperatures_domestic_plug_1",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["domestic_plug_1"],
    ),
    NRGKickSensorEntityDescription(
        key="temperatures_domestic_plug_2",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        value_fn=lambda data: data["values"]["temperatures"]["domestic_plug_2"],
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
        try:
            return self.entity_description.value_fn(self.coordinator.data)
        except KeyError:
            return None
