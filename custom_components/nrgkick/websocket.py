"""NRGKick websocket implementation."""

import asyncio
import logging
from typing import Optional
import uuid

import websockets
import websockets.client

from .proto import nrgcp_pb2 as nrgcp

_LOGGER = logging.getLogger(__name__)


class NRGKickWebsocket:
    """Definition of a NRGKickWebsocket."""

    def __init__(self, _ip: str, _uuid: str | None) -> None:
        """Init NRGKickWebsocket."""
        self._ip = _ip
        self._uuid = _uuid
        self._websocket: Optional[websockets.client.WebSocketClientProtocol] = None
        self._receive_task: Optional[asyncio.Task] = None
        self._connected = False
        self._requests: dict[str, asyncio.Event] = {}
        self._responses: dict[str, nrgcp.Nrgcp] = {}

    @property
    def ip(self):
        """Returns the IP address."""
        return self._ip

    @property
    def uuid(self):
        """Returns the UUID."""
        return self._uuid

    @property
    def connected(self) -> bool:
        """Returns if the websocket is connected."""
        return self._connected

    async def close(self) -> None:
        """Stop the connection."""
        self._connected = False
        if self._receive_task:
            self._receive_task.cancel()
            self._receive_task = None
        if self._websocket:
            await self._websocket.close()

    async def connect(self) -> None:
        """Connect to the NRGKick device."""
        self._websocket = await websockets.connect(f"ws://{self._ip}:8765")
        self._connected = True
        if self._receive_task:
            self._receive_task.cancel()
            self._receive_task = None
        self._receive_task = asyncio.create_task(self.__receive_loop())

    async def __receive_loop(self):
        while self._connected:
            try:
                response = await self._websocket.recv()
                data = nrgcp.Nrgcp()
                data.ParseFromString(response)
                event = self._requests.get(data.metadata.requestId)
                if event is not None:
                    self._responses[data.metadata.requestId] = data
                    event.set()
            except websockets.ConnectionClosed:
                _LOGGER.warning("Connection to NRGKick closed")

    async def __send(self, event: asyncio.Event, data: nrgcp.Nrgcp):
        self._requests[str(data.metadata.requestId)] = event
        try:
            if self._websocket:
                await self._websocket.send(data.SerializeToString())
        except Exception:  # pylint: disable=broad-except
            _LOGGER.warning("Failed to send message to NRGKick")

    def __get_base_request(self) -> nrgcp.Nrgcp:
        request = nrgcp.Nrgcp()
        request.header.type = nrgcp.Nrgcp.Header.Type.GET
        if self.uuid:
            request.header.uuid = self.uuid

        request.metadata.requestId = str(uuid.uuid4())[-8:]

        return request

    async def get_charge_control_dynamic_values(
        self,
    ) -> nrgcp.NrgcpChargecontrolDynamicvaluesGetPayload | None:
        """Get the CHARGECONTROL_DYNAMICVALUES."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.DYNAMIC_VALUES

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return None
        return data.payload.CHARGECONTROL_DYNAMICVALUES_GET

    async def get_charge_control_settings(
        self,
    ) -> nrgcp.NrgcpChargecontrolSettingsGetPayload | None:
        """Get the CHARGECONTROL_SETTINGS."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.SETTINGS

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return None
        return data.payload.CHARGECONTROL_SETTINGS_GET

    async def get_device_control_info(
        self,
    ) -> nrgcp.NrgcpDevicecontrolInfoGetPayload | None:
        """Get the DEVICECONTROL_INFO."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.service = nrgcp.Nrgcp.Header.Service.DEVICE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.INFO

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return None
        return data.payload.DEVICECONTROL_INFO_GET

    async def get_wifi_status(
        self,
    ) -> nrgcp.NrgcpWifiStatusGetPayload | None:
        """Get the WIFI_STATUS."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.service = nrgcp.Nrgcp.Header.Service.WIFI
        request.header.property = nrgcp.Nrgcp.Header.Property.STATUS

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return None
        return data.payload.WIFI_STATUS_GET

    async def set_charge_current_limit(self, limit: float) -> bool:
        """Set the charging current limit."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.type = nrgcp.Nrgcp.Header.Type.UPDATE
        request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.SETTINGS

        request.payload.CHARGECONTROL_SETTINGS_UPDATE.chargeCurrent.userSet = limit

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return False
        return True

    async def set_charging_state(self, state: nrgcp.NrgcpTypes.ChargingState) -> bool:
        """Set the charging state."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.type = nrgcp.Nrgcp.Header.Type.UPDATE
        request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.SETTINGS

        request.payload.CHARGECONTROL_SETTINGS_UPDATE.chargingState.value = state

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return False
        return True

    async def set_charging_state_bool(self, state: bool) -> bool:
        """Stop of start charging (bool)."""
        nrgcpState = nrgcp.NrgcpTypes.ChargingState.PAUSE_CHARGING
        if state:
            nrgcpState = nrgcp.NrgcpTypes.ChargingState.CHARGING
        return await self.set_charging_state(nrgcpState)

    async def create_uuid(self, pin: str) -> str | None:
        """Create a new UUID."""
        event = asyncio.Event()

        request = self.__get_base_request()

        request.header.type = nrgcp.Nrgcp.Header.Type.UPDATE
        request.header.service = nrgcp.Nrgcp.Header.Service.DEVICE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.INFO

        devUUID = str(uuid.uuid4())

        request.payload.DEVICECONTROL_INFO_UPDATE.devicePin.accessControlState = (
            nrgcp.NrgcpTypes.AccessControlState.AUTHORIZE_CLIENT
        )
        request.payload.DEVICECONTROL_INFO_UPDATE.devicePin.pin = pin
        request.payload.DEVICECONTROL_INFO_UPDATE.devicePin.uuid = devUUID

        async with asyncio.timeout(5):
            await self.__send(event, request)
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return None

        if data.header.status != nrgcp.Nrgcp.Header.Status.ACCEPTED:
            return None
        return devUUID
