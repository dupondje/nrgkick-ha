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

    def __init__(self, _ip: str, _uuid: str) -> None:
        """Init NRGKickWebsocket."""
        self._ip = _ip
        self._uuid = _uuid
        self._websocket: Optional[websockets.client.WebSocketClientProtocol] = None
        self._receive_task: Optional[asyncio.Task] = None
        self._running = False
        self._connected = asyncio.Event()
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

    def stop(self) -> None:
        """Stop the connection."""
        self._running = False

    async def connect(self) -> None:
        """Connect to the NRGKick device."""
        self._receive_task = asyncio.create_task(self.__connect_loop())

    async def __connect_loop(self):
        self._running = True
        while self._running:
            async for self._websocket in websockets.connect(f"ws://{self._ip}:8765"):
                try:
                    self._connected.set()
                    await self.__receive_loop()
                except websockets.ConnectionClosed:
                    continue
        await self._websocket.close()

    async def __receive_loop(self):
        while self._running:
            try:
                await self._connected.wait()
                response = await self._websocket.recv()
                data = nrgcp.Nrgcp()
                data.ParseFromString(response)
                event = self._requests.get(data.metadata.requestId)
                if event is not None:
                    self._responses[data.metadata.requestId] = data
                    event.set()
            except websockets.ConnectionClosed:
                self._connected.clear()
                raise

    async def __send(self, event: asyncio.Event, data: nrgcp.Nrgcp):
        self._requests[str(data.metadata.requestId)] = event
        try:
            await self._connected.wait()
            if self._websocket:
                await self._websocket.send(data.SerializeToString())
        except Exception:  # pylint: disable=broad-except
            _LOGGER.warning("Failed to send message to NRGKick")

    def __get_base_request(self) -> nrgcp.Nrgcp:
        request = nrgcp.Nrgcp()
        request.header.type = nrgcp.Nrgcp.Header.Type.GET
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

        await self.__send(event, request)
        async with asyncio.timeout(5):
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

        await self.__send(event, request)
        async with asyncio.timeout(5):
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

        await self.__send(event, request)
        async with asyncio.timeout(5):
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

        await self.__send(event, request)
        async with asyncio.timeout(5):
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

        await self.__send(event, request)
        async with asyncio.timeout(5):
            await event.wait()

        data = self._responses.pop(str(request.metadata.requestId))
        if data is None:
            return False
        return True

    async def set_charging_state(self, state: nrgcp.NrgcpTypes.ChargingState) -> bool:
        """Set the charging ."""
        event = asyncio.Event()

        request = self.__get_base_request()
        request.header.type = nrgcp.Nrgcp.Header.Type.UPDATE
        request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
        request.header.property = nrgcp.Nrgcp.Header.Property.SETTINGS

        request.payload.CHARGECONTROL_SETTINGS_UPDATE.chargingState.value = state

        await self.__send(event, request)
        async with asyncio.timeout(5):
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
