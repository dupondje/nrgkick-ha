import asyncio
import pprint
import uuid
import websockets
from .proto import nrgcp_pb2 as nrgcp


class NRGKickWebsocket:
    def __init__(self, _ip: str, _uuid: str) -> None:
        self._ip = _ip
        self._uuid = _uuid
        self._websocket = None
        self._loop = asyncio.get_event_loop()

    @property
    def ip(self):
        return self._ip

    @property
    def uuid(self):
        return self._uuid

    async def connect(self) -> None:
        self._websocket = await websockets.connect(f"ws://{self._ip}:8765")

    def __get_info(
        self, service: nrgcp.Nrgcp.Header.Service, prop: nrgcp.Nrgcp.Header.Property
    ) -> str:
        request = nrgcp.Nrgcp()
        request.header.type = nrgcp.Nrgcp.Header.Type.GET
        request.header.service = service
        request.header.property = prop
        request.header.uuid = self.uuid

        request.metadata.requestId = str(uuid.uuid4())[-8:]

        return request.SerializeToString()

    async def get_charge_control_dynamic_values(
        self,
    ) -> nrgcp.NrgcpChargecontrolDynamicvaluesGetPayload:
        try:
            if self._websocket.closed:
                await self.connect()
            await self._websocket.send(
                self.__get_info(
                    nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL,
                    nrgcp.Nrgcp.Header.Property.DYNAMIC_VALUES,
                )
            )
            response = await self._websocket.recv()
            data = nrgcp.Nrgcp()
            data.ParseFromString(response)
            return data.payload.CHARGECONTROL_DYNAMICVALUES_GET
        except websockets.ConnectionClosed:
            self._websocket = None
            self.connect()

        return None

    async def get_charge_control_settings(
        self,
    ) -> nrgcp.NrgcpChargecontrolSettingsGetPayload:
        try:
            if self._websocket.closed:
                await self.connect()
            await self._websocket.send(
                self.__get_info(
                    nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL,
                    nrgcp.Nrgcp.Header.Property.SETTINGS,
                )
            )
            response = await self._websocket.recv()
            data = nrgcp.Nrgcp()
            data.ParseFromString(response)
            return data.payload.CHARGECONTROL_SETTINGS_GET
        except websockets.ConnectionClosed:
            self._websocket = None
            self.connect()

        return None

    async def get_device_control_info(self) -> nrgcp.NrgcpDevicecontrolInfoGetPayload:
        try:
            if self._websocket.closed:
                await self.connect()
            await self._websocket.send(
                self.__get_info(
                    nrgcp.Nrgcp.Header.Service.DEVICE_CONTROL,
                    nrgcp.Nrgcp.Header.Property.INFO,
                )
            )
            response = await self._websocket.recv()
            data = nrgcp.Nrgcp()
            data.ParseFromString(response)
            pprint.pprint(data)
            return data.payload.DEVICECONTROL_INFO_GET
        except websockets.ConnectionClosed:
            self._websocket = None
            self.connect()

        return None

    async def get_wifi_status(self) -> nrgcp.NrgcpWifiStatusGetPayload:
        try:
            if self._websocket.closed:
                await self.connect()
            await self._websocket.send(
                self.__get_info(
                    nrgcp.Nrgcp.Header.Service.WIFI,
                    nrgcp.Nrgcp.Header.Property.STATUS,
                )
            )
            response = await self._websocket.recv()
            data = nrgcp.Nrgcp()
            data.ParseFromString(response)
            pprint.pprint(data)
            return data.payload.WIFI_STATUS_GET
        except websockets.ConnectionClosed:
            self._websocket = None
            self.connect()

        return None

    async def set_charge_current_limit(self, limit: float) -> bool:
        try:
            if self._websocket.closed:
                await self.connect()

            request = nrgcp.Nrgcp()
            request.header.type = nrgcp.Nrgcp.Header.Type.UPDATE
            request.header.service = nrgcp.Nrgcp.Header.Service.CHARGE_CONTROL
            request.header.property = nrgcp.Nrgcp.Header.Property.SETTINGS
            request.header.uuid = self.uuid

            request.metadata.requestId = str(uuid.uuid4())[-8:]

            request.payload.CHARGECONTROL_SETTINGS_UPDATE.chargeCurrent.userSet = limit

            await self._websocket.send(request.SerializeToString())
            response = await self._websocket.recv()
            data = nrgcp.Nrgcp()
            data.ParseFromString(response)
            pprint.pprint(data)
            return data.payload.CHARGECONTROL_SETTINGS_UPDATE
        except websockets.ConnectionClosed:
            self._websocket = None
            self.connect()

        return None
