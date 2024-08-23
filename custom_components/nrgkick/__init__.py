"""The NRGKick integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import _LOGGER, HomeAssistant, callback
from homeassistant.helpers import entity_registry as er

from .const import DOMAIN
from .coordinator import NRGKickCoordinator

PLATFORMS: list[Platform] = [Platform.NUMBER, Platform.SENSOR, Platform.SWITCH]


async def _async_migrate_entries(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    entity_registry = er.async_get(hass)

    @callback
    def update_unique_id(entry: er.RegistryEntry) -> dict[str, str] | None:
        replacements = {
            "charge_current_max_adapter": "connector_max_current",
            "wifi_network": "network_ssid",
            "charge_current_user_set": "current_set",
            "energy_limit_value": "energy_limit",
            "total_charged_energy": "energy_total_charged_energy",
            "charged_energy": "energy_charged_energy",
            "charging_voltage": "powerflow_charging_voltage",
            "charge_current_value": "powerflow_charging_current",
            "peak_charging_power": "powerflow_peak_power",
            "charging_power": "powerflow_total_active_power",
            "voltage_phase_a": "powerflow_l1_voltage",
            "charging_current_phase_a": "powerflow_l1_current",
            "charging_power_phase_a": "powerflow_l1_active_power",
            "voltage_phase_b": "powerflow_l2_voltage",
            "charging_current_phase_b": "powerflow_l2_current",
            "charging_power_phase_b": "powerflow_l2_active_power",
            "voltage_phase_c": "powerflow_l3_voltage",
            "charging_current_phase_c": "powerflow_l3_current",
            "charging_power_phase_c": "powerflow_l3_active_power",
            "charging_rate": "general_charging_rate",
            "charging_state": "general_status",
            "total_charging_cycles": "general_charge_count",
            "control_pilot_status": "general_error_code",
        }
        if (key := entry.unique_id.split("_", 1)[-1]) in replacements:
            new_unique_id = entry.unique_id.replace(key, replacements[key])
            _LOGGER.debug(
                "Migrating entity '%s' unique_id from '%s' to '%s'",
                entry.entity_id,
                entry.unique_id,
                new_unique_id,
            )
            if existing_entity_id := entity_registry.async_get_entity_id(
                entry.domain, entry.platform, new_unique_id
            ):
                _LOGGER.debug(
                    "Cannot migrate to unique_id '%s', already exists for '%s'",
                    new_unique_id,
                    existing_entity_id,
                )
                return None
            return {
                "new_unique_id": new_unique_id,
            }
        return None

    await er.async_migrate_entries(hass, entry.entry_id, update_unique_id)

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up NRGKick from a config entry."""

    await _async_migrate_entries(hass, entry)

    coordinator = NRGKickCoordinator(
        hass, entry.data["url"], entry.data["login"], entry.data["password"]
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
