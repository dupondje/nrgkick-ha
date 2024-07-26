"""NRGKick entity class."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import NRGKickCoordinator


class NRGKickEntity(CoordinatorEntity[NRGKickCoordinator]):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available

    """

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: NRGKickCoordinator,
        description: EntityDescription,
    ) -> None:
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator)
        self.entity_description = description

        if coordinator.config_entry:
            serial = coordinator.config_entry.data["serial"]
            dev_name = coordinator.config_entry.data["name"]
            self._attr_unique_id = f"{serial}_{description.key}"
            self._attr_device_info = DeviceInfo(
                identifiers={(DOMAIN, serial)},
                manufacturer="DiniTech",
                model=coordinator.config_entry.data["model"],
                name=dev_name,
                serial_number=serial,
            )

    @property
    def translation_key(self):
        """Return the translation key to translate the entity's name and states."""
        return self.entity_description.key
