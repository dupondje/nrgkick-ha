from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Nrgcp(_message.Message):
    __slots__ = ("header", "metadata", "payload")
    class Header(_message.Message):
        __slots__ = ("type", "status", "service", "property", "uuid")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Nrgcp.Header.Type]
            GET: _ClassVar[Nrgcp.Header.Type]
            UPDATE: _ClassVar[Nrgcp.Header.Type]
            NOTIFY: _ClassVar[Nrgcp.Header.Type]
            DELETE: _ClassVar[Nrgcp.Header.Type]
            ADD: _ClassVar[Nrgcp.Header.Type]
        UNKNOWN_TYPE: Nrgcp.Header.Type
        GET: Nrgcp.Header.Type
        UPDATE: Nrgcp.Header.Type
        NOTIFY: Nrgcp.Header.Type
        DELETE: Nrgcp.Header.Type
        ADD: Nrgcp.Header.Type
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATUS: _ClassVar[Nrgcp.Header.Status]
            ACCEPTED: _ClassVar[Nrgcp.Header.Status]
            REJECTED: _ClassVar[Nrgcp.Header.Status]
        UNKNOWN_STATUS: Nrgcp.Header.Status
        ACCEPTED: Nrgcp.Header.Status
        REJECTED: Nrgcp.Header.Status
        class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SERVICE: _ClassVar[Nrgcp.Header.Service]
            CHARGE_CONTROL: _ClassVar[Nrgcp.Header.Service]
            WIFI: _ClassVar[Nrgcp.Header.Service]
            DEVICE_CONTROL: _ClassVar[Nrgcp.Header.Service]
            NRGDP: _ClassVar[Nrgcp.Header.Service]
            OCPP: _ClassVar[Nrgcp.Header.Service]
            TIMEBASEDCHARGING: _ClassVar[Nrgcp.Header.Service]
            SOLAR_CHARGING: _ClassVar[Nrgcp.Header.Service]
            LICENSE_SERVICE: _ClassVar[Nrgcp.Header.Service]
            STATISTICS: _ClassVar[Nrgcp.Header.Service]
        UNKNOWN_SERVICE: Nrgcp.Header.Service
        CHARGE_CONTROL: Nrgcp.Header.Service
        WIFI: Nrgcp.Header.Service
        DEVICE_CONTROL: Nrgcp.Header.Service
        NRGDP: Nrgcp.Header.Service
        OCPP: Nrgcp.Header.Service
        TIMEBASEDCHARGING: Nrgcp.Header.Service
        SOLAR_CHARGING: Nrgcp.Header.Service
        LICENSE_SERVICE: Nrgcp.Header.Service
        STATISTICS: Nrgcp.Header.Service
        class Property(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PROPERTY: _ClassVar[Nrgcp.Header.Property]
            DYNAMIC_VALUES: _ClassVar[Nrgcp.Header.Property]
            SETTINGS: _ClassVar[Nrgcp.Header.Property]
            INFO: _ClassVar[Nrgcp.Header.Property]
            NAME: _ClassVar[Nrgcp.Header.Property]
            PASSWORD: _ClassVar[Nrgcp.Header.Property]
            CONNECT: _ClassVar[Nrgcp.Header.Property]
            SCAN: _ClassVar[Nrgcp.Header.Property]
            STATUS: _ClassVar[Nrgcp.Header.Property]
            APP_SETTINGS: _ClassVar[Nrgcp.Header.Property]
            DATA: _ClassVar[Nrgcp.Header.Property]
            CHARGE_VALUES: _ClassVar[Nrgcp.Header.Property]
            SELF_TESTS: _ClassVar[Nrgcp.Header.Property]
            CALIBRATION: _ClassVar[Nrgcp.Header.Property]
            INFO_EXTENDED: _ClassVar[Nrgcp.Header.Property]
            TEMPERATURES: _ClassVar[Nrgcp.Header.Property]
            CHARGE_RECORDS: _ClassVar[Nrgcp.Header.Property]
            CONFIGURATION: _ClassVar[Nrgcp.Header.Property]
            ACTIVATION: _ClassVar[Nrgcp.Header.Property]
            TIMEBASEDCHARGING_SETTINGS: _ClassVar[Nrgcp.Header.Property]
            RESET: _ClassVar[Nrgcp.Header.Property]
            CHARGE_RECORD: _ClassVar[Nrgcp.Header.Property]
            STATE: _ClassVar[Nrgcp.Header.Property]
            LOCATION: _ClassVar[Nrgcp.Header.Property]
            SOLARINVERTER_SCAN: _ClassVar[Nrgcp.Header.Property]
            PROFILES: _ClassVar[Nrgcp.Header.Property]
            PROFILE: _ClassVar[Nrgcp.Header.Property]
            DIAGNOSTIC_DATA: _ClassVar[Nrgcp.Header.Property]
            SYSTEM: _ClassVar[Nrgcp.Header.Property]
            ENERGY_METER_SCAN: _ClassVar[Nrgcp.Header.Property]
            LICENSE_SERVICES_TIME_LEFT_H: _ClassVar[Nrgcp.Header.Property]
            DEVICE_PING: _ClassVar[Nrgcp.Header.Property]
            SMART_LOAD_SCAN: _ClassVar[Nrgcp.Header.Property]
            SOLARBATTERY_SCAN: _ClassVar[Nrgcp.Header.Property]
            SOLAR_STATISTICS_DATA: _ClassVar[Nrgcp.Header.Property]
            SOLAR_STATISTICS_INFO: _ClassVar[Nrgcp.Header.Property]
            SOLAR_FULLSCAN: _ClassVar[Nrgcp.Header.Property]
        UNKNOWN_PROPERTY: Nrgcp.Header.Property
        DYNAMIC_VALUES: Nrgcp.Header.Property
        SETTINGS: Nrgcp.Header.Property
        INFO: Nrgcp.Header.Property
        NAME: Nrgcp.Header.Property
        PASSWORD: Nrgcp.Header.Property
        CONNECT: Nrgcp.Header.Property
        SCAN: Nrgcp.Header.Property
        STATUS: Nrgcp.Header.Property
        APP_SETTINGS: Nrgcp.Header.Property
        DATA: Nrgcp.Header.Property
        CHARGE_VALUES: Nrgcp.Header.Property
        SELF_TESTS: Nrgcp.Header.Property
        CALIBRATION: Nrgcp.Header.Property
        INFO_EXTENDED: Nrgcp.Header.Property
        TEMPERATURES: Nrgcp.Header.Property
        CHARGE_RECORDS: Nrgcp.Header.Property
        CONFIGURATION: Nrgcp.Header.Property
        ACTIVATION: Nrgcp.Header.Property
        TIMEBASEDCHARGING_SETTINGS: Nrgcp.Header.Property
        RESET: Nrgcp.Header.Property
        CHARGE_RECORD: Nrgcp.Header.Property
        STATE: Nrgcp.Header.Property
        LOCATION: Nrgcp.Header.Property
        SOLARINVERTER_SCAN: Nrgcp.Header.Property
        PROFILES: Nrgcp.Header.Property
        PROFILE: Nrgcp.Header.Property
        DIAGNOSTIC_DATA: Nrgcp.Header.Property
        SYSTEM: Nrgcp.Header.Property
        ENERGY_METER_SCAN: Nrgcp.Header.Property
        LICENSE_SERVICES_TIME_LEFT_H: Nrgcp.Header.Property
        DEVICE_PING: Nrgcp.Header.Property
        SMART_LOAD_SCAN: Nrgcp.Header.Property
        SOLARBATTERY_SCAN: Nrgcp.Header.Property
        SOLAR_STATISTICS_DATA: Nrgcp.Header.Property
        SOLAR_STATISTICS_INFO: Nrgcp.Header.Property
        SOLAR_FULLSCAN: Nrgcp.Header.Property
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        type: Nrgcp.Header.Type
        status: Nrgcp.Header.Status
        service: Nrgcp.Header.Service
        property: Nrgcp.Header.Property
        uuid: str
        def __init__(self, type: _Optional[_Union[Nrgcp.Header.Type, str]] = ..., status: _Optional[_Union[Nrgcp.Header.Status, str]] = ..., service: _Optional[_Union[Nrgcp.Header.Service, str]] = ..., property: _Optional[_Union[Nrgcp.Header.Property, str]] = ..., uuid: _Optional[str] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("requestId",)
        REQUESTID_FIELD_NUMBER: _ClassVar[int]
        requestId: str
        def __init__(self, requestId: _Optional[str] = ...) -> None: ...
    class Payload(_message.Message):
        __slots__ = ("ERROR", "CHARGECONTROL_CHARGEVALUES_GET", "CHARGECONTROL_SELFTESTS_GET", "CHARGECONTROL_CALIBRATIONVALUES_GET", "CHARGECONTROL_TEMPERATURES_GET", "CHARGECONTROL_CHARGERECORDS_GET", "CHARGECONTROL_DYNAMICVALUES_GET", "CHARGECONTROL_SETTINGS_GET", "CHARGECONTROL_SETTINGS_UPDATE", "DEVICECONTROL_INFOEXTENDED_GET", "DEVICECONTROL_INFO_GET", "DEVICECONTROL_INFO_UPDATE", "WIFI_CONNECT_UPDATE", "WIFI_SCAN_GET", "WIFI_STATUS_GET", "NRGDP_DATA_GET", "DEVICECONTROL_APPSETTINGS_GET", "DEVICECONTROL_APPSETTINGS_UPDATE", "DEVICECONTROL_ACTIVATION_GET", "TIMEBASEDCHARGING_CHARGING_EVENTS_GET", "TIMEBASEDCHARGING_CHARGING_EVENTS_UPDATE", "DEVICECONTROL_RESET_UPDATE", "CHARGECONTROL_CHARGERECORD_GET", "CHARGECONTROL_CHARGERECORD_GET_REQUEST", "TIMEBASEDCHARGING_STATE_GET", "TIMEBASEDCHARGING_STATE_UPDATE", "WIFI_LOCATION_GET", "WIFI_LOCATION_UPDATE", "SOLARCHARGING_SOLARINVERTERSCAN_GET", "SOLARCHARGING_DATA_GET", "SOLARCHARGING_PROFILES_GET", "SOLARCHARGING_PROFILE_UPDATE", "SOLARCHARGING_PROFILE_DELETE", "SOLARCHARGING_STATE_GET", "SOLARCHARGING_STATE_UPDATE", "DEVICECONTROL_DIAGNOSTIC_DATA_GET", "DEVICECONTROL_SYSTEM_UPDATE", "SOLARCHARGING_ENERGYMETERSCAN_GET", "LICENSE_SERVICES_GET", "SOLARCHARGING_DEVICEPING_GET", "SOLARCHARGING_SMARTLOADSCAN_GET", "SOLARCHARGING_BATTERYSCAN_GET", "STATISTICS_SOLARSTATISTICSDATA_GET", "STATISTICS_SOLARSTATISTICSINFO_GET", "SOLARCHARGING_FULLSCAN_GET")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_CHARGEVALUES_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_SELFTESTS_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_CALIBRATIONVALUES_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_TEMPERATURES_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_CHARGERECORDS_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_DYNAMICVALUES_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_SETTINGS_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_SETTINGS_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_INFOEXTENDED_GET_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_INFO_GET_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_INFO_UPDATE_FIELD_NUMBER: _ClassVar[int]
        WIFI_CONNECT_UPDATE_FIELD_NUMBER: _ClassVar[int]
        WIFI_SCAN_GET_FIELD_NUMBER: _ClassVar[int]
        WIFI_STATUS_GET_FIELD_NUMBER: _ClassVar[int]
        NRGDP_DATA_GET_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_APPSETTINGS_GET_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_APPSETTINGS_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_ACTIVATION_GET_FIELD_NUMBER: _ClassVar[int]
        TIMEBASEDCHARGING_CHARGING_EVENTS_GET_FIELD_NUMBER: _ClassVar[int]
        TIMEBASEDCHARGING_CHARGING_EVENTS_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_RESET_UPDATE_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_CHARGERECORD_GET_FIELD_NUMBER: _ClassVar[int]
        CHARGECONTROL_CHARGERECORD_GET_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TIMEBASEDCHARGING_STATE_GET_FIELD_NUMBER: _ClassVar[int]
        TIMEBASEDCHARGING_STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        WIFI_LOCATION_GET_FIELD_NUMBER: _ClassVar[int]
        WIFI_LOCATION_UPDATE_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_SOLARINVERTERSCAN_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_DATA_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_PROFILES_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_PROFILE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_PROFILE_DELETE_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_STATE_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_DIAGNOSTIC_DATA_GET_FIELD_NUMBER: _ClassVar[int]
        DEVICECONTROL_SYSTEM_UPDATE_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_ENERGYMETERSCAN_GET_FIELD_NUMBER: _ClassVar[int]
        LICENSE_SERVICES_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_DEVICEPING_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_SMARTLOADSCAN_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_BATTERYSCAN_GET_FIELD_NUMBER: _ClassVar[int]
        STATISTICS_SOLARSTATISTICSDATA_GET_FIELD_NUMBER: _ClassVar[int]
        STATISTICS_SOLARSTATISTICSINFO_GET_FIELD_NUMBER: _ClassVar[int]
        SOLARCHARGING_FULLSCAN_GET_FIELD_NUMBER: _ClassVar[int]
        ERROR: NrgcpRequestRejectedPayload
        CHARGECONTROL_CHARGEVALUES_GET: NrgcpChargecontrolChargevaluesGetPayload
        CHARGECONTROL_SELFTESTS_GET: NrgcpChargecontrolSelftestsGetPayload
        CHARGECONTROL_CALIBRATIONVALUES_GET: NrgcpChargecontrolCalibrationvaluesGetPayload
        CHARGECONTROL_TEMPERATURES_GET: NrgcpChargecontrolTemperaturesGetPayload
        CHARGECONTROL_CHARGERECORDS_GET: NrgcpChargecontrolChargerecordsGetPayload
        CHARGECONTROL_DYNAMICVALUES_GET: NrgcpChargecontrolDynamicvaluesGetPayload
        CHARGECONTROL_SETTINGS_GET: NrgcpChargecontrolSettingsGetPayload
        CHARGECONTROL_SETTINGS_UPDATE: NrgcpChargecontrolSettingsUpdatePayload
        DEVICECONTROL_INFOEXTENDED_GET: NrgcpDevicecontrolInfoextendedGetPayload
        DEVICECONTROL_INFO_GET: NrgcpDevicecontrolInfoGetPayload
        DEVICECONTROL_INFO_UPDATE: NrgcpDevicecontrolInfoUpdatePayload
        WIFI_CONNECT_UPDATE: NrgcpWifiConnectUpdatePayload
        WIFI_SCAN_GET: NrgcpWifiScanGetPayload
        WIFI_STATUS_GET: NrgcpWifiStatusGetPayload
        NRGDP_DATA_GET: NrgcpNrgdpDataGetPayload
        DEVICECONTROL_APPSETTINGS_GET: NrgcpDevicecontrolAppsettingsGetPayload
        DEVICECONTROL_APPSETTINGS_UPDATE: NrgcpDevicecontrolAppsettingsUpdatePayload
        DEVICECONTROL_ACTIVATION_GET: NrgcpDevicecontrolActivationGetPayload
        TIMEBASEDCHARGING_CHARGING_EVENTS_GET: NrgcpTimebasedchargingChargingEventsGetPayload
        TIMEBASEDCHARGING_CHARGING_EVENTS_UPDATE: NrgcpTimebasedchargingChargingEventsUpdatePayload
        DEVICECONTROL_RESET_UPDATE: NrgcpDevicecontrolResetUpdatePayload
        CHARGECONTROL_CHARGERECORD_GET: NrgcpChargecontrolChargerecordGetPayload
        CHARGECONTROL_CHARGERECORD_GET_REQUEST: NrgcpChargecontrolChargerecordGetPayloadRequest
        TIMEBASEDCHARGING_STATE_GET: NrgcpTimebasedchargingStateGetPayload
        TIMEBASEDCHARGING_STATE_UPDATE: NrgcpTimebasedchargingStateUpdatePayload
        WIFI_LOCATION_GET: NrgcpWifiLocationGetPayload
        WIFI_LOCATION_UPDATE: NrgcpWifiLocationUpdatePayload
        SOLARCHARGING_SOLARINVERTERSCAN_GET: NrgcpSolarchargingSolarinverterscanGetPayload
        SOLARCHARGING_DATA_GET: NrgcpSolarchargingDataGetPayload
        SOLARCHARGING_PROFILES_GET: NrgcpSolarchargingProfilesGetPayload
        SOLARCHARGING_PROFILE_UPDATE: NrgcpSolarchargingProfileUpdatePayload
        SOLARCHARGING_PROFILE_DELETE: NrgcpSolarchargingProfileDeletePayload
        SOLARCHARGING_STATE_GET: NrgcpSolarchargingStateGetPayload
        SOLARCHARGING_STATE_UPDATE: NrgcpSolarchargingStateUpdatePayload
        DEVICECONTROL_DIAGNOSTIC_DATA_GET: NrgcpDevicecontrolDiagnosticdataGetPayload
        DEVICECONTROL_SYSTEM_UPDATE: NrgcpDevicecontrolSystemUpdatePayload
        SOLARCHARGING_ENERGYMETERSCAN_GET: NrgcpSolarchargingEnergymeterscanGetPayload
        LICENSE_SERVICES_GET: NrgcpLicenseServicesGetPayload
        SOLARCHARGING_DEVICEPING_GET: NrgcpSolarchargingDevicepingGetPayload
        SOLARCHARGING_SMARTLOADSCAN_GET: NrgcpSolarchargingSmartloadscanGetPayload
        SOLARCHARGING_BATTERYSCAN_GET: NrgcpSolarchargingBatteryscanGetPayload
        STATISTICS_SOLARSTATISTICSDATA_GET: NrgcpStatisticsSolarstatisticsdataGetPayload
        STATISTICS_SOLARSTATISTICSINFO_GET: NrgcpStatisticsSolarstatisticsinfoGetPayload
        SOLARCHARGING_FULLSCAN_GET: NrgcpSolarchargingFullscanGetPayload
        def __init__(self, ERROR: _Optional[_Union[NrgcpRequestRejectedPayload, _Mapping]] = ..., CHARGECONTROL_CHARGEVALUES_GET: _Optional[_Union[NrgcpChargecontrolChargevaluesGetPayload, _Mapping]] = ..., CHARGECONTROL_SELFTESTS_GET: _Optional[_Union[NrgcpChargecontrolSelftestsGetPayload, _Mapping]] = ..., CHARGECONTROL_CALIBRATIONVALUES_GET: _Optional[_Union[NrgcpChargecontrolCalibrationvaluesGetPayload, _Mapping]] = ..., CHARGECONTROL_TEMPERATURES_GET: _Optional[_Union[NrgcpChargecontrolTemperaturesGetPayload, _Mapping]] = ..., CHARGECONTROL_CHARGERECORDS_GET: _Optional[_Union[NrgcpChargecontrolChargerecordsGetPayload, _Mapping]] = ..., CHARGECONTROL_DYNAMICVALUES_GET: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload, _Mapping]] = ..., CHARGECONTROL_SETTINGS_GET: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload, _Mapping]] = ..., CHARGECONTROL_SETTINGS_UPDATE: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload, _Mapping]] = ..., DEVICECONTROL_INFOEXTENDED_GET: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload, _Mapping]] = ..., DEVICECONTROL_INFO_GET: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload, _Mapping]] = ..., DEVICECONTROL_INFO_UPDATE: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload, _Mapping]] = ..., WIFI_CONNECT_UPDATE: _Optional[_Union[NrgcpWifiConnectUpdatePayload, _Mapping]] = ..., WIFI_SCAN_GET: _Optional[_Union[NrgcpWifiScanGetPayload, _Mapping]] = ..., WIFI_STATUS_GET: _Optional[_Union[NrgcpWifiStatusGetPayload, _Mapping]] = ..., NRGDP_DATA_GET: _Optional[_Union[NrgcpNrgdpDataGetPayload, _Mapping]] = ..., DEVICECONTROL_APPSETTINGS_GET: _Optional[_Union[NrgcpDevicecontrolAppsettingsGetPayload, _Mapping]] = ..., DEVICECONTROL_APPSETTINGS_UPDATE: _Optional[_Union[NrgcpDevicecontrolAppsettingsUpdatePayload, _Mapping]] = ..., DEVICECONTROL_ACTIVATION_GET: _Optional[_Union[NrgcpDevicecontrolActivationGetPayload, _Mapping]] = ..., TIMEBASEDCHARGING_CHARGING_EVENTS_GET: _Optional[_Union[NrgcpTimebasedchargingChargingEventsGetPayload, _Mapping]] = ..., TIMEBASEDCHARGING_CHARGING_EVENTS_UPDATE: _Optional[_Union[NrgcpTimebasedchargingChargingEventsUpdatePayload, _Mapping]] = ..., DEVICECONTROL_RESET_UPDATE: _Optional[_Union[NrgcpDevicecontrolResetUpdatePayload, _Mapping]] = ..., CHARGECONTROL_CHARGERECORD_GET: _Optional[_Union[NrgcpChargecontrolChargerecordGetPayload, _Mapping]] = ..., CHARGECONTROL_CHARGERECORD_GET_REQUEST: _Optional[_Union[NrgcpChargecontrolChargerecordGetPayloadRequest, _Mapping]] = ..., TIMEBASEDCHARGING_STATE_GET: _Optional[_Union[NrgcpTimebasedchargingStateGetPayload, _Mapping]] = ..., TIMEBASEDCHARGING_STATE_UPDATE: _Optional[_Union[NrgcpTimebasedchargingStateUpdatePayload, _Mapping]] = ..., WIFI_LOCATION_GET: _Optional[_Union[NrgcpWifiLocationGetPayload, _Mapping]] = ..., WIFI_LOCATION_UPDATE: _Optional[_Union[NrgcpWifiLocationUpdatePayload, _Mapping]] = ..., SOLARCHARGING_SOLARINVERTERSCAN_GET: _Optional[_Union[NrgcpSolarchargingSolarinverterscanGetPayload, _Mapping]] = ..., SOLARCHARGING_DATA_GET: _Optional[_Union[NrgcpSolarchargingDataGetPayload, _Mapping]] = ..., SOLARCHARGING_PROFILES_GET: _Optional[_Union[NrgcpSolarchargingProfilesGetPayload, _Mapping]] = ..., SOLARCHARGING_PROFILE_UPDATE: _Optional[_Union[NrgcpSolarchargingProfileUpdatePayload, _Mapping]] = ..., SOLARCHARGING_PROFILE_DELETE: _Optional[_Union[NrgcpSolarchargingProfileDeletePayload, _Mapping]] = ..., SOLARCHARGING_STATE_GET: _Optional[_Union[NrgcpSolarchargingStateGetPayload, _Mapping]] = ..., SOLARCHARGING_STATE_UPDATE: _Optional[_Union[NrgcpSolarchargingStateUpdatePayload, _Mapping]] = ..., DEVICECONTROL_DIAGNOSTIC_DATA_GET: _Optional[_Union[NrgcpDevicecontrolDiagnosticdataGetPayload, _Mapping]] = ..., DEVICECONTROL_SYSTEM_UPDATE: _Optional[_Union[NrgcpDevicecontrolSystemUpdatePayload, _Mapping]] = ..., SOLARCHARGING_ENERGYMETERSCAN_GET: _Optional[_Union[NrgcpSolarchargingEnergymeterscanGetPayload, _Mapping]] = ..., LICENSE_SERVICES_GET: _Optional[_Union[NrgcpLicenseServicesGetPayload, _Mapping]] = ..., SOLARCHARGING_DEVICEPING_GET: _Optional[_Union[NrgcpSolarchargingDevicepingGetPayload, _Mapping]] = ..., SOLARCHARGING_SMARTLOADSCAN_GET: _Optional[_Union[NrgcpSolarchargingSmartloadscanGetPayload, _Mapping]] = ..., SOLARCHARGING_BATTERYSCAN_GET: _Optional[_Union[NrgcpSolarchargingBatteryscanGetPayload, _Mapping]] = ..., STATISTICS_SOLARSTATISTICSDATA_GET: _Optional[_Union[NrgcpStatisticsSolarstatisticsdataGetPayload, _Mapping]] = ..., STATISTICS_SOLARSTATISTICSINFO_GET: _Optional[_Union[NrgcpStatisticsSolarstatisticsinfoGetPayload, _Mapping]] = ..., SOLARCHARGING_FULLSCAN_GET: _Optional[_Union[NrgcpSolarchargingFullscanGetPayload, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    header: Nrgcp.Header
    metadata: Nrgcp.Metadata
    payload: Nrgcp.Payload
    def __init__(self, header: _Optional[_Union[Nrgcp.Header, _Mapping]] = ..., metadata: _Optional[_Union[Nrgcp.Metadata, _Mapping]] = ..., payload: _Optional[_Union[Nrgcp.Payload, _Mapping]] = ...) -> None: ...

class NrgcpRequestRejectedPayload(_message.Message):
    __slots__ = ("code", "name")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: int
    name: str
    def __init__(self, code: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class NrgcpChargecontrolChargevaluesGetPayload(_message.Message):
    __slots__ = ("phaseA", "phaseB", "phaseC", "phaseTotal", "pMeanTMax", "gridFrequency", "iRmsN", "evDiode", "ifidc", "chargedEnergy", "ifiac")
    class Phase(_message.Message):
        __slots__ = ("aPEnergy", "iRms", "pFMean", "pMeanF", "pMean", "qMean", "sMean", "uRms")
        APENERGY_FIELD_NUMBER: _ClassVar[int]
        IRMS_FIELD_NUMBER: _ClassVar[int]
        PFMEAN_FIELD_NUMBER: _ClassVar[int]
        PMEANF_FIELD_NUMBER: _ClassVar[int]
        PMEAN_FIELD_NUMBER: _ClassVar[int]
        QMEAN_FIELD_NUMBER: _ClassVar[int]
        SMEAN_FIELD_NUMBER: _ClassVar[int]
        URMS_FIELD_NUMBER: _ClassVar[int]
        aPEnergy: float
        iRms: float
        pFMean: float
        pMeanF: float
        pMean: float
        qMean: float
        sMean: float
        uRms: float
        def __init__(self, aPEnergy: _Optional[float] = ..., iRms: _Optional[float] = ..., pFMean: _Optional[float] = ..., pMeanF: _Optional[float] = ..., pMean: _Optional[float] = ..., qMean: _Optional[float] = ..., sMean: _Optional[float] = ..., uRms: _Optional[float] = ...) -> None: ...
    PHASEA_FIELD_NUMBER: _ClassVar[int]
    PHASEB_FIELD_NUMBER: _ClassVar[int]
    PHASEC_FIELD_NUMBER: _ClassVar[int]
    PHASETOTAL_FIELD_NUMBER: _ClassVar[int]
    PMEANTMAX_FIELD_NUMBER: _ClassVar[int]
    GRIDFREQUENCY_FIELD_NUMBER: _ClassVar[int]
    IRMSN_FIELD_NUMBER: _ClassVar[int]
    EVDIODE_FIELD_NUMBER: _ClassVar[int]
    IFIDC_FIELD_NUMBER: _ClassVar[int]
    CHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
    IFIAC_FIELD_NUMBER: _ClassVar[int]
    phaseA: NrgcpChargecontrolChargevaluesGetPayload.Phase
    phaseB: NrgcpChargecontrolChargevaluesGetPayload.Phase
    phaseC: NrgcpChargecontrolChargevaluesGetPayload.Phase
    phaseTotal: NrgcpChargecontrolChargevaluesGetPayload.Phase
    pMeanTMax: float
    gridFrequency: float
    iRmsN: float
    evDiode: bool
    ifidc: int
    chargedEnergy: float
    ifiac: int
    def __init__(self, phaseA: _Optional[_Union[NrgcpChargecontrolChargevaluesGetPayload.Phase, _Mapping]] = ..., phaseB: _Optional[_Union[NrgcpChargecontrolChargevaluesGetPayload.Phase, _Mapping]] = ..., phaseC: _Optional[_Union[NrgcpChargecontrolChargevaluesGetPayload.Phase, _Mapping]] = ..., phaseTotal: _Optional[_Union[NrgcpChargecontrolChargevaluesGetPayload.Phase, _Mapping]] = ..., pMeanTMax: _Optional[float] = ..., gridFrequency: _Optional[float] = ..., iRmsN: _Optional[float] = ..., evDiode: bool = ..., ifidc: _Optional[int] = ..., chargedEnergy: _Optional[float] = ..., ifiac: _Optional[int] = ...) -> None: ...

class NrgcpChargecontrolSelftestsGetPayload(_message.Message):
    __slots__ = ("fi", "peR", "pe", "relaisWeld", "relayState")
    FI_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    PE_FIELD_NUMBER: _ClassVar[int]
    RELAISWELD_FIELD_NUMBER: _ClassVar[int]
    RELAYSTATE_FIELD_NUMBER: _ClassVar[int]
    fi: bool
    peR: int
    pe: bool
    relaisWeld: bool
    relayState: int
    def __init__(self, fi: bool = ..., peR: _Optional[int] = ..., pe: bool = ..., relaisWeld: bool = ..., relayState: _Optional[int] = ...) -> None: ...

class NrgcpChargecontrolCalibrationvaluesGetPayload(_message.Message):
    __slots__ = ("uCalibrateGainA", "uCalibrateGainB", "uCalibrateGainC", "uCalibrateOffsetA", "uCalibrateOffsetB", "uCalibrateOffsetC")
    UCALIBRATEGAINA_FIELD_NUMBER: _ClassVar[int]
    UCALIBRATEGAINB_FIELD_NUMBER: _ClassVar[int]
    UCALIBRATEGAINC_FIELD_NUMBER: _ClassVar[int]
    UCALIBRATEOFFSETA_FIELD_NUMBER: _ClassVar[int]
    UCALIBRATEOFFSETB_FIELD_NUMBER: _ClassVar[int]
    UCALIBRATEOFFSETC_FIELD_NUMBER: _ClassVar[int]
    uCalibrateGainA: int
    uCalibrateGainB: int
    uCalibrateGainC: int
    uCalibrateOffsetA: int
    uCalibrateOffsetB: int
    uCalibrateOffsetC: int
    def __init__(self, uCalibrateGainA: _Optional[int] = ..., uCalibrateGainB: _Optional[int] = ..., uCalibrateGainC: _Optional[int] = ..., uCalibrateOffsetA: _Optional[int] = ..., uCalibrateOffsetB: _Optional[int] = ..., uCalibrateOffsetC: _Optional[int] = ...) -> None: ...

class NrgcpChargecontrolTemperaturesGetPayload(_message.Message):
    __slots__ = ("tempMainEm", "tempMainPcb", "tempMainPic", "tempSchuko1", "tempSchuko2", "tempSchuko3", "tempStarPic", "tempStarSens1", "tempStarSens2", "tempStarSens3")
    TEMPMAINEM_FIELD_NUMBER: _ClassVar[int]
    TEMPMAINPCB_FIELD_NUMBER: _ClassVar[int]
    TEMPMAINPIC_FIELD_NUMBER: _ClassVar[int]
    TEMPSCHUKO1_FIELD_NUMBER: _ClassVar[int]
    TEMPSCHUKO2_FIELD_NUMBER: _ClassVar[int]
    TEMPSCHUKO3_FIELD_NUMBER: _ClassVar[int]
    TEMPSTARPIC_FIELD_NUMBER: _ClassVar[int]
    TEMPSTARSENS1_FIELD_NUMBER: _ClassVar[int]
    TEMPSTARSENS2_FIELD_NUMBER: _ClassVar[int]
    TEMPSTARSENS3_FIELD_NUMBER: _ClassVar[int]
    tempMainEm: float
    tempMainPcb: float
    tempMainPic: float
    tempSchuko1: float
    tempSchuko2: float
    tempSchuko3: float
    tempStarPic: float
    tempStarSens1: float
    tempStarSens2: float
    tempStarSens3: float
    def __init__(self, tempMainEm: _Optional[float] = ..., tempMainPcb: _Optional[float] = ..., tempMainPic: _Optional[float] = ..., tempSchuko1: _Optional[float] = ..., tempSchuko2: _Optional[float] = ..., tempSchuko3: _Optional[float] = ..., tempStarPic: _Optional[float] = ..., tempStarSens1: _Optional[float] = ..., tempStarSens2: _Optional[float] = ..., tempStarSens3: _Optional[float] = ...) -> None: ...

class NrgcpChargecontrolChargerecordsGetPayload(_message.Message):
    __slots__ = ("totalChargedEnergyOverall",)
    TOTALCHARGEDENERGYOVERALL_FIELD_NUMBER: _ClassVar[int]
    totalChargedEnergyOverall: float
    def __init__(self, totalChargedEnergyOverall: _Optional[float] = ...) -> None: ...

class NrgcpChargecontrolDynamicvaluesGetPayload(_message.Message):
    __slots__ = ("chargingData", "temperatures")
    class ChargingData(_message.Message):
        __slots__ = ("chargedEnergy", "chargingPower", "chargingRate", "chargingVoltage", "costs", "gridFrequency", "nCurrent", "peakPower", "phaseA", "phaseB", "phaseC", "remainKm", "totalChargedEnergy")
        class Phase(_message.Message):
            __slots__ = ("current", "power", "voltage")
            CURRENT_FIELD_NUMBER: _ClassVar[int]
            POWER_FIELD_NUMBER: _ClassVar[int]
            VOLTAGE_FIELD_NUMBER: _ClassVar[int]
            current: float
            power: float
            voltage: float
            def __init__(self, current: _Optional[float] = ..., power: _Optional[float] = ..., voltage: _Optional[float] = ...) -> None: ...
        CHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
        CHARGINGPOWER_FIELD_NUMBER: _ClassVar[int]
        CHARGINGRATE_FIELD_NUMBER: _ClassVar[int]
        CHARGINGVOLTAGE_FIELD_NUMBER: _ClassVar[int]
        COSTS_FIELD_NUMBER: _ClassVar[int]
        GRIDFREQUENCY_FIELD_NUMBER: _ClassVar[int]
        NCURRENT_FIELD_NUMBER: _ClassVar[int]
        PEAKPOWER_FIELD_NUMBER: _ClassVar[int]
        PHASEA_FIELD_NUMBER: _ClassVar[int]
        PHASEB_FIELD_NUMBER: _ClassVar[int]
        PHASEC_FIELD_NUMBER: _ClassVar[int]
        REMAINKM_FIELD_NUMBER: _ClassVar[int]
        TOTALCHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
        chargedEnergy: float
        chargingPower: float
        chargingRate: float
        chargingVoltage: float
        costs: float
        gridFrequency: float
        nCurrent: float
        peakPower: float
        phaseA: NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase
        phaseB: NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase
        phaseC: NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase
        remainKm: float
        totalChargedEnergy: float
        def __init__(self, chargedEnergy: _Optional[float] = ..., chargingPower: _Optional[float] = ..., chargingRate: _Optional[float] = ..., chargingVoltage: _Optional[float] = ..., costs: _Optional[float] = ..., gridFrequency: _Optional[float] = ..., nCurrent: _Optional[float] = ..., peakPower: _Optional[float] = ..., phaseA: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase, _Mapping]] = ..., phaseB: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase, _Mapping]] = ..., phaseC: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData.Phase, _Mapping]] = ..., remainKm: _Optional[float] = ..., totalChargedEnergy: _Optional[float] = ...) -> None: ...
    class Temperatures(_message.Message):
        __slots__ = ("main1", "smart1", "star1", "touch1")
        MAIN1_FIELD_NUMBER: _ClassVar[int]
        SMART1_FIELD_NUMBER: _ClassVar[int]
        STAR1_FIELD_NUMBER: _ClassVar[int]
        TOUCH1_FIELD_NUMBER: _ClassVar[int]
        main1: float
        smart1: float
        star1: float
        touch1: float
        def __init__(self, main1: _Optional[float] = ..., smart1: _Optional[float] = ..., star1: _Optional[float] = ..., touch1: _Optional[float] = ...) -> None: ...
    CHARGINGDATA_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURES_FIELD_NUMBER: _ClassVar[int]
    chargingData: NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData
    temperatures: NrgcpChargecontrolDynamicvaluesGetPayload.Temperatures
    def __init__(self, chargingData: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload.ChargingData, _Mapping]] = ..., temperatures: _Optional[_Union[NrgcpChargecontrolDynamicvaluesGetPayload.Temperatures, _Mapping]] = ...) -> None: ...

class NrgcpChargecontrolSettingsGetPayload(_message.Message):
    __slots__ = ("chargeCurrent", "chargingCycle", "chargingState", "cpPwmActive", "cpStatus", "energyLimit", "errorCode", "latestRecordNumber", "phaseSwitch", "warningCode")
    class ChargeCurrent(_message.Message):
        __slots__ = ("maxAdapter", "max", "min", "type2Current", "userSet", "value")
        MAXADAPTER_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        TYPE2CURRENT_FIELD_NUMBER: _ClassVar[int]
        USERSET_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        maxAdapter: float
        max: int
        min: int
        type2Current: float
        userSet: float
        value: int
        def __init__(self, maxAdapter: _Optional[float] = ..., max: _Optional[int] = ..., min: _Optional[int] = ..., type2Current: _Optional[float] = ..., userSet: _Optional[float] = ..., value: _Optional[int] = ...) -> None: ...
    class ChargingState(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: NrgcpTypes.ChargingState
        def __init__(self, value: _Optional[_Union[NrgcpTypes.ChargingState, str]] = ...) -> None: ...
    class EnergyLimit(_message.Message):
        __slots__ = ("limited", "max", "min", "value")
        LIMITED_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        limited: NrgcpTypes.EnergyLimitMode
        max: float
        min: float
        value: float
        def __init__(self, limited: _Optional[_Union[NrgcpTypes.EnergyLimitMode, str]] = ..., max: _Optional[float] = ..., min: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    class PhaseSwitch(_message.Message):
        __slots__ = ("selection",)
        class PhaseSwitchSelection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNKNOWN: _ClassVar[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection]
            STATE_1PHASE: _ClassVar[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection]
            STATE_2PHASE: _ClassVar[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection]
            STATE_3PHASE: _ClassVar[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection]
        STATE_UNKNOWN: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection
        STATE_1PHASE: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection
        STATE_2PHASE: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection
        STATE_3PHASE: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection
        SELECTION_FIELD_NUMBER: _ClassVar[int]
        selection: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection
        def __init__(self, selection: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch.PhaseSwitchSelection, str]] = ...) -> None: ...
    CHARGECURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGINGCYCLE_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    CPPWMACTIVE_FIELD_NUMBER: _ClassVar[int]
    CPSTATUS_FIELD_NUMBER: _ClassVar[int]
    ENERGYLIMIT_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    LATESTRECORDNUMBER_FIELD_NUMBER: _ClassVar[int]
    PHASESWITCH_FIELD_NUMBER: _ClassVar[int]
    WARNINGCODE_FIELD_NUMBER: _ClassVar[int]
    chargeCurrent: NrgcpChargecontrolSettingsGetPayload.ChargeCurrent
    chargingCycle: int
    chargingState: NrgcpChargecontrolSettingsGetPayload.ChargingState
    cpPwmActive: bool
    cpStatus: NrgcpTypes.CpStatus
    energyLimit: NrgcpChargecontrolSettingsGetPayload.EnergyLimit
    errorCode: int
    latestRecordNumber: int
    phaseSwitch: NrgcpChargecontrolSettingsGetPayload.PhaseSwitch
    warningCode: int
    def __init__(self, chargeCurrent: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload.ChargeCurrent, _Mapping]] = ..., chargingCycle: _Optional[int] = ..., chargingState: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload.ChargingState, _Mapping]] = ..., cpPwmActive: bool = ..., cpStatus: _Optional[_Union[NrgcpTypes.CpStatus, str]] = ..., energyLimit: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload.EnergyLimit, _Mapping]] = ..., errorCode: _Optional[int] = ..., latestRecordNumber: _Optional[int] = ..., phaseSwitch: _Optional[_Union[NrgcpChargecontrolSettingsGetPayload.PhaseSwitch, _Mapping]] = ..., warningCode: _Optional[int] = ...) -> None: ...

class NrgcpChargecontrolSettingsUpdatePayload(_message.Message):
    __slots__ = ("chargeCurrent", "chargingState", "energyLimit", "phaseSwitch")
    class ChargeCurrent(_message.Message):
        __slots__ = ("userSet", "value")
        USERSET_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        userSet: float
        value: int
        def __init__(self, userSet: _Optional[float] = ..., value: _Optional[int] = ...) -> None: ...
    class ChargingState(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: NrgcpTypes.ChargingState
        def __init__(self, value: _Optional[_Union[NrgcpTypes.ChargingState, str]] = ...) -> None: ...
    class EnergyLimit(_message.Message):
        __slots__ = ("limited", "value")
        LIMITED_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        limited: NrgcpTypes.EnergyLimitMode
        value: float
        def __init__(self, limited: _Optional[_Union[NrgcpTypes.EnergyLimitMode, str]] = ..., value: _Optional[float] = ...) -> None: ...
    class PhaseSwitch(_message.Message):
        __slots__ = ("selection",)
        class PhaseSelection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNKNOWN: _ClassVar[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection]
            STATE_1PHASE: _ClassVar[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection]
            STATE_2PHASE: _ClassVar[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection]
            STATE_3PHASE: _ClassVar[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection]
        STATE_UNKNOWN: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection
        STATE_1PHASE: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection
        STATE_2PHASE: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection
        STATE_3PHASE: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection
        SELECTION_FIELD_NUMBER: _ClassVar[int]
        selection: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection
        def __init__(self, selection: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch.PhaseSelection, str]] = ...) -> None: ...
    CHARGECURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    ENERGYLIMIT_FIELD_NUMBER: _ClassVar[int]
    PHASESWITCH_FIELD_NUMBER: _ClassVar[int]
    chargeCurrent: NrgcpChargecontrolSettingsUpdatePayload.ChargeCurrent
    chargingState: NrgcpChargecontrolSettingsUpdatePayload.ChargingState
    energyLimit: NrgcpChargecontrolSettingsUpdatePayload.EnergyLimit
    phaseSwitch: NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch
    def __init__(self, chargeCurrent: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload.ChargeCurrent, _Mapping]] = ..., chargingState: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload.ChargingState, _Mapping]] = ..., energyLimit: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload.EnergyLimit, _Mapping]] = ..., phaseSwitch: _Optional[_Union[NrgcpChargecontrolSettingsUpdatePayload.PhaseSwitch, _Mapping]] = ...) -> None: ...

class NrgcpDevicecontrolInfoextendedGetPayload(_message.Message):
    __slots__ = ("adapter", "ipAddress", "macAddress", "mainController", "smCurRstReason", "smRstDeepsleeps", "smRstPanics", "smRstUnknown", "smRstWatchdogs", "smUptime", "star", "touch")
    class Adapter(_message.Message):
        __slots__ = ("chargedEnergy", "connectionCycle", "countryCode", "maxCurrent", "phases", "serial", "tagPcbType", "type2")
        class Type2(_message.Message):
            __slots__ = ("chargingCurrent", "dutycycle", "frequency", "states", "version")
            CHARGINGCURRENT_FIELD_NUMBER: _ClassVar[int]
            DUTYCYCLE_FIELD_NUMBER: _ClassVar[int]
            FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            STATES_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            chargingCurrent: float
            dutycycle: float
            frequency: float
            states: int
            version: int
            def __init__(self, chargingCurrent: _Optional[float] = ..., dutycycle: _Optional[float] = ..., frequency: _Optional[float] = ..., states: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
        CHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
        CONNECTIONCYCLE_FIELD_NUMBER: _ClassVar[int]
        COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
        MAXCURRENT_FIELD_NUMBER: _ClassVar[int]
        PHASES_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        TAGPCBTYPE_FIELD_NUMBER: _ClassVar[int]
        TYPE2_FIELD_NUMBER: _ClassVar[int]
        chargedEnergy: int
        connectionCycle: int
        countryCode: int
        maxCurrent: float
        phases: int
        serial: bytes
        tagPcbType: int
        type2: NrgcpDevicecontrolInfoextendedGetPayload.Adapter.Type2
        def __init__(self, chargedEnergy: _Optional[int] = ..., connectionCycle: _Optional[int] = ..., countryCode: _Optional[int] = ..., maxCurrent: _Optional[float] = ..., phases: _Optional[int] = ..., serial: _Optional[bytes] = ..., tagPcbType: _Optional[int] = ..., type2: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload.Adapter.Type2, _Mapping]] = ...) -> None: ...
    class MainController(_message.Message):
        __slots__ = ("hardwareVersion", "softwareVersion")
        HARDWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        hardwareVersion: str
        softwareVersion: str
        def __init__(self, hardwareVersion: _Optional[str] = ..., softwareVersion: _Optional[str] = ...) -> None: ...
    class Star(_message.Message):
        __slots__ = ("hardwareVersion", "softwareVersion")
        HARDWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        hardwareVersion: str
        softwareVersion: str
        def __init__(self, hardwareVersion: _Optional[str] = ..., softwareVersion: _Optional[str] = ...) -> None: ...
    class Touch(_message.Message):
        __slots__ = ("hardwareVersion", "softwareVersion")
        HARDWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        hardwareVersion: str
        softwareVersion: str
        def __init__(self, hardwareVersion: _Optional[str] = ..., softwareVersion: _Optional[str] = ...) -> None: ...
    ADAPTER_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAINCONTROLLER_FIELD_NUMBER: _ClassVar[int]
    SMCURRSTREASON_FIELD_NUMBER: _ClassVar[int]
    SMRSTDEEPSLEEPS_FIELD_NUMBER: _ClassVar[int]
    SMRSTPANICS_FIELD_NUMBER: _ClassVar[int]
    SMRSTUNKNOWN_FIELD_NUMBER: _ClassVar[int]
    SMRSTWATCHDOGS_FIELD_NUMBER: _ClassVar[int]
    SMUPTIME_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    TOUCH_FIELD_NUMBER: _ClassVar[int]
    adapter: NrgcpDevicecontrolInfoextendedGetPayload.Adapter
    ipAddress: str
    macAddress: str
    mainController: NrgcpDevicecontrolInfoextendedGetPayload.MainController
    smCurRstReason: int
    smRstDeepsleeps: int
    smRstPanics: int
    smRstUnknown: int
    smRstWatchdogs: int
    smUptime: int
    star: NrgcpDevicecontrolInfoextendedGetPayload.Star
    touch: NrgcpDevicecontrolInfoextendedGetPayload.Touch
    def __init__(self, adapter: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload.Adapter, _Mapping]] = ..., ipAddress: _Optional[str] = ..., macAddress: _Optional[str] = ..., mainController: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload.MainController, _Mapping]] = ..., smCurRstReason: _Optional[int] = ..., smRstDeepsleeps: _Optional[int] = ..., smRstPanics: _Optional[int] = ..., smRstUnknown: _Optional[int] = ..., smRstWatchdogs: _Optional[int] = ..., smUptime: _Optional[int] = ..., star: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload.Star, _Mapping]] = ..., touch: _Optional[_Union[NrgcpDevicecontrolInfoextendedGetPayload.Touch, _Mapping]] = ...) -> None: ...

class NrgcpDevicecontrolInfoGetPayload(_message.Message):
    __slots__ = ("cellular", "cellularMode", "chargeRecordsItemStorage", "chargeRecordsUnsynced", "configState", "connectionInterface", "deviceName", "devicePassword", "devicePin", "gps", "hardwareRevision", "initialSetup", "phaseSwitch", "productType", "serialNumber", "softwareVersion", "statisticVersion", "utcTimestamp", "verificationCode")
    class ConfigMode(_message.Message):
        __slots__ = ("state",)
        class ConfigModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_CONFIG_UNKNOWN: _ClassVar[NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState]
            STATE_CONFIG_DISABLED: _ClassVar[NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState]
            STATE_CONFIG_ENABLED: _ClassVar[NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState]
        STATE_CONFIG_UNKNOWN: NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState
        STATE_CONFIG_DISABLED: NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState
        STATE_CONFIG_ENABLED: NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState
        def __init__(self, state: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.ConfigMode.ConfigModeState, str]] = ...) -> None: ...
    class DeviceName(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: int
        min: int
        value: str
        def __init__(self, max: _Optional[int] = ..., min: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class DevicePassword(_message.Message):
        __slots__ = ("max", "min")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        max: int
        min: int
        def __init__(self, max: _Optional[int] = ..., min: _Optional[int] = ...) -> None: ...
    class DevicePin(_message.Message):
        __slots__ = ("max", "min")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        max: int
        min: int
        def __init__(self, max: _Optional[int] = ..., min: _Optional[int] = ...) -> None: ...
    class PhaseSwitch(_message.Message):
        __slots__ = ("state",)
        class PhaseSwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_PHASE_SWITCH_UNKNOWN: _ClassVar[NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState]
            STATE_PHASE_SWITCH_DISABLED: _ClassVar[NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState]
            STATE_PHASE_SWITCH_ENABLED: _ClassVar[NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState]
        STATE_PHASE_SWITCH_UNKNOWN: NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState
        STATE_PHASE_SWITCH_DISABLED: NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState
        STATE_PHASE_SWITCH_ENABLED: NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState
        def __init__(self, state: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.PhaseSwitch.PhaseSwitchState, str]] = ...) -> None: ...
    CELLULAR_FIELD_NUMBER: _ClassVar[int]
    CELLULARMODE_FIELD_NUMBER: _ClassVar[int]
    CHARGERECORDSITEMSTORAGE_FIELD_NUMBER: _ClassVar[int]
    CHARGERECORDSUNSYNCED_FIELD_NUMBER: _ClassVar[int]
    CONFIGSTATE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONINTERFACE_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEPASSWORD_FIELD_NUMBER: _ClassVar[int]
    DEVICEPIN_FIELD_NUMBER: _ClassVar[int]
    GPS_FIELD_NUMBER: _ClassVar[int]
    HARDWAREREVISION_FIELD_NUMBER: _ClassVar[int]
    INITIALSETUP_FIELD_NUMBER: _ClassVar[int]
    PHASESWITCH_FIELD_NUMBER: _ClassVar[int]
    PRODUCTTYPE_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    STATISTICVERSION_FIELD_NUMBER: _ClassVar[int]
    UTCTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERIFICATIONCODE_FIELD_NUMBER: _ClassVar[int]
    cellular: NrgcpTypes.Cellular
    cellularMode: NrgcpTypes.CellularMode
    chargeRecordsItemStorage: int
    chargeRecordsUnsynced: int
    configState: NrgcpDevicecontrolInfoGetPayload.ConfigMode
    connectionInterface: NrgcpTypes.ConnectionInterface
    deviceName: NrgcpDevicecontrolInfoGetPayload.DeviceName
    devicePassword: NrgcpDevicecontrolInfoGetPayload.DevicePassword
    devicePin: NrgcpDevicecontrolInfoGetPayload.DevicePin
    gps: NrgcpTypes.GPS
    hardwareRevision: str
    initialSetup: NrgcpTypes.InitialSetupState
    phaseSwitch: NrgcpDevicecontrolInfoGetPayload.PhaseSwitch
    productType: NrgcpTypes.ProductType
    serialNumber: str
    softwareVersion: str
    statisticVersion: int
    utcTimestamp: int
    verificationCode: str
    def __init__(self, cellular: _Optional[_Union[NrgcpTypes.Cellular, _Mapping]] = ..., cellularMode: _Optional[_Union[NrgcpTypes.CellularMode, str]] = ..., chargeRecordsItemStorage: _Optional[int] = ..., chargeRecordsUnsynced: _Optional[int] = ..., configState: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.ConfigMode, _Mapping]] = ..., connectionInterface: _Optional[_Union[NrgcpTypes.ConnectionInterface, str]] = ..., deviceName: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.DeviceName, _Mapping]] = ..., devicePassword: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.DevicePassword, _Mapping]] = ..., devicePin: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.DevicePin, _Mapping]] = ..., gps: _Optional[_Union[NrgcpTypes.GPS, _Mapping]] = ..., hardwareRevision: _Optional[str] = ..., initialSetup: _Optional[_Union[NrgcpTypes.InitialSetupState, str]] = ..., phaseSwitch: _Optional[_Union[NrgcpDevicecontrolInfoGetPayload.PhaseSwitch, _Mapping]] = ..., productType: _Optional[_Union[NrgcpTypes.ProductType, str]] = ..., serialNumber: _Optional[str] = ..., softwareVersion: _Optional[str] = ..., statisticVersion: _Optional[int] = ..., utcTimestamp: _Optional[int] = ..., verificationCode: _Optional[str] = ...) -> None: ...

class NrgcpDevicecontrolInfoUpdatePayload(_message.Message):
    __slots__ = ("configMode", "deviceName", "devicePin", "initialSetup", "password", "phaseSwitch", "utcTimestamp")
    class ConfigMode(_message.Message):
        __slots__ = ("state",)
        class ConfigModeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_CONFIG_UNKNOWN: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState]
            STATE_CONFIG_DISABLED: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState]
            STATE_CONFIG_ENABLED: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState]
        STATE_CONFIG_UNKNOWN: NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState
        STATE_CONFIG_DISABLED: NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState
        STATE_CONFIG_ENABLED: NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState
        def __init__(self, state: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.ConfigMode.ConfigModeState, str]] = ...) -> None: ...
    class DeviceName(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class DevicePin(_message.Message):
        __slots__ = ("accessControlState", "pin", "uuid")
        ACCESSCONTROLSTATE_FIELD_NUMBER: _ClassVar[int]
        PIN_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        accessControlState: NrgcpTypes.AccessControlState
        pin: str
        uuid: str
        def __init__(self, accessControlState: _Optional[_Union[NrgcpTypes.AccessControlState, str]] = ..., pin: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...
    class DevicePassword(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class PhaseSwitch(_message.Message):
        __slots__ = ("state",)
        class PhaseSwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_PHASE_SWITCH_UNKNOWN: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState]
            STATE_PHASE_SWITCH_DISABLED: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState]
            STATE_PHASE_SWITCH_ENABLED: _ClassVar[NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState]
        STATE_PHASE_SWITCH_UNKNOWN: NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState
        STATE_PHASE_SWITCH_DISABLED: NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState
        STATE_PHASE_SWITCH_ENABLED: NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState
        def __init__(self, state: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch.PhaseSwitchState, str]] = ...) -> None: ...
    CONFIGMODE_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEPIN_FIELD_NUMBER: _ClassVar[int]
    INITIALSETUP_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PHASESWITCH_FIELD_NUMBER: _ClassVar[int]
    UTCTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    configMode: NrgcpDevicecontrolInfoUpdatePayload.ConfigMode
    deviceName: NrgcpDevicecontrolInfoUpdatePayload.DeviceName
    devicePin: NrgcpDevicecontrolInfoUpdatePayload.DevicePin
    initialSetup: NrgcpTypes.InitialSetupState
    password: NrgcpDevicecontrolInfoUpdatePayload.DevicePassword
    phaseSwitch: NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch
    utcTimestamp: int
    def __init__(self, configMode: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.ConfigMode, _Mapping]] = ..., deviceName: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.DeviceName, _Mapping]] = ..., devicePin: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.DevicePin, _Mapping]] = ..., initialSetup: _Optional[_Union[NrgcpTypes.InitialSetupState, str]] = ..., password: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.DevicePassword, _Mapping]] = ..., phaseSwitch: _Optional[_Union[NrgcpDevicecontrolInfoUpdatePayload.PhaseSwitch, _Mapping]] = ..., utcTimestamp: _Optional[int] = ...) -> None: ...

class NrgcpWifiConnectUpdatePayload(_message.Message):
    __slots__ = ("bssid", "key", "ssid")
    BSSID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    key: str
    ssid: str
    def __init__(self, bssid: _Optional[str] = ..., key: _Optional[str] = ..., ssid: _Optional[str] = ...) -> None: ...

class NrgcpWifiScanGetPayload(_message.Message):
    __slots__ = ("scanResults",)
    SCANRESULTS_FIELD_NUMBER: _ClassVar[int]
    scanResults: _containers.RepeatedCompositeFieldContainer[NrgcpWifiTypes.WifiApRecordProto]
    def __init__(self, scanResults: _Optional[_Iterable[_Union[NrgcpWifiTypes.WifiApRecordProto, _Mapping]]] = ...) -> None: ...

class NrgcpWifiStatusGetPayload(_message.Message):
    __slots__ = ("ap", "aps")
    AP_FIELD_NUMBER: _ClassVar[int]
    APS_FIELD_NUMBER: _ClassVar[int]
    ap: NrgcpWifiTypes.WifiApRecordProto
    aps: _containers.RepeatedCompositeFieldContainer[NrgcpWifiTypes.WifiApRecordProto]
    def __init__(self, ap: _Optional[_Union[NrgcpWifiTypes.WifiApRecordProto, _Mapping]] = ..., aps: _Optional[_Iterable[_Union[NrgcpWifiTypes.WifiApRecordProto, _Mapping]]] = ...) -> None: ...

class NrgcpNrgdpDataGetPayload(_message.Message):
    __slots__ = ("adapter", "cellularMode", "cellular", "chargeSocket", "chargingCurrent", "chargingInfo", "cloudConnected", "connectionInterface", "cpData", "cpStatus", "deviceName", "deviceOptionsConfig", "deviceSettings", "energyMeter", "gps", "mainController", "moduleInitStates", "numConfiguredWifis", "numScannedWifis", "phaseSwitchControl", "productType", "rssiWifi", "selfTestStatus", "serialNumber", "smartModule", "star", "temperatures", "timestamp", "touch", "uptime", "voltagePcb", "voltagePhases")
    class Adapter(_message.Message):
        __slots__ = ("chargedEnergy", "connectionCycle", "countryCode", "maxCurrent", "phases", "schukoVersionId", "serial", "tagPcbType", "type2")
        class Type2(_message.Message):
            __slots__ = ("chargingCurrent", "dutycycle", "frequency", "states", "version")
            CHARGINGCURRENT_FIELD_NUMBER: _ClassVar[int]
            DUTYCYCLE_FIELD_NUMBER: _ClassVar[int]
            FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            STATES_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            chargingCurrent: float
            dutycycle: float
            frequency: float
            states: int
            version: int
            def __init__(self, chargingCurrent: _Optional[float] = ..., dutycycle: _Optional[float] = ..., frequency: _Optional[float] = ..., states: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
        CHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
        CONNECTIONCYCLE_FIELD_NUMBER: _ClassVar[int]
        COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
        MAXCURRENT_FIELD_NUMBER: _ClassVar[int]
        PHASES_FIELD_NUMBER: _ClassVar[int]
        SCHUKOVERSIONID_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        TAGPCBTYPE_FIELD_NUMBER: _ClassVar[int]
        TYPE2_FIELD_NUMBER: _ClassVar[int]
        chargedEnergy: int
        connectionCycle: int
        countryCode: int
        maxCurrent: float
        phases: int
        schukoVersionId: int
        serial: bytes
        tagPcbType: int
        type2: NrgcpNrgdpDataGetPayload.Adapter.Type2
        def __init__(self, chargedEnergy: _Optional[int] = ..., connectionCycle: _Optional[int] = ..., countryCode: _Optional[int] = ..., maxCurrent: _Optional[float] = ..., phases: _Optional[int] = ..., schukoVersionId: _Optional[int] = ..., serial: _Optional[bytes] = ..., tagPcbType: _Optional[int] = ..., type2: _Optional[_Union[NrgcpNrgdpDataGetPayload.Adapter.Type2, _Mapping]] = ...) -> None: ...
    class ChargingInfo(_message.Message):
        __slots__ = ("chargeDurationS", "chargingCycle", "currentEnergyCounter", "globalEnergyCounter", "latestRecordNumber", "measurementMode", "schukoState", "vehicleConnectTimeCounter")
        CHARGEDURATIONS_FIELD_NUMBER: _ClassVar[int]
        CHARGINGCYCLE_FIELD_NUMBER: _ClassVar[int]
        CURRENTENERGYCOUNTER_FIELD_NUMBER: _ClassVar[int]
        GLOBALENERGYCOUNTER_FIELD_NUMBER: _ClassVar[int]
        LATESTRECORDNUMBER_FIELD_NUMBER: _ClassVar[int]
        MEASUREMENTMODE_FIELD_NUMBER: _ClassVar[int]
        SCHUKOSTATE_FIELD_NUMBER: _ClassVar[int]
        VEHICLECONNECTTIMECOUNTER_FIELD_NUMBER: _ClassVar[int]
        chargeDurationS: int
        chargingCycle: int
        currentEnergyCounter: int
        globalEnergyCounter: int
        latestRecordNumber: int
        measurementMode: NrgcpTypes.MeasurementMode
        schukoState: NrgcpTypes.SchukoState
        vehicleConnectTimeCounter: int
        def __init__(self, chargeDurationS: _Optional[int] = ..., chargingCycle: _Optional[int] = ..., currentEnergyCounter: _Optional[int] = ..., globalEnergyCounter: _Optional[int] = ..., latestRecordNumber: _Optional[int] = ..., measurementMode: _Optional[_Union[NrgcpTypes.MeasurementMode, str]] = ..., schukoState: _Optional[_Union[NrgcpTypes.SchukoState, str]] = ..., vehicleConnectTimeCounter: _Optional[int] = ...) -> None: ...
    class CpData(_message.Message):
        __slots__ = ("cpNegVal", "cpPosVal", "cpPwmState")
        CPNEGVAL_FIELD_NUMBER: _ClassVar[int]
        CPPOSVAL_FIELD_NUMBER: _ClassVar[int]
        CPPWMSTATE_FIELD_NUMBER: _ClassVar[int]
        cpNegVal: int
        cpPosVal: int
        cpPwmState: NrgcpTypes.PwmState
        def __init__(self, cpNegVal: _Optional[int] = ..., cpPosVal: _Optional[int] = ..., cpPwmState: _Optional[_Union[NrgcpTypes.PwmState, str]] = ...) -> None: ...
    class DeviceSettings(_message.Message):
        __slots__ = ("capacity", "chargingLimit", "cloudAccount", "consumption", "currency", "energyCosts", "networkSettings", "services", "timezone", "unitSystem")
        class ChargingLimit(_message.Message):
            __slots__ = ("energyLimitMode", "limit")
            ENERGYLIMITMODE_FIELD_NUMBER: _ClassVar[int]
            LIMIT_FIELD_NUMBER: _ClassVar[int]
            energyLimitMode: NrgcpTypes.EnergyLimitMode
            limit: float
            def __init__(self, energyLimitMode: _Optional[_Union[NrgcpTypes.EnergyLimitMode, str]] = ..., limit: _Optional[float] = ...) -> None: ...
        class Consumption(_message.Message):
            __slots__ = ("consumptionMode", "value")
            CONSUMPTIONMODE_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            consumptionMode: NrgcpTypes.ConsumptionMode
            value: float
            def __init__(self, consumptionMode: _Optional[_Union[NrgcpTypes.ConsumptionMode, str]] = ..., value: _Optional[float] = ...) -> None: ...
        class NetworkSetting(_message.Message):
            __slots__ = ("ssid", "wifiLocation")
            SSID_FIELD_NUMBER: _ClassVar[int]
            WIFILOCATION_FIELD_NUMBER: _ClassVar[int]
            ssid: bytes
            wifiLocation: NrgcpTypes.WifiLocation
            def __init__(self, ssid: _Optional[bytes] = ..., wifiLocation: _Optional[_Union[NrgcpTypes.WifiLocation, _Mapping]] = ...) -> None: ...
        class Services(_message.Message):
            __slots__ = ("soc", "tbc")
            SOC_FIELD_NUMBER: _ClassVar[int]
            TBC_FIELD_NUMBER: _ClassVar[int]
            soc: NrgcpTypes.ConfigurationStatus
            tbc: NrgcpTypes.ConfigurationStatus
            def __init__(self, soc: _Optional[_Union[NrgcpTypes.ConfigurationStatus, str]] = ..., tbc: _Optional[_Union[NrgcpTypes.ConfigurationStatus, str]] = ...) -> None: ...
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        CHARGINGLIMIT_FIELD_NUMBER: _ClassVar[int]
        CLOUDACCOUNT_FIELD_NUMBER: _ClassVar[int]
        CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        ENERGYCOSTS_FIELD_NUMBER: _ClassVar[int]
        NETWORKSETTINGS_FIELD_NUMBER: _ClassVar[int]
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
        UNITSYSTEM_FIELD_NUMBER: _ClassVar[int]
        capacity: float
        chargingLimit: NrgcpNrgdpDataGetPayload.DeviceSettings.ChargingLimit
        cloudAccount: bytes
        consumption: NrgcpNrgdpDataGetPayload.DeviceSettings.Consumption
        currency: bytes
        energyCosts: float
        networkSettings: _containers.RepeatedCompositeFieldContainer[NrgcpNrgdpDataGetPayload.DeviceSettings.NetworkSetting]
        services: NrgcpNrgdpDataGetPayload.DeviceSettings.Services
        timezone: NrgcpTypes.Timezone
        unitSystem: NrgcpTypes.UnitSystem
        def __init__(self, capacity: _Optional[float] = ..., chargingLimit: _Optional[_Union[NrgcpNrgdpDataGetPayload.DeviceSettings.ChargingLimit, _Mapping]] = ..., cloudAccount: _Optional[bytes] = ..., consumption: _Optional[_Union[NrgcpNrgdpDataGetPayload.DeviceSettings.Consumption, _Mapping]] = ..., currency: _Optional[bytes] = ..., energyCosts: _Optional[float] = ..., networkSettings: _Optional[_Iterable[_Union[NrgcpNrgdpDataGetPayload.DeviceSettings.NetworkSetting, _Mapping]]] = ..., services: _Optional[_Union[NrgcpNrgdpDataGetPayload.DeviceSettings.Services, _Mapping]] = ..., timezone: _Optional[_Union[NrgcpTypes.Timezone, str]] = ..., unitSystem: _Optional[_Union[NrgcpTypes.UnitSystem, str]] = ...) -> None: ...
    class EnergyMeter(_message.Message):
        __slots__ = ("activePowerPhases", "apparentPowerPhases", "currentPhases", "gridFrequency", "powerFactorPhases", "reactivePowerPhases")
        class ActivePowerPhases(_message.Message):
            __slots__ = ("pL1", "pL2", "pL3", "pSUM")
            PL1_FIELD_NUMBER: _ClassVar[int]
            PL2_FIELD_NUMBER: _ClassVar[int]
            PL3_FIELD_NUMBER: _ClassVar[int]
            PSUM_FIELD_NUMBER: _ClassVar[int]
            pL1: float
            pL2: float
            pL3: float
            pSUM: float
            def __init__(self, pL1: _Optional[float] = ..., pL2: _Optional[float] = ..., pL3: _Optional[float] = ..., pSUM: _Optional[float] = ...) -> None: ...
        class ApparentPowerPhases(_message.Message):
            __slots__ = ("sL1", "sL2", "sL3", "sSUM")
            SL1_FIELD_NUMBER: _ClassVar[int]
            SL2_FIELD_NUMBER: _ClassVar[int]
            SL3_FIELD_NUMBER: _ClassVar[int]
            SSUM_FIELD_NUMBER: _ClassVar[int]
            sL1: float
            sL2: float
            sL3: float
            sSUM: float
            def __init__(self, sL1: _Optional[float] = ..., sL2: _Optional[float] = ..., sL3: _Optional[float] = ..., sSUM: _Optional[float] = ...) -> None: ...
        class CurrentPhases(_message.Message):
            __slots__ = ("iL1", "iL2", "iL3", "iN")
            IL1_FIELD_NUMBER: _ClassVar[int]
            IL2_FIELD_NUMBER: _ClassVar[int]
            IL3_FIELD_NUMBER: _ClassVar[int]
            IN_FIELD_NUMBER: _ClassVar[int]
            iL1: float
            iL2: float
            iL3: float
            iN: float
            def __init__(self, iL1: _Optional[float] = ..., iL2: _Optional[float] = ..., iL3: _Optional[float] = ..., iN: _Optional[float] = ...) -> None: ...
        class PowerFactorPhases(_message.Message):
            __slots__ = ("phiL1", "phiL2", "phiL3", "phiSUM")
            PHIL1_FIELD_NUMBER: _ClassVar[int]
            PHIL2_FIELD_NUMBER: _ClassVar[int]
            PHIL3_FIELD_NUMBER: _ClassVar[int]
            PHISUM_FIELD_NUMBER: _ClassVar[int]
            phiL1: float
            phiL2: float
            phiL3: float
            phiSUM: float
            def __init__(self, phiL1: _Optional[float] = ..., phiL2: _Optional[float] = ..., phiL3: _Optional[float] = ..., phiSUM: _Optional[float] = ...) -> None: ...
        class ReactivePowerPhases(_message.Message):
            __slots__ = ("qL1", "qL2", "qL3", "qSUM")
            QL1_FIELD_NUMBER: _ClassVar[int]
            QL2_FIELD_NUMBER: _ClassVar[int]
            QL3_FIELD_NUMBER: _ClassVar[int]
            QSUM_FIELD_NUMBER: _ClassVar[int]
            qL1: float
            qL2: float
            qL3: float
            qSUM: float
            def __init__(self, qL1: _Optional[float] = ..., qL2: _Optional[float] = ..., qL3: _Optional[float] = ..., qSUM: _Optional[float] = ...) -> None: ...
        ACTIVEPOWERPHASES_FIELD_NUMBER: _ClassVar[int]
        APPARENTPOWERPHASES_FIELD_NUMBER: _ClassVar[int]
        CURRENTPHASES_FIELD_NUMBER: _ClassVar[int]
        GRIDFREQUENCY_FIELD_NUMBER: _ClassVar[int]
        POWERFACTORPHASES_FIELD_NUMBER: _ClassVar[int]
        REACTIVEPOWERPHASES_FIELD_NUMBER: _ClassVar[int]
        activePowerPhases: NrgcpNrgdpDataGetPayload.EnergyMeter.ActivePowerPhases
        apparentPowerPhases: NrgcpNrgdpDataGetPayload.EnergyMeter.ApparentPowerPhases
        currentPhases: NrgcpNrgdpDataGetPayload.EnergyMeter.CurrentPhases
        gridFrequency: float
        powerFactorPhases: NrgcpNrgdpDataGetPayload.EnergyMeter.PowerFactorPhases
        reactivePowerPhases: NrgcpNrgdpDataGetPayload.EnergyMeter.ReactivePowerPhases
        def __init__(self, activePowerPhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter.ActivePowerPhases, _Mapping]] = ..., apparentPowerPhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter.ApparentPowerPhases, _Mapping]] = ..., currentPhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter.CurrentPhases, _Mapping]] = ..., gridFrequency: _Optional[float] = ..., powerFactorPhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter.PowerFactorPhases, _Mapping]] = ..., reactivePowerPhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter.ReactivePowerPhases, _Mapping]] = ...) -> None: ...
    class SoftwareHardwareVersion(_message.Message):
        __slots__ = ("hardwareVersion", "softwareVersion")
        HARDWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
        hardwareVersion: bytes
        softwareVersion: bytes
        def __init__(self, hardwareVersion: _Optional[bytes] = ..., softwareVersion: _Optional[bytes] = ...) -> None: ...
    class ModuleInitStates(_message.Message):
        __slots__ = ("nrgactivation", "nrgauthentication", "nrgawsiot", "nrgble", "nrgbootlinecommunicator", "nrgbootloader", "nrgdeviceinfo", "nrgi2C", "nrgreset", "nrgstatistics", "nrgsystem", "nrgtimebasedcharging", "nrgtimecontroller", "nrgupdater", "nrgwifi", "nrgwsserver")
        NRGACTIVATION_FIELD_NUMBER: _ClassVar[int]
        NRGAUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        NRGAWSIOT_FIELD_NUMBER: _ClassVar[int]
        NRGBLE_FIELD_NUMBER: _ClassVar[int]
        NRGBOOTLINECOMMUNICATOR_FIELD_NUMBER: _ClassVar[int]
        NRGBOOTLOADER_FIELD_NUMBER: _ClassVar[int]
        NRGDEVICEINFO_FIELD_NUMBER: _ClassVar[int]
        NRGI2C_FIELD_NUMBER: _ClassVar[int]
        NRGRESET_FIELD_NUMBER: _ClassVar[int]
        NRGSTATISTICS_FIELD_NUMBER: _ClassVar[int]
        NRGSYSTEM_FIELD_NUMBER: _ClassVar[int]
        NRGTIMEBASEDCHARGING_FIELD_NUMBER: _ClassVar[int]
        NRGTIMECONTROLLER_FIELD_NUMBER: _ClassVar[int]
        NRGUPDATER_FIELD_NUMBER: _ClassVar[int]
        NRGWIFI_FIELD_NUMBER: _ClassVar[int]
        NRGWSSERVER_FIELD_NUMBER: _ClassVar[int]
        nrgactivation: int
        nrgauthentication: int
        nrgawsiot: int
        nrgble: int
        nrgbootlinecommunicator: int
        nrgbootloader: int
        nrgdeviceinfo: int
        nrgi2C: int
        nrgreset: int
        nrgstatistics: int
        nrgsystem: int
        nrgtimebasedcharging: int
        nrgtimecontroller: int
        nrgupdater: int
        nrgwifi: int
        nrgwsserver: int
        def __init__(self, nrgactivation: _Optional[int] = ..., nrgauthentication: _Optional[int] = ..., nrgawsiot: _Optional[int] = ..., nrgble: _Optional[int] = ..., nrgbootlinecommunicator: _Optional[int] = ..., nrgbootloader: _Optional[int] = ..., nrgdeviceinfo: _Optional[int] = ..., nrgi2C: _Optional[int] = ..., nrgreset: _Optional[int] = ..., nrgstatistics: _Optional[int] = ..., nrgsystem: _Optional[int] = ..., nrgtimebasedcharging: _Optional[int] = ..., nrgtimecontroller: _Optional[int] = ..., nrgupdater: _Optional[int] = ..., nrgwifi: _Optional[int] = ..., nrgwsserver: _Optional[int] = ...) -> None: ...
    class SelfTestStatus(_message.Message):
        __slots__ = ("connectedPowerPhases", "errorCode", "evDiode", "fI", "nrgkickDebug1", "pER", "pE", "powerGridFreq", "powerGridVoltage", "rcdTrigger", "relais", "relayState", "warningCode")
        CONNECTEDPOWERPHASES_FIELD_NUMBER: _ClassVar[int]
        ERRORCODE_FIELD_NUMBER: _ClassVar[int]
        EVDIODE_FIELD_NUMBER: _ClassVar[int]
        FI_FIELD_NUMBER: _ClassVar[int]
        NRGKICKDEBUG1_FIELD_NUMBER: _ClassVar[int]
        PER_FIELD_NUMBER: _ClassVar[int]
        PE_FIELD_NUMBER: _ClassVar[int]
        POWERGRIDFREQ_FIELD_NUMBER: _ClassVar[int]
        POWERGRIDVOLTAGE_FIELD_NUMBER: _ClassVar[int]
        RCDTRIGGER_FIELD_NUMBER: _ClassVar[int]
        RELAIS_FIELD_NUMBER: _ClassVar[int]
        RELAYSTATE_FIELD_NUMBER: _ClassVar[int]
        WARNINGCODE_FIELD_NUMBER: _ClassVar[int]
        connectedPowerPhases: int
        errorCode: NrgcpTypes.ErrorCode
        evDiode: NrgcpTypes.SelfTest
        fI: NrgcpTypes.SelfTest
        nrgkickDebug1: bytes
        pER: int
        pE: NrgcpTypes.SelfTest
        powerGridFreq: int
        powerGridVoltage: int
        rcdTrigger: NrgcpTypes.RcdTrigger
        relais: NrgcpTypes.SelfTest
        relayState: NrgcpTypes.RelayState
        warningCode: NrgcpTypes.WarningCode
        def __init__(self, connectedPowerPhases: _Optional[int] = ..., errorCode: _Optional[_Union[NrgcpTypes.ErrorCode, str]] = ..., evDiode: _Optional[_Union[NrgcpTypes.SelfTest, str]] = ..., fI: _Optional[_Union[NrgcpTypes.SelfTest, str]] = ..., nrgkickDebug1: _Optional[bytes] = ..., pER: _Optional[int] = ..., pE: _Optional[_Union[NrgcpTypes.SelfTest, str]] = ..., powerGridFreq: _Optional[int] = ..., powerGridVoltage: _Optional[int] = ..., rcdTrigger: _Optional[_Union[NrgcpTypes.RcdTrigger, str]] = ..., relais: _Optional[_Union[NrgcpTypes.SelfTest, str]] = ..., relayState: _Optional[_Union[NrgcpTypes.RelayState, str]] = ..., warningCode: _Optional[_Union[NrgcpTypes.WarningCode, str]] = ...) -> None: ...
    class Temperatures(_message.Message):
        __slots__ = ("tempMainEm", "tempMainPcb", "tempMainPic", "tempSchuko1", "tempSchuko2", "tempSchuko3", "tempStarPic", "tempStarSens1", "tempStarSens2", "tempStarSens3")
        TEMPMAINEM_FIELD_NUMBER: _ClassVar[int]
        TEMPMAINPCB_FIELD_NUMBER: _ClassVar[int]
        TEMPMAINPIC_FIELD_NUMBER: _ClassVar[int]
        TEMPSCHUKO1_FIELD_NUMBER: _ClassVar[int]
        TEMPSCHUKO2_FIELD_NUMBER: _ClassVar[int]
        TEMPSCHUKO3_FIELD_NUMBER: _ClassVar[int]
        TEMPSTARPIC_FIELD_NUMBER: _ClassVar[int]
        TEMPSTARSENS1_FIELD_NUMBER: _ClassVar[int]
        TEMPSTARSENS2_FIELD_NUMBER: _ClassVar[int]
        TEMPSTARSENS3_FIELD_NUMBER: _ClassVar[int]
        tempMainEm: float
        tempMainPcb: float
        tempMainPic: float
        tempSchuko1: float
        tempSchuko2: float
        tempSchuko3: float
        tempStarPic: float
        tempStarSens1: float
        tempStarSens2: float
        tempStarSens3: float
        def __init__(self, tempMainEm: _Optional[float] = ..., tempMainPcb: _Optional[float] = ..., tempMainPic: _Optional[float] = ..., tempSchuko1: _Optional[float] = ..., tempSchuko2: _Optional[float] = ..., tempSchuko3: _Optional[float] = ..., tempStarPic: _Optional[float] = ..., tempStarSens1: _Optional[float] = ..., tempStarSens2: _Optional[float] = ..., tempStarSens3: _Optional[float] = ...) -> None: ...
    class VoltagePhases(_message.Message):
        __slots__ = ("phase1", "phase2", "phase3")
        PHASE1_FIELD_NUMBER: _ClassVar[int]
        PHASE2_FIELD_NUMBER: _ClassVar[int]
        PHASE3_FIELD_NUMBER: _ClassVar[int]
        phase1: float
        phase2: float
        phase3: float
        def __init__(self, phase1: _Optional[float] = ..., phase2: _Optional[float] = ..., phase3: _Optional[float] = ...) -> None: ...
    ADAPTER_FIELD_NUMBER: _ClassVar[int]
    CELLULARMODE_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_FIELD_NUMBER: _ClassVar[int]
    CHARGESOCKET_FIELD_NUMBER: _ClassVar[int]
    CHARGINGCURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGINGINFO_FIELD_NUMBER: _ClassVar[int]
    CLOUDCONNECTED_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONINTERFACE_FIELD_NUMBER: _ClassVar[int]
    CPDATA_FIELD_NUMBER: _ClassVar[int]
    CPSTATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEOPTIONSCONFIG_FIELD_NUMBER: _ClassVar[int]
    DEVICESETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENERGYMETER_FIELD_NUMBER: _ClassVar[int]
    GPS_FIELD_NUMBER: _ClassVar[int]
    MAINCONTROLLER_FIELD_NUMBER: _ClassVar[int]
    MODULEINITSTATES_FIELD_NUMBER: _ClassVar[int]
    NUMCONFIGUREDWIFIS_FIELD_NUMBER: _ClassVar[int]
    NUMSCANNEDWIFIS_FIELD_NUMBER: _ClassVar[int]
    PHASESWITCHCONTROL_FIELD_NUMBER: _ClassVar[int]
    PRODUCTTYPE_FIELD_NUMBER: _ClassVar[int]
    RSSIWIFI_FIELD_NUMBER: _ClassVar[int]
    SELFTESTSTATUS_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    SMARTMODULE_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOUCH_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    VOLTAGEPCB_FIELD_NUMBER: _ClassVar[int]
    VOLTAGEPHASES_FIELD_NUMBER: _ClassVar[int]
    adapter: NrgcpNrgdpDataGetPayload.Adapter
    cellularMode: NrgcpTypes.CellularMode
    cellular: NrgcpTypes.Cellular
    chargeSocket: NrgcpTypes.ChargeSocket
    chargingCurrent: int
    chargingInfo: NrgcpNrgdpDataGetPayload.ChargingInfo
    cloudConnected: bool
    connectionInterface: NrgcpTypes.ConnectionInterface
    cpData: NrgcpNrgdpDataGetPayload.CpData
    cpStatus: NrgcpTypes.CpStatus
    deviceName: bytes
    deviceOptionsConfig: int
    deviceSettings: NrgcpNrgdpDataGetPayload.DeviceSettings
    energyMeter: NrgcpNrgdpDataGetPayload.EnergyMeter
    gps: NrgcpTypes.GPS
    mainController: NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion
    moduleInitStates: NrgcpNrgdpDataGetPayload.ModuleInitStates
    numConfiguredWifis: int
    numScannedWifis: int
    phaseSwitchControl: int
    productType: NrgcpTypes.ProductType
    rssiWifi: int
    selfTestStatus: NrgcpNrgdpDataGetPayload.SelfTestStatus
    serialNumber: bytes
    smartModule: NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion
    star: NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion
    temperatures: NrgcpNrgdpDataGetPayload.Temperatures
    timestamp: int
    touch: NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion
    uptime: int
    voltagePcb: float
    voltagePhases: NrgcpNrgdpDataGetPayload.VoltagePhases
    def __init__(self, adapter: _Optional[_Union[NrgcpNrgdpDataGetPayload.Adapter, _Mapping]] = ..., cellularMode: _Optional[_Union[NrgcpTypes.CellularMode, str]] = ..., cellular: _Optional[_Union[NrgcpTypes.Cellular, _Mapping]] = ..., chargeSocket: _Optional[_Union[NrgcpTypes.ChargeSocket, str]] = ..., chargingCurrent: _Optional[int] = ..., chargingInfo: _Optional[_Union[NrgcpNrgdpDataGetPayload.ChargingInfo, _Mapping]] = ..., cloudConnected: bool = ..., connectionInterface: _Optional[_Union[NrgcpTypes.ConnectionInterface, str]] = ..., cpData: _Optional[_Union[NrgcpNrgdpDataGetPayload.CpData, _Mapping]] = ..., cpStatus: _Optional[_Union[NrgcpTypes.CpStatus, str]] = ..., deviceName: _Optional[bytes] = ..., deviceOptionsConfig: _Optional[int] = ..., deviceSettings: _Optional[_Union[NrgcpNrgdpDataGetPayload.DeviceSettings, _Mapping]] = ..., energyMeter: _Optional[_Union[NrgcpNrgdpDataGetPayload.EnergyMeter, _Mapping]] = ..., gps: _Optional[_Union[NrgcpTypes.GPS, _Mapping]] = ..., mainController: _Optional[_Union[NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion, _Mapping]] = ..., moduleInitStates: _Optional[_Union[NrgcpNrgdpDataGetPayload.ModuleInitStates, _Mapping]] = ..., numConfiguredWifis: _Optional[int] = ..., numScannedWifis: _Optional[int] = ..., phaseSwitchControl: _Optional[int] = ..., productType: _Optional[_Union[NrgcpTypes.ProductType, str]] = ..., rssiWifi: _Optional[int] = ..., selfTestStatus: _Optional[_Union[NrgcpNrgdpDataGetPayload.SelfTestStatus, _Mapping]] = ..., serialNumber: _Optional[bytes] = ..., smartModule: _Optional[_Union[NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion, _Mapping]] = ..., star: _Optional[_Union[NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion, _Mapping]] = ..., temperatures: _Optional[_Union[NrgcpNrgdpDataGetPayload.Temperatures, _Mapping]] = ..., timestamp: _Optional[int] = ..., touch: _Optional[_Union[NrgcpNrgdpDataGetPayload.SoftwareHardwareVersion, _Mapping]] = ..., uptime: _Optional[int] = ..., voltagePcb: _Optional[float] = ..., voltagePhases: _Optional[_Union[NrgcpNrgdpDataGetPayload.VoltagePhases, _Mapping]] = ...) -> None: ...

class NrgcpDevicecontrolAppsettingsGetPayload(_message.Message):
    __slots__ = ("batteryCapacity", "consumptionMode", "consumption", "currency", "efficacy", "pricePerKwh", "timezone", "unitSystem")
    BATTERYCAPACITY_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTIONMODE_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EFFICACY_FIELD_NUMBER: _ClassVar[int]
    PRICEPERKWH_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITSYSTEM_FIELD_NUMBER: _ClassVar[int]
    batteryCapacity: NrgcpTypes.BatteryCapacity
    consumptionMode: NrgcpTypes.ConsumptionMode
    consumption: NrgcpTypes.Consumption
    currency: NrgcpTypes.Currency
    efficacy: NrgcpTypes.Efficacy
    pricePerKwh: NrgcpTypes.PricePerKwh
    timezone: NrgcpTypes.Timezone
    unitSystem: NrgcpTypes.UnitSystem
    def __init__(self, batteryCapacity: _Optional[_Union[NrgcpTypes.BatteryCapacity, _Mapping]] = ..., consumptionMode: _Optional[_Union[NrgcpTypes.ConsumptionMode, str]] = ..., consumption: _Optional[_Union[NrgcpTypes.Consumption, _Mapping]] = ..., currency: _Optional[_Union[NrgcpTypes.Currency, _Mapping]] = ..., efficacy: _Optional[_Union[NrgcpTypes.Efficacy, _Mapping]] = ..., pricePerKwh: _Optional[_Union[NrgcpTypes.PricePerKwh, _Mapping]] = ..., timezone: _Optional[_Union[NrgcpTypes.Timezone, str]] = ..., unitSystem: _Optional[_Union[NrgcpTypes.UnitSystem, str]] = ...) -> None: ...

class NrgcpDevicecontrolAppsettingsUpdatePayload(_message.Message):
    __slots__ = ("batteryCapacity", "consumptionMode", "consumption", "currency", "efficacy", "pricePerKwh", "timezone", "unitSystem")
    BATTERYCAPACITY_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTIONMODE_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EFFICACY_FIELD_NUMBER: _ClassVar[int]
    PRICEPERKWH_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITSYSTEM_FIELD_NUMBER: _ClassVar[int]
    batteryCapacity: NrgcpTypes.BatteryCapacity
    consumptionMode: NrgcpTypes.ConsumptionMode
    consumption: NrgcpTypes.Consumption
    currency: NrgcpTypes.Currency
    efficacy: NrgcpTypes.Efficacy
    pricePerKwh: NrgcpTypes.PricePerKwh
    timezone: NrgcpTypes.Timezone
    unitSystem: NrgcpTypes.UnitSystem
    def __init__(self, batteryCapacity: _Optional[_Union[NrgcpTypes.BatteryCapacity, _Mapping]] = ..., consumptionMode: _Optional[_Union[NrgcpTypes.ConsumptionMode, str]] = ..., consumption: _Optional[_Union[NrgcpTypes.Consumption, _Mapping]] = ..., currency: _Optional[_Union[NrgcpTypes.Currency, _Mapping]] = ..., efficacy: _Optional[_Union[NrgcpTypes.Efficacy, _Mapping]] = ..., pricePerKwh: _Optional[_Union[NrgcpTypes.PricePerKwh, _Mapping]] = ..., timezone: _Optional[_Union[NrgcpTypes.Timezone, str]] = ..., unitSystem: _Optional[_Union[NrgcpTypes.UnitSystem, str]] = ...) -> None: ...

class NrgcpDevicecontrolActivationGetPayload(_message.Message):
    __slots__ = ("activationCode",)
    ACTIVATIONCODE_FIELD_NUMBER: _ClassVar[int]
    activationCode: str
    def __init__(self, activationCode: _Optional[str] = ...) -> None: ...

class NrgcpTimebasedchargingChargingEventsGetPayload(_message.Message):
    __slots__ = ("chargingEventFriday", "chargingEventMonday", "chargingEventSaturday", "chargingEventSunday", "chargingEventThursday", "chargingEventTuesday", "chargingEventWednesday")
    CHARGINGEVENTFRIDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTMONDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTSATURDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTSUNDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTTHURSDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTTUESDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTWEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    chargingEventFriday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventMonday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventSaturday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventSunday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventThursday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventTuesday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventWednesday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    def __init__(self, chargingEventFriday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventMonday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventSaturday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventSunday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventThursday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventTuesday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventWednesday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ...) -> None: ...

class NrgcpTimebasedchargingChargingEventsUpdatePayload(_message.Message):
    __slots__ = ("chargingEventFriday", "chargingEventMonday", "chargingEventSaturday", "chargingEventSunday", "chargingEventThursday", "chargingEventTuesday", "chargingEventWednesday")
    CHARGINGEVENTFRIDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTMONDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTSATURDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTSUNDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTTHURSDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTTUESDAY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGEVENTWEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    chargingEventFriday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventMonday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventSaturday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventSunday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventThursday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventTuesday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    chargingEventWednesday: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.TimeBasedChargingEvent]
    def __init__(self, chargingEventFriday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventMonday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventSaturday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventSunday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventThursday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventTuesday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ..., chargingEventWednesday: _Optional[_Iterable[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]]] = ...) -> None: ...

class NrgcpDevicecontrolResetUpdatePayload(_message.Message):
    __slots__ = ("resetType",)
    RESETTYPE_FIELD_NUMBER: _ClassVar[int]
    resetType: NrgcpTypes.ResetType
    def __init__(self, resetType: _Optional[_Union[NrgcpTypes.ResetType, str]] = ...) -> None: ...

class NrgcpChargecontrolChargerecordGetPayload(_message.Message):
    __slots__ = ("chargeDurationS", "chargedEnergy", "chargingMode", "connectionInterface", "currency", "errorCode", "globalChargedEnergyCounterBegin", "globalChargedEnergyCounterEnd", "isTimeSyncedAtStart", "latitude", "longitude", "messSwapEn", "pricePerKwh", "recordNumber", "status", "tagSerialNumber", "tagType", "timeSource", "timestampBeginVehicleConnect", "timestampChargingEnd", "timestampEndOffset", "timestampEnd", "timestampStartOffset", "timestampStart", "triedToSyncTime", "vehicleConnectCount", "wifiLocation")
    CHARGEDURATIONS_FIELD_NUMBER: _ClassVar[int]
    CHARGEDENERGY_FIELD_NUMBER: _ClassVar[int]
    CHARGINGMODE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONINTERFACE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    GLOBALCHARGEDENERGYCOUNTERBEGIN_FIELD_NUMBER: _ClassVar[int]
    GLOBALCHARGEDENERGYCOUNTEREND_FIELD_NUMBER: _ClassVar[int]
    ISTIMESYNCEDATSTART_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MESSSWAPEN_FIELD_NUMBER: _ClassVar[int]
    PRICEPERKWH_FIELD_NUMBER: _ClassVar[int]
    RECORDNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGSERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    TAGTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESOURCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPBEGINVEHICLECONNECT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPCHARGINGEND_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPENDOFFSET_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPEND_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPSTARTOFFSET_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPSTART_FIELD_NUMBER: _ClassVar[int]
    TRIEDTOSYNCTIME_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
    WIFILOCATION_FIELD_NUMBER: _ClassVar[int]
    chargeDurationS: int
    chargedEnergy: int
    chargingMode: int
    connectionInterface: int
    currency: str
    errorCode: int
    globalChargedEnergyCounterBegin: int
    globalChargedEnergyCounterEnd: int
    isTimeSyncedAtStart: bool
    latitude: float
    longitude: float
    messSwapEn: bool
    pricePerKwh: float
    recordNumber: int
    status: int
    tagSerialNumber: str
    tagType: int
    timeSource: int
    timestampBeginVehicleConnect: int
    timestampChargingEnd: int
    timestampEndOffset: int
    timestampEnd: int
    timestampStartOffset: int
    timestampStart: int
    triedToSyncTime: bool
    vehicleConnectCount: int
    wifiLocation: NrgcpTypes.WifiLocation
    def __init__(self, chargeDurationS: _Optional[int] = ..., chargedEnergy: _Optional[int] = ..., chargingMode: _Optional[int] = ..., connectionInterface: _Optional[int] = ..., currency: _Optional[str] = ..., errorCode: _Optional[int] = ..., globalChargedEnergyCounterBegin: _Optional[int] = ..., globalChargedEnergyCounterEnd: _Optional[int] = ..., isTimeSyncedAtStart: bool = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., messSwapEn: bool = ..., pricePerKwh: _Optional[float] = ..., recordNumber: _Optional[int] = ..., status: _Optional[int] = ..., tagSerialNumber: _Optional[str] = ..., tagType: _Optional[int] = ..., timeSource: _Optional[int] = ..., timestampBeginVehicleConnect: _Optional[int] = ..., timestampChargingEnd: _Optional[int] = ..., timestampEndOffset: _Optional[int] = ..., timestampEnd: _Optional[int] = ..., timestampStartOffset: _Optional[int] = ..., timestampStart: _Optional[int] = ..., triedToSyncTime: bool = ..., vehicleConnectCount: _Optional[int] = ..., wifiLocation: _Optional[_Union[NrgcpTypes.WifiLocation, _Mapping]] = ...) -> None: ...

class NrgcpChargecontrolChargerecordGetPayloadRequest(_message.Message):
    __slots__ = ("recordNumber",)
    RECORDNUMBER_FIELD_NUMBER: _ClassVar[int]
    recordNumber: int
    def __init__(self, recordNumber: _Optional[int] = ...) -> None: ...

class NrgcpTimebasedchargingStateGetPayload(_message.Message):
    __slots__ = ("currentChargingEvent", "timeBasedChargingState")
    class TimeBasedChargingState(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: NrgcpTypes.TimeBasedChargingState
        def __init__(self, value: _Optional[_Union[NrgcpTypes.TimeBasedChargingState, str]] = ...) -> None: ...
    CURRENTCHARGINGEVENT_FIELD_NUMBER: _ClassVar[int]
    TIMEBASEDCHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    currentChargingEvent: NrgcpTypes.TimeBasedChargingEvent
    timeBasedChargingState: NrgcpTimebasedchargingStateGetPayload.TimeBasedChargingState
    def __init__(self, currentChargingEvent: _Optional[_Union[NrgcpTypes.TimeBasedChargingEvent, _Mapping]] = ..., timeBasedChargingState: _Optional[_Union[NrgcpTimebasedchargingStateGetPayload.TimeBasedChargingState, _Mapping]] = ...) -> None: ...

class NrgcpTimebasedchargingStateUpdatePayload(_message.Message):
    __slots__ = ("timeBasedChargingState",)
    class TimeBasedChargingState(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: NrgcpTypes.TimeBasedChargingState
        def __init__(self, value: _Optional[_Union[NrgcpTypes.TimeBasedChargingState, str]] = ...) -> None: ...
    TIMEBASEDCHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    timeBasedChargingState: NrgcpTimebasedchargingStateUpdatePayload.TimeBasedChargingState
    def __init__(self, timeBasedChargingState: _Optional[_Union[NrgcpTimebasedchargingStateUpdatePayload.TimeBasedChargingState, _Mapping]] = ...) -> None: ...

class NrgcpWifiLocationGetPayload(_message.Message):
    __slots__ = ("locations",)
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[NrgcpTypes.WifiLocation]
    def __init__(self, locations: _Optional[_Iterable[_Union[NrgcpTypes.WifiLocation, _Mapping]]] = ...) -> None: ...

class NrgcpWifiLocationUpdatePayload(_message.Message):
    __slots__ = ("location", "ssid")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    location: NrgcpTypes.WifiLocation
    ssid: str
    def __init__(self, location: _Optional[_Union[NrgcpTypes.WifiLocation, _Mapping]] = ..., ssid: _Optional[str] = ...) -> None: ...

class NrgcpSolarchargingSolarinverterscanGetPayload(_message.Message):
    __slots__ = ("inverters",)
    INVERTERS_FIELD_NUMBER: _ClassVar[int]
    inverters: NrgcpSolarchargingTypes.SolarInverterInfo
    def __init__(self, inverters: _Optional[_Union[NrgcpSolarchargingTypes.SolarInverterInfo, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingDataGetPayload(_message.Message):
    __slots__ = ("batteryChargeWh", "batteryData", "batteryDischargeWh", "chargedEnergyWh", "chargedFromExtSrcWh", "chargingState", "combBatPowerW", "combGridPowerW", "combLoadPowerW", "combPvEnergyWhDay", "combPvPowerW", "combSlLoadW", "dischargeToExtSinkWh", "energyMeterData", "generateEnergyWh", "gridConsumptionWh", "gridFeedWh", "inverterData", "loadEnergyWh", "mainToEv", "producedSolarEnergyWh", "recChargingPowerW", "smState", "smToMainW", "smartLoadData", "smartLoadEnergyWh")
    BATTERYCHARGEWH_FIELD_NUMBER: _ClassVar[int]
    BATTERYDATA_FIELD_NUMBER: _ClassVar[int]
    BATTERYDISCHARGEWH_FIELD_NUMBER: _ClassVar[int]
    CHARGEDENERGYWH_FIELD_NUMBER: _ClassVar[int]
    CHARGEDFROMEXTSRCWH_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    COMBBATPOWERW_FIELD_NUMBER: _ClassVar[int]
    COMBGRIDPOWERW_FIELD_NUMBER: _ClassVar[int]
    COMBLOADPOWERW_FIELD_NUMBER: _ClassVar[int]
    COMBPVENERGYWHDAY_FIELD_NUMBER: _ClassVar[int]
    COMBPVPOWERW_FIELD_NUMBER: _ClassVar[int]
    COMBSLLOADW_FIELD_NUMBER: _ClassVar[int]
    DISCHARGETOEXTSINKWH_FIELD_NUMBER: _ClassVar[int]
    ENERGYMETERDATA_FIELD_NUMBER: _ClassVar[int]
    GENERATEENERGYWH_FIELD_NUMBER: _ClassVar[int]
    GRIDCONSUMPTIONWH_FIELD_NUMBER: _ClassVar[int]
    GRIDFEEDWH_FIELD_NUMBER: _ClassVar[int]
    INVERTERDATA_FIELD_NUMBER: _ClassVar[int]
    LOADENERGYWH_FIELD_NUMBER: _ClassVar[int]
    MAINTOEV_FIELD_NUMBER: _ClassVar[int]
    PRODUCEDSOLARENERGYWH_FIELD_NUMBER: _ClassVar[int]
    RECCHARGINGPOWERW_FIELD_NUMBER: _ClassVar[int]
    SMSTATE_FIELD_NUMBER: _ClassVar[int]
    SMTOMAINW_FIELD_NUMBER: _ClassVar[int]
    SMARTLOADDATA_FIELD_NUMBER: _ClassVar[int]
    SMARTLOADENERGYWH_FIELD_NUMBER: _ClassVar[int]
    batteryChargeWh: int
    batteryData: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SolarBatteryData]
    batteryDischargeWh: int
    chargedEnergyWh: int
    chargedFromExtSrcWh: int
    chargingState: int
    combBatPowerW: int
    combGridPowerW: int
    combLoadPowerW: int
    combPvEnergyWhDay: int
    combPvPowerW: int
    combSlLoadW: int
    dischargeToExtSinkWh: int
    energyMeterData: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.EnergyMeterData]
    generateEnergyWh: int
    gridConsumptionWh: int
    gridFeedWh: int
    inverterData: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SolarInverterData]
    loadEnergyWh: int
    mainToEv: int
    producedSolarEnergyWh: int
    recChargingPowerW: int
    smState: int
    smToMainW: int
    smartLoadData: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SmartLoadData]
    smartLoadEnergyWh: int
    def __init__(self, batteryChargeWh: _Optional[int] = ..., batteryData: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SolarBatteryData, _Mapping]]] = ..., batteryDischargeWh: _Optional[int] = ..., chargedEnergyWh: _Optional[int] = ..., chargedFromExtSrcWh: _Optional[int] = ..., chargingState: _Optional[int] = ..., combBatPowerW: _Optional[int] = ..., combGridPowerW: _Optional[int] = ..., combLoadPowerW: _Optional[int] = ..., combPvEnergyWhDay: _Optional[int] = ..., combPvPowerW: _Optional[int] = ..., combSlLoadW: _Optional[int] = ..., dischargeToExtSinkWh: _Optional[int] = ..., energyMeterData: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.EnergyMeterData, _Mapping]]] = ..., generateEnergyWh: _Optional[int] = ..., gridConsumptionWh: _Optional[int] = ..., gridFeedWh: _Optional[int] = ..., inverterData: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SolarInverterData, _Mapping]]] = ..., loadEnergyWh: _Optional[int] = ..., mainToEv: _Optional[int] = ..., producedSolarEnergyWh: _Optional[int] = ..., recChargingPowerW: _Optional[int] = ..., smState: _Optional[int] = ..., smToMainW: _Optional[int] = ..., smartLoadData: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SmartLoadData, _Mapping]]] = ..., smartLoadEnergyWh: _Optional[int] = ...) -> None: ...

class NrgcpSolarchargingProfilesGetPayload(_message.Message):
    __slots__ = ("activeProfileIdx", "profiles")
    ACTIVEPROFILEIDX_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    activeProfileIdx: int
    profiles: NrgcpSolarchargingTypes.SolarProfile
    def __init__(self, activeProfileIdx: _Optional[int] = ..., profiles: _Optional[_Union[NrgcpSolarchargingTypes.SolarProfile, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingProfileUpdatePayload(_message.Message):
    __slots__ = ("enabled", "idx", "profile")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    idx: int
    profile: NrgcpSolarchargingTypes.SolarProfile
    def __init__(self, enabled: bool = ..., idx: _Optional[int] = ..., profile: _Optional[_Union[NrgcpSolarchargingTypes.SolarProfile, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingProfileDeletePayload(_message.Message):
    __slots__ = ("idx", "deleteType")
    class DeleteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELTE_TYPE_SOFT: _ClassVar[NrgcpSolarchargingProfileDeletePayload.DeleteType]
        DELTE_TYPE_HARD: _ClassVar[NrgcpSolarchargingProfileDeletePayload.DeleteType]
    DELTE_TYPE_SOFT: NrgcpSolarchargingProfileDeletePayload.DeleteType
    DELTE_TYPE_HARD: NrgcpSolarchargingProfileDeletePayload.DeleteType
    IDX_FIELD_NUMBER: _ClassVar[int]
    DELETETYPE_FIELD_NUMBER: _ClassVar[int]
    idx: int
    deleteType: NrgcpSolarchargingProfileDeletePayload.DeleteType
    def __init__(self, idx: _Optional[int] = ..., deleteType: _Optional[_Union[NrgcpSolarchargingProfileDeletePayload.DeleteType, str]] = ...) -> None: ...

class NrgcpSolarchargingStateGetPayload(_message.Message):
    __slots__ = ("activeProfile", "deviceInfo", "state")
    ACTIVEPROFILE_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    activeProfile: int
    deviceInfo: NrgcpSolarchargingTypes.DeviceFailInfo
    state: NrgcpSolarchargingTypes.SolarChargingState
    def __init__(self, activeProfile: _Optional[int] = ..., deviceInfo: _Optional[_Union[NrgcpSolarchargingTypes.DeviceFailInfo, _Mapping]] = ..., state: _Optional[_Union[NrgcpSolarchargingTypes.SolarChargingState, str]] = ...) -> None: ...

class NrgcpSolarchargingStateUpdatePayload(_message.Message):
    __slots__ = ("activeProfile", "state")
    ACTIVEPROFILE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    activeProfile: int
    state: NrgcpSolarchargingTypes.SolarChargingState
    def __init__(self, activeProfile: _Optional[int] = ..., state: _Optional[_Union[NrgcpSolarchargingTypes.SolarChargingState, str]] = ...) -> None: ...

class NrgcpDevicecontrolDiagnosticdataGetPayload(_message.Message):
    __slots__ = ("bleRssi", "cpData", "errorCode", "nrgkickDebug1", "rcdTrigger", "relayState", "selfTestPeR", "warningCode")
    class CpData(_message.Message):
        __slots__ = ("code", "cpNegVal", "cpPosVal")
        CODE_FIELD_NUMBER: _ClassVar[int]
        CPNEGVAL_FIELD_NUMBER: _ClassVar[int]
        CPPOSVAL_FIELD_NUMBER: _ClassVar[int]
        code: NrgcpTypes.CpStatus
        cpNegVal: int
        cpPosVal: int
        def __init__(self, code: _Optional[_Union[NrgcpTypes.CpStatus, str]] = ..., cpNegVal: _Optional[int] = ..., cpPosVal: _Optional[int] = ...) -> None: ...
    BLERSSI_FIELD_NUMBER: _ClassVar[int]
    CPDATA_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    NRGKICKDEBUG1_FIELD_NUMBER: _ClassVar[int]
    RCDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    RELAYSTATE_FIELD_NUMBER: _ClassVar[int]
    SELFTESTPER_FIELD_NUMBER: _ClassVar[int]
    WARNINGCODE_FIELD_NUMBER: _ClassVar[int]
    bleRssi: int
    cpData: NrgcpDevicecontrolDiagnosticdataGetPayload.CpData
    errorCode: int
    nrgkickDebug1: int
    rcdTrigger: int
    relayState: int
    selfTestPeR: int
    warningCode: int
    def __init__(self, bleRssi: _Optional[int] = ..., cpData: _Optional[_Union[NrgcpDevicecontrolDiagnosticdataGetPayload.CpData, _Mapping]] = ..., errorCode: _Optional[int] = ..., nrgkickDebug1: _Optional[int] = ..., rcdTrigger: _Optional[int] = ..., relayState: _Optional[int] = ..., selfTestPeR: _Optional[int] = ..., warningCode: _Optional[int] = ...) -> None: ...

class NrgcpDevicecontrolSystemUpdatePayload(_message.Message):
    __slots__ = ("restartMode",)
    RESTARTMODE_FIELD_NUMBER: _ClassVar[int]
    restartMode: NrgcpTypes.RestartMode
    def __init__(self, restartMode: _Optional[_Union[NrgcpTypes.RestartMode, str]] = ...) -> None: ...

class NrgcpSolarchargingEnergymeterscanGetPayload(_message.Message):
    __slots__ = ("energyMeters",)
    ENERGYMETERS_FIELD_NUMBER: _ClassVar[int]
    energyMeters: NrgcpSolarchargingTypes.EnergyMeterInfo
    def __init__(self, energyMeters: _Optional[_Union[NrgcpSolarchargingTypes.EnergyMeterInfo, _Mapping]] = ...) -> None: ...

class NrgcpLicenseServicesGetPayload(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: NrgcpLicenseServicesTypes.LicenseServices
    def __init__(self, services: _Optional[_Union[NrgcpLicenseServicesTypes.LicenseServices, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingDevicepingGetPayload(_message.Message):
    __slots__ = ("devicePing",)
    DEVICEPING_FIELD_NUMBER: _ClassVar[int]
    devicePing: NrgcpSolarchargingTypes.DevicePing
    def __init__(self, devicePing: _Optional[_Union[NrgcpSolarchargingTypes.DevicePing, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingSmartloadscanGetPayload(_message.Message):
    __slots__ = ("smartLoads",)
    SMARTLOADS_FIELD_NUMBER: _ClassVar[int]
    smartLoads: NrgcpSolarchargingTypes.SmartLoadInfo
    def __init__(self, smartLoads: _Optional[_Union[NrgcpSolarchargingTypes.SmartLoadInfo, _Mapping]] = ...) -> None: ...

class NrgcpSolarchargingBatteryscanGetPayload(_message.Message):
    __slots__ = ("batteryInfo",)
    BATTERYINFO_FIELD_NUMBER: _ClassVar[int]
    batteryInfo: NrgcpSolarchargingTypes.BatteryInfo
    def __init__(self, batteryInfo: _Optional[_Union[NrgcpSolarchargingTypes.BatteryInfo, _Mapping]] = ...) -> None: ...

class NrgcpStatisticsSolarstatisticsdataGetPayload(_message.Message):
    __slots__ = ("requestInfo", "solarStatistics")
    REQUESTINFO_FIELD_NUMBER: _ClassVar[int]
    SOLARSTATISTICS_FIELD_NUMBER: _ClassVar[int]
    requestInfo: NrgcpStatisticsTypes.RequestInfo
    solarStatistics: _containers.RepeatedCompositeFieldContainer[NrgcpStatisticsTypes.SolarChargingStatistics]
    def __init__(self, requestInfo: _Optional[_Union[NrgcpStatisticsTypes.RequestInfo, _Mapping]] = ..., solarStatistics: _Optional[_Iterable[_Union[NrgcpStatisticsTypes.SolarChargingStatistics, _Mapping]]] = ...) -> None: ...

class NrgcpStatisticsSolarstatisticsinfoGetPayload(_message.Message):
    __slots__ = ("newestTs", "numDataPoints", "oldestTs")
    NEWESTTS_FIELD_NUMBER: _ClassVar[int]
    NUMDATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    OLDESTTS_FIELD_NUMBER: _ClassVar[int]
    newestTs: int
    numDataPoints: int
    oldestTs: int
    def __init__(self, newestTs: _Optional[int] = ..., numDataPoints: _Optional[int] = ..., oldestTs: _Optional[int] = ...) -> None: ...

class NrgcpSolarchargingFullscanGetPayload(_message.Message):
    __slots__ = ("fullScanInfo",)
    FULLSCANINFO_FIELD_NUMBER: _ClassVar[int]
    fullScanInfo: NrgcpSolarchargingTypes.FullScanInfo
    def __init__(self, fullScanInfo: _Optional[_Union[NrgcpSolarchargingTypes.FullScanInfo, _Mapping]] = ...) -> None: ...

class NrgcpTypes(_message.Message):
    __slots__ = ()
    class AccessControlState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_ACCESS_CONTROL_STATE: _ClassVar[NrgcpTypes.AccessControlState]
        CHANGE_PIN: _ClassVar[NrgcpTypes.AccessControlState]
        AUTHORIZE_CLIENT: _ClassVar[NrgcpTypes.AccessControlState]
    UNKNOWN_ACCESS_CONTROL_STATE: NrgcpTypes.AccessControlState
    CHANGE_PIN: NrgcpTypes.AccessControlState
    AUTHORIZE_CLIENT: NrgcpTypes.AccessControlState
    class CellularMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CELLULAR_MODE_UNKNOWN: _ClassVar[NrgcpTypes.CellularMode]
        CELLULAR_MODE_GPRS: _ClassVar[NrgcpTypes.CellularMode]
        CELLULAR_MODE_NB_IOT: _ClassVar[NrgcpTypes.CellularMode]
        CELLULAR_MODE_CAT_M: _ClassVar[NrgcpTypes.CellularMode]
    CELLULAR_MODE_UNKNOWN: NrgcpTypes.CellularMode
    CELLULAR_MODE_GPRS: NrgcpTypes.CellularMode
    CELLULAR_MODE_NB_IOT: NrgcpTypes.CellularMode
    CELLULAR_MODE_CAT_M: NrgcpTypes.CellularMode
    class ChargeSocket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CHARGE_SOCKET: _ClassVar[NrgcpTypes.ChargeSocket]
        SOCKET_NONE: _ClassVar[NrgcpTypes.ChargeSocket]
        SOCKET_SCHUCKO: _ClassVar[NrgcpTypes.ChargeSocket]
        SOCKET_16A: _ClassVar[NrgcpTypes.ChargeSocket]
        SOCKET_32A: _ClassVar[NrgcpTypes.ChargeSocket]
        SOCKET_T2: _ClassVar[NrgcpTypes.ChargeSocket]
    UNKNOWN_CHARGE_SOCKET: NrgcpTypes.ChargeSocket
    SOCKET_NONE: NrgcpTypes.ChargeSocket
    SOCKET_SCHUCKO: NrgcpTypes.ChargeSocket
    SOCKET_16A: NrgcpTypes.ChargeSocket
    SOCKET_32A: NrgcpTypes.ChargeSocket
    SOCKET_T2: NrgcpTypes.ChargeSocket
    class ChargingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CHARGING_STATE: _ClassVar[NrgcpTypes.ChargingState]
        CHARGING: _ClassVar[NrgcpTypes.ChargingState]
        PAUSE_CHARGING: _ClassVar[NrgcpTypes.ChargingState]
        NO_CHARGING: _ClassVar[NrgcpTypes.ChargingState]
    UNKNOWN_CHARGING_STATE: NrgcpTypes.ChargingState
    CHARGING: NrgcpTypes.ChargingState
    PAUSE_CHARGING: NrgcpTypes.ChargingState
    NO_CHARGING: NrgcpTypes.ChargingState
    class ConfigurationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CONFIGURATION_STATUS: _ClassVar[NrgcpTypes.ConfigurationStatus]
        ENABLED: _ClassVar[NrgcpTypes.ConfigurationStatus]
        DISABLED: _ClassVar[NrgcpTypes.ConfigurationStatus]
    UNKNOWN_CONFIGURATION_STATUS: NrgcpTypes.ConfigurationStatus
    ENABLED: NrgcpTypes.ConfigurationStatus
    DISABLED: NrgcpTypes.ConfigurationStatus
    class ConnectionInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_INTERFACE_UNKNOWN: _ClassVar[NrgcpTypes.ConnectionInterface]
        CONNECTION_INTERFACE_WIFI: _ClassVar[NrgcpTypes.ConnectionInterface]
        CONNECTION_INTERFACE_CELLULAR: _ClassVar[NrgcpTypes.ConnectionInterface]
    CONNECTION_INTERFACE_UNKNOWN: NrgcpTypes.ConnectionInterface
    CONNECTION_INTERFACE_WIFI: NrgcpTypes.ConnectionInterface
    CONNECTION_INTERFACE_CELLULAR: NrgcpTypes.ConnectionInterface
    class ConsumptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CONSUMPTION_MODE: _ClassVar[NrgcpTypes.ConsumptionMode]
        KWH_PER_100KM: _ClassVar[NrgcpTypes.ConsumptionMode]
        KM_PER_KWH: _ClassVar[NrgcpTypes.ConsumptionMode]
    UNKNOWN_CONSUMPTION_MODE: NrgcpTypes.ConsumptionMode
    KWH_PER_100KM: NrgcpTypes.ConsumptionMode
    KM_PER_KWH: NrgcpTypes.ConsumptionMode
    class CpStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CP_STATUS: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_A_STANDBY: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_B_CONNECTED: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_C_CHARGE_ACTIVE: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_D_CHARGE_ACTIVE_VENTILATION: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_E_NO_POWER: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_F_ERROR: _ClassVar[NrgcpTypes.CpStatus]
        NRG_CP_E_WAKEUP: _ClassVar[NrgcpTypes.CpStatus]
    UNKNOWN_CP_STATUS: NrgcpTypes.CpStatus
    NRG_CP_A_STANDBY: NrgcpTypes.CpStatus
    NRG_CP_B_CONNECTED: NrgcpTypes.CpStatus
    NRG_CP_C_CHARGE_ACTIVE: NrgcpTypes.CpStatus
    NRG_CP_D_CHARGE_ACTIVE_VENTILATION: NrgcpTypes.CpStatus
    NRG_CP_E_NO_POWER: NrgcpTypes.CpStatus
    NRG_CP_F_ERROR: NrgcpTypes.CpStatus
    NRG_CP_E_WAKEUP: NrgcpTypes.CpStatus
    class EnergyLimitMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENERGY_LIMIT_MODE_UNKNOWN: _ClassVar[NrgcpTypes.EnergyLimitMode]
        ENERGY_LIMIT_MODE_LIMITED: _ClassVar[NrgcpTypes.EnergyLimitMode]
        ENERGY_LIMIT_MODE_UNLIMITED: _ClassVar[NrgcpTypes.EnergyLimitMode]
    ENERGY_LIMIT_MODE_UNKNOWN: NrgcpTypes.EnergyLimitMode
    ENERGY_LIMIT_MODE_LIMITED: NrgcpTypes.EnergyLimitMode
    ENERGY_LIMIT_MODE_UNLIMITED: NrgcpTypes.EnergyLimitMode
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_ERROR_CODE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_NO_ERROR: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_GENERAL_ERROR: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_RCD: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_CPSG_ERROR_UNKNOWN: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_CPSG_ERROR_TRANSMISSION: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_CPSG_ERROR_DIODE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_CPSG_ERROR_EV_6V: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_CPSG_ERROR_EV_3V: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_FAIL_ACKNOWLEDGED: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_WAIT_FOR_ACKNOWLEDGE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_RAM: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_RCD: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_RAM: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_RAM_RCD: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_RCD: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_RCD_RAM: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SUPPLY_VOLTAGE_ERROR: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SUPPLY_PHASE_ERROR: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERVOLTAGE_SOURCE_PHASE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_UNDERVOLTAGE_SOURCE_PHASE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_NO_TAG_OF_CONNECTORUNIT_FOUND: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_32A_ADAPTER_ON_16A_UNIT: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SELFTEST_PE_FAIL: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERVOLTAGE_SOURCE_PHASE_PE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_UNDERVOLTAGE_SOURCE_PHASE_PE: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_GRID_UNDERFREQUENCY: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_GRID_OVERFREQUENCY: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERTEMPERATURE_SYSTEM: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERTEMPERATURE_MAIN: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERTEMPERATURE_STAR: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_OVERTEMPERATURE_SCHUKO: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_SUPPLY_PHASE_LOSS_TRIGGERED: _ClassVar[NrgcpTypes.ErrorCode]
        SYS_ERROR_CODE_UNPLUG_DETECTION_TRIGGERED: _ClassVar[NrgcpTypes.ErrorCode]
    UNKNOWN_ERROR_CODE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_NO_ERROR: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_GENERAL_ERROR: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_RCD: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_CPSG_ERROR_UNKNOWN: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_CPSG_ERROR_TRANSMISSION: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_CPSG_ERROR_DIODE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_CPSG_ERROR_EV_6V: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_CPSG_ERROR_EV_3V: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_FAIL_ACKNOWLEDGED: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_WAIT_FOR_ACKNOWLEDGE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_RAM: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_RCD: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_RAM: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_RAM_RCD: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_RCD: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_RCD_RAM: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SUPPLY_VOLTAGE_ERROR: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SUPPLY_PHASE_ERROR: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERVOLTAGE_SOURCE_PHASE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_UNDERVOLTAGE_SOURCE_PHASE: NrgcpTypes.ErrorCode
    SYS_ERROR_NO_TAG_OF_CONNECTORUNIT_FOUND: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_32A_ADAPTER_ON_16A_UNIT: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SELFTEST_PE_FAIL: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERVOLTAGE_SOURCE_PHASE_PE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_UNDERVOLTAGE_SOURCE_PHASE_PE: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_GRID_UNDERFREQUENCY: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_GRID_OVERFREQUENCY: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERTEMPERATURE_SYSTEM: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERTEMPERATURE_MAIN: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERTEMPERATURE_STAR: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_OVERTEMPERATURE_SCHUKO: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_SUPPLY_PHASE_LOSS_TRIGGERED: NrgcpTypes.ErrorCode
    SYS_ERROR_CODE_UNPLUG_DETECTION_TRIGGERED: NrgcpTypes.ErrorCode
    class InitialSetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_INIT_SETUP_STATE: _ClassVar[NrgcpTypes.InitialSetupState]
        INIT_SETUP_INCOMPLETE: _ClassVar[NrgcpTypes.InitialSetupState]
        INIT_SETUP_COMPLETE: _ClassVar[NrgcpTypes.InitialSetupState]
    UNKNOWN_INIT_SETUP_STATE: NrgcpTypes.InitialSetupState
    INIT_SETUP_INCOMPLETE: NrgcpTypes.InitialSetupState
    INIT_SETUP_COMPLETE: NrgcpTypes.InitialSetupState
    class MeasurementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MESS_SWAP_STATE: _ClassVar[NrgcpTypes.MeasurementMode]
        NORMAL_OPERATION: _ClassVar[NrgcpTypes.MeasurementMode]
        INVERTED_PHASE_MEASUREMENT: _ClassVar[NrgcpTypes.MeasurementMode]
    UNKNOWN_MESS_SWAP_STATE: NrgcpTypes.MeasurementMode
    NORMAL_OPERATION: NrgcpTypes.MeasurementMode
    INVERTED_PHASE_MEASUREMENT: NrgcpTypes.MeasurementMode
    class ProductType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_PRODUCT_TYPE: _ClassVar[NrgcpTypes.ProductType]
        NRGKICK_16A: _ClassVar[NrgcpTypes.ProductType]
        NRGKICK_32A: _ClassVar[NrgcpTypes.ProductType]
        NRGKICK_16A_SIM: _ClassVar[NrgcpTypes.ProductType]
        NRGKICK_32A_SIM: _ClassVar[NrgcpTypes.ProductType]
    UNKNOWN_PRODUCT_TYPE: NrgcpTypes.ProductType
    NRGKICK_16A: NrgcpTypes.ProductType
    NRGKICK_32A: NrgcpTypes.ProductType
    NRGKICK_16A_SIM: NrgcpTypes.ProductType
    NRGKICK_32A_SIM: NrgcpTypes.ProductType
    class PwmState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_PWM_STATE: _ClassVar[NrgcpTypes.PwmState]
        PWM_STATE_INACTIVE: _ClassVar[NrgcpTypes.PwmState]
        PWM_STATE_ACTIVE: _ClassVar[NrgcpTypes.PwmState]
    UNKNOWN_PWM_STATE: NrgcpTypes.PwmState
    PWM_STATE_INACTIVE: NrgcpTypes.PwmState
    PWM_STATE_ACTIVE: NrgcpTypes.PwmState
    class RcdTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RCD_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_NO_VALUE_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_30MA_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_60MA_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_150MA_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_POS_6MA_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
        RCD_NEG_6MA_TRIGGER: _ClassVar[NrgcpTypes.RcdTrigger]
    UNKNOWN_RCD_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_NO_VALUE_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_30MA_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_60MA_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_150MA_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_POS_6MA_TRIGGER: NrgcpTypes.RcdTrigger
    RCD_NEG_6MA_TRIGGER: NrgcpTypes.RcdTrigger
    class RelayState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RELAY_STATE: _ClassVar[NrgcpTypes.RelayState]
        NO_RELAY: _ClassVar[NrgcpTypes.RelayState]
        N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L1_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L1_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L2_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L2_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L2_L1_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L2_L1_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L1_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L1_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L2_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L2_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L2_L1_RELAY: _ClassVar[NrgcpTypes.RelayState]
        L3_L2_L1_N_RELAY: _ClassVar[NrgcpTypes.RelayState]
    UNKNOWN_RELAY_STATE: NrgcpTypes.RelayState
    NO_RELAY: NrgcpTypes.RelayState
    N_RELAY: NrgcpTypes.RelayState
    L1_RELAY: NrgcpTypes.RelayState
    L1_N_RELAY: NrgcpTypes.RelayState
    L2_RELAY: NrgcpTypes.RelayState
    L2_N_RELAY: NrgcpTypes.RelayState
    L2_L1_RELAY: NrgcpTypes.RelayState
    L2_L1_N_RELAY: NrgcpTypes.RelayState
    L3_RELAY: NrgcpTypes.RelayState
    L3_N_RELAY: NrgcpTypes.RelayState
    L3_L1_RELAY: NrgcpTypes.RelayState
    L3_L1_N_RELAY: NrgcpTypes.RelayState
    L3_L2_RELAY: NrgcpTypes.RelayState
    L3_L2_N_RELAY: NrgcpTypes.RelayState
    L3_L2_L1_RELAY: NrgcpTypes.RelayState
    L3_L2_L1_N_RELAY: NrgcpTypes.RelayState
    class ResetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RESET_TYPE: _ClassVar[NrgcpTypes.ResetType]
        SOFT: _ClassVar[NrgcpTypes.ResetType]
    UNKNOWN_RESET_TYPE: NrgcpTypes.ResetType
    SOFT: NrgcpTypes.ResetType
    class RestartMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MODE: _ClassVar[NrgcpTypes.RestartMode]
        SMART_MODULE: _ClassVar[NrgcpTypes.RestartMode]
        MC_SOFT: _ClassVar[NrgcpTypes.RestartMode]
        MC_HARD: _ClassVar[NrgcpTypes.RestartMode]
        SMART_MODULE_MCS: _ClassVar[NrgcpTypes.RestartMode]
        SMART_MODULE_MCH: _ClassVar[NrgcpTypes.RestartMode]
    UNKNOWN_MODE: NrgcpTypes.RestartMode
    SMART_MODULE: NrgcpTypes.RestartMode
    MC_SOFT: NrgcpTypes.RestartMode
    MC_HARD: NrgcpTypes.RestartMode
    SMART_MODULE_MCS: NrgcpTypes.RestartMode
    SMART_MODULE_MCH: NrgcpTypes.RestartMode
    class SchukoState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SCHUKO_REV_POL: _ClassVar[NrgcpTypes.SchukoState]
        CORRECT_POLARITY: _ClassVar[NrgcpTypes.SchukoState]
        REVERSE_POLARITY: _ClassVar[NrgcpTypes.SchukoState]
    UNKNOWN_SCHUKO_REV_POL: NrgcpTypes.SchukoState
    CORRECT_POLARITY: NrgcpTypes.SchukoState
    REVERSE_POLARITY: NrgcpTypes.SchukoState
    class SelfTest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SELF_TEST: _ClassVar[NrgcpTypes.SelfTest]
        OK: _ClassVar[NrgcpTypes.SelfTest]
        NOK: _ClassVar[NrgcpTypes.SelfTest]
    UNKNOWN_SELF_TEST: NrgcpTypes.SelfTest
    OK: NrgcpTypes.SelfTest
    NOK: NrgcpTypes.SelfTest
    class TimeBasedChargingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TIME_BASED_CHARGING_STATUS: _ClassVar[NrgcpTypes.TimeBasedChargingState]
        CHARGE_TIME_BASED: _ClassVar[NrgcpTypes.TimeBasedChargingState]
        PAUSE_TIME_BASED_CHARGING: _ClassVar[NrgcpTypes.TimeBasedChargingState]
        SOLAR_TIME_BASED_CHARGING: _ClassVar[NrgcpTypes.TimeBasedChargingState]
    UNKNOWN_TIME_BASED_CHARGING_STATUS: NrgcpTypes.TimeBasedChargingState
    CHARGE_TIME_BASED: NrgcpTypes.TimeBasedChargingState
    PAUSE_TIME_BASED_CHARGING: NrgcpTypes.TimeBasedChargingState
    SOLAR_TIME_BASED_CHARGING: NrgcpTypes.TimeBasedChargingState
    class Timezone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TIMEZONE_TYPE: _ClassVar[NrgcpTypes.Timezone]
        IDLW_m12: _ClassVar[NrgcpTypes.Timezone]
        SST_m11: _ClassVar[NrgcpTypes.Timezone]
        HST_m10: _ClassVar[NrgcpTypes.Timezone]
        MIT_m9_30: _ClassVar[NrgcpTypes.Timezone]
        AKST_m9: _ClassVar[NrgcpTypes.Timezone]
        PST_m8: _ClassVar[NrgcpTypes.Timezone]
        MST_m7: _ClassVar[NrgcpTypes.Timezone]
        CST_m6: _ClassVar[NrgcpTypes.Timezone]
        EST_m5: _ClassVar[NrgcpTypes.Timezone]
        AST_m4: _ClassVar[NrgcpTypes.Timezone]
        NST_m3_30: _ClassVar[NrgcpTypes.Timezone]
        BRT_m3: _ClassVar[NrgcpTypes.Timezone]
        NDT_m2_30: _ClassVar[NrgcpTypes.Timezone]
        BRST_m2: _ClassVar[NrgcpTypes.Timezone]
        AZOT_m1: _ClassVar[NrgcpTypes.Timezone]
        GMT_0: _ClassVar[NrgcpTypes.Timezone]
        CET_p1: _ClassVar[NrgcpTypes.Timezone]
        CEST_p2: _ClassVar[NrgcpTypes.Timezone]
        EAT_p3: _ClassVar[NrgcpTypes.Timezone]
        IRST_p3_30: _ClassVar[NrgcpTypes.Timezone]
        GST_p4: _ClassVar[NrgcpTypes.Timezone]
        IRDT_p4_30: _ClassVar[NrgcpTypes.Timezone]
        PKT_p5: _ClassVar[NrgcpTypes.Timezone]
        IST_p5_30: _ClassVar[NrgcpTypes.Timezone]
        NPT_p5_45: _ClassVar[NrgcpTypes.Timezone]
        BIOT_p6: _ClassVar[NrgcpTypes.Timezone]
        MMT_p6_30: _ClassVar[NrgcpTypes.Timezone]
        THA_p7: _ClassVar[NrgcpTypes.Timezone]
        CT_p8: _ClassVar[NrgcpTypes.Timezone]
        CWST_p8_45: _ClassVar[NrgcpTypes.Timezone]
        JST_p9: _ClassVar[NrgcpTypes.Timezone]
        ACST_p9_30: _ClassVar[NrgcpTypes.Timezone]
        AEST_p10: _ClassVar[NrgcpTypes.Timezone]
        ACDT_p10_30: _ClassVar[NrgcpTypes.Timezone]
        AEDT_p11: _ClassVar[NrgcpTypes.Timezone]
        NZST_p12: _ClassVar[NrgcpTypes.Timezone]
        NZDT_p13: _ClassVar[NrgcpTypes.Timezone]
        CHADT_p13_45: _ClassVar[NrgcpTypes.Timezone]
        LINT_p14: _ClassVar[NrgcpTypes.Timezone]
        WET_0: _ClassVar[NrgcpTypes.Timezone]
        WEST_p1: _ClassVar[NrgcpTypes.Timezone]
    UNKNOWN_TIMEZONE_TYPE: NrgcpTypes.Timezone
    IDLW_m12: NrgcpTypes.Timezone
    SST_m11: NrgcpTypes.Timezone
    HST_m10: NrgcpTypes.Timezone
    MIT_m9_30: NrgcpTypes.Timezone
    AKST_m9: NrgcpTypes.Timezone
    PST_m8: NrgcpTypes.Timezone
    MST_m7: NrgcpTypes.Timezone
    CST_m6: NrgcpTypes.Timezone
    EST_m5: NrgcpTypes.Timezone
    AST_m4: NrgcpTypes.Timezone
    NST_m3_30: NrgcpTypes.Timezone
    BRT_m3: NrgcpTypes.Timezone
    NDT_m2_30: NrgcpTypes.Timezone
    BRST_m2: NrgcpTypes.Timezone
    AZOT_m1: NrgcpTypes.Timezone
    GMT_0: NrgcpTypes.Timezone
    CET_p1: NrgcpTypes.Timezone
    CEST_p2: NrgcpTypes.Timezone
    EAT_p3: NrgcpTypes.Timezone
    IRST_p3_30: NrgcpTypes.Timezone
    GST_p4: NrgcpTypes.Timezone
    IRDT_p4_30: NrgcpTypes.Timezone
    PKT_p5: NrgcpTypes.Timezone
    IST_p5_30: NrgcpTypes.Timezone
    NPT_p5_45: NrgcpTypes.Timezone
    BIOT_p6: NrgcpTypes.Timezone
    MMT_p6_30: NrgcpTypes.Timezone
    THA_p7: NrgcpTypes.Timezone
    CT_p8: NrgcpTypes.Timezone
    CWST_p8_45: NrgcpTypes.Timezone
    JST_p9: NrgcpTypes.Timezone
    ACST_p9_30: NrgcpTypes.Timezone
    AEST_p10: NrgcpTypes.Timezone
    ACDT_p10_30: NrgcpTypes.Timezone
    AEDT_p11: NrgcpTypes.Timezone
    NZST_p12: NrgcpTypes.Timezone
    NZDT_p13: NrgcpTypes.Timezone
    CHADT_p13_45: NrgcpTypes.Timezone
    LINT_p14: NrgcpTypes.Timezone
    WET_0: NrgcpTypes.Timezone
    WEST_p1: NrgcpTypes.Timezone
    class UnitSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_UNIT_SYSTEM: _ClassVar[NrgcpTypes.UnitSystem]
        METRIC: _ClassVar[NrgcpTypes.UnitSystem]
        IMPERIAL: _ClassVar[NrgcpTypes.UnitSystem]
    UNKNOWN_UNIT_SYSTEM: NrgcpTypes.UnitSystem
    METRIC: NrgcpTypes.UnitSystem
    IMPERIAL: NrgcpTypes.UnitSystem
    class WarningCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_WARNING_CODE: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_NO_WARNING: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_CHARGING_WITHOUT_PE: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_BLACKOUT_ACTIVE: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_HIGHTEMPERATURE_SYSTEM: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_HIGHTEMPERATURE_MAIN: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_HIGHTEMPERATURE_STAR: _ClassVar[NrgcpTypes.WarningCode]
        SYS_WARNING_CODE_HIGHTEMPERATURE_SCHUKO: _ClassVar[NrgcpTypes.WarningCode]
    UNKNOWN_WARNING_CODE: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_NO_WARNING: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_CHARGING_WITHOUT_PE: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_BLACKOUT_ACTIVE: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_HIGHTEMPERATURE_SYSTEM: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_HIGHTEMPERATURE_MAIN: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_HIGHTEMPERATURE_STAR: NrgcpTypes.WarningCode
    SYS_WARNING_CODE_HIGHTEMPERATURE_SCHUKO: NrgcpTypes.WarningCode
    class BatteryCapacity(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: float
        min: float
        value: float
        def __init__(self, max: _Optional[float] = ..., min: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    class Cellular(_message.Message):
        __slots__ = ("imei", "imsi", "oper", "rssi", "signalStrength", "swRev")
        IMEI_FIELD_NUMBER: _ClassVar[int]
        IMSI_FIELD_NUMBER: _ClassVar[int]
        OPER_FIELD_NUMBER: _ClassVar[int]
        RSSI_FIELD_NUMBER: _ClassVar[int]
        SIGNALSTRENGTH_FIELD_NUMBER: _ClassVar[int]
        SWREV_FIELD_NUMBER: _ClassVar[int]
        imei: bytes
        imsi: bytes
        oper: bytes
        rssi: int
        signalStrength: int
        swRev: bytes
        def __init__(self, imei: _Optional[bytes] = ..., imsi: _Optional[bytes] = ..., oper: _Optional[bytes] = ..., rssi: _Optional[int] = ..., signalStrength: _Optional[int] = ..., swRev: _Optional[bytes] = ...) -> None: ...
    class Consumption(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: float
        min: float
        value: float
        def __init__(self, max: _Optional[float] = ..., min: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    class Currency(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: int
        min: int
        value: str
        def __init__(self, max: _Optional[int] = ..., min: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Efficacy(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: float
        min: float
        value: float
        def __init__(self, max: _Optional[float] = ..., min: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    class GPS(_message.Message):
        __slots__ = ("hpa", "latitude", "longitude", "state", "timestamp", "vpa")
        HPA_FIELD_NUMBER: _ClassVar[int]
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        VPA_FIELD_NUMBER: _ClassVar[int]
        hpa: float
        latitude: float
        longitude: float
        state: int
        timestamp: int
        vpa: float
        def __init__(self, hpa: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., state: _Optional[int] = ..., timestamp: _Optional[int] = ..., vpa: _Optional[float] = ...) -> None: ...
    class PricePerKwh(_message.Message):
        __slots__ = ("max", "min", "value")
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        max: float
        min: float
        value: float
        def __init__(self, max: _Optional[float] = ..., min: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    class TimeBasedChargingEvent(_message.Message):
        __slots__ = ("chargeCurrent", "chargingType", "energyLimit", "time", "unlimitedCharging", "profileId")
        class ChargingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_CHARGING_TYPE: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.ChargingType]
            CHARGE: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.ChargingType]
            PAUSE: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.ChargingType]
            SOLAR: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.ChargingType]
        UNKNOWN_CHARGING_TYPE: NrgcpTypes.TimeBasedChargingEvent.ChargingType
        CHARGE: NrgcpTypes.TimeBasedChargingEvent.ChargingType
        PAUSE: NrgcpTypes.TimeBasedChargingEvent.ChargingType
        SOLAR: NrgcpTypes.TimeBasedChargingEvent.ChargingType
        class TimeBasedChargingUnlimited(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TIME_BASED_CHARGING_VALUE: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited]
            LIMITED: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited]
            UNLIMITED: _ClassVar[NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited]
        UNKNOWN_TIME_BASED_CHARGING_VALUE: NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited
        LIMITED: NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited
        UNLIMITED: NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited
        CHARGECURRENT_FIELD_NUMBER: _ClassVar[int]
        CHARGINGTYPE_FIELD_NUMBER: _ClassVar[int]
        ENERGYLIMIT_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        UNLIMITEDCHARGING_FIELD_NUMBER: _ClassVar[int]
        PROFILEID_FIELD_NUMBER: _ClassVar[int]
        chargeCurrent: float
        chargingType: NrgcpTypes.TimeBasedChargingEvent.ChargingType
        energyLimit: float
        time: int
        unlimitedCharging: NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited
        profileId: int
        def __init__(self, chargeCurrent: _Optional[float] = ..., chargingType: _Optional[_Union[NrgcpTypes.TimeBasedChargingEvent.ChargingType, str]] = ..., energyLimit: _Optional[float] = ..., time: _Optional[int] = ..., unlimitedCharging: _Optional[_Union[NrgcpTypes.TimeBasedChargingEvent.TimeBasedChargingUnlimited, str]] = ..., profileId: _Optional[int] = ...) -> None: ...
    class WifiLocation(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class NrgcpWifiTypes(_message.Message):
    __slots__ = ()
    class WifiApRecordProto(_message.Message):
        __slots__ = ("ant", "authmode", "bssid", "country", "groupCipher", "pairwiseCipher", "phy11B", "phy11G", "phy11N", "phyLr", "primary", "reserved", "rssi", "second", "ssid", "wps")
        class WifiCountry(_message.Message):
            __slots__ = ("cc", "maxTxPower", "nchan", "policy", "schan")
            CC_FIELD_NUMBER: _ClassVar[int]
            MAXTXPOWER_FIELD_NUMBER: _ClassVar[int]
            NCHAN_FIELD_NUMBER: _ClassVar[int]
            POLICY_FIELD_NUMBER: _ClassVar[int]
            SCHAN_FIELD_NUMBER: _ClassVar[int]
            cc: str
            maxTxPower: int
            nchan: int
            policy: int
            schan: int
            def __init__(self, cc: _Optional[str] = ..., maxTxPower: _Optional[int] = ..., nchan: _Optional[int] = ..., policy: _Optional[int] = ..., schan: _Optional[int] = ...) -> None: ...
        ANT_FIELD_NUMBER: _ClassVar[int]
        AUTHMODE_FIELD_NUMBER: _ClassVar[int]
        BSSID_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        GROUPCIPHER_FIELD_NUMBER: _ClassVar[int]
        PAIRWISECIPHER_FIELD_NUMBER: _ClassVar[int]
        PHY11B_FIELD_NUMBER: _ClassVar[int]
        PHY11G_FIELD_NUMBER: _ClassVar[int]
        PHY11N_FIELD_NUMBER: _ClassVar[int]
        PHYLR_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        RESERVED_FIELD_NUMBER: _ClassVar[int]
        RSSI_FIELD_NUMBER: _ClassVar[int]
        SECOND_FIELD_NUMBER: _ClassVar[int]
        SSID_FIELD_NUMBER: _ClassVar[int]
        WPS_FIELD_NUMBER: _ClassVar[int]
        ant: int
        authmode: int
        bssid: str
        country: NrgcpWifiTypes.WifiApRecordProto.WifiCountry
        groupCipher: int
        pairwiseCipher: int
        phy11B: bool
        phy11G: bool
        phy11N: bool
        phyLr: bool
        primary: int
        reserved: int
        rssi: int
        second: int
        ssid: str
        wps: bool
        def __init__(self, ant: _Optional[int] = ..., authmode: _Optional[int] = ..., bssid: _Optional[str] = ..., country: _Optional[_Union[NrgcpWifiTypes.WifiApRecordProto.WifiCountry, _Mapping]] = ..., groupCipher: _Optional[int] = ..., pairwiseCipher: _Optional[int] = ..., phy11B: bool = ..., phy11G: bool = ..., phy11N: bool = ..., phyLr: bool = ..., primary: _Optional[int] = ..., reserved: _Optional[int] = ..., rssi: _Optional[int] = ..., second: _Optional[int] = ..., ssid: _Optional[str] = ..., wps: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class NrgcpSolarchargingTypes(_message.Message):
    __slots__ = ()
    class ApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        JSON_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        XML_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_0_0_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_0_1_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_0_2_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_1_0_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_1_1_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_1_2_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_2_0_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_2_1_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        MODBUS_SUB_2_2_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        DXS_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
        UDP_API_TYPE: _ClassVar[NrgcpSolarchargingTypes.ApiType]
    UNKNOWN_API_TYPE: NrgcpSolarchargingTypes.ApiType
    JSON_API_TYPE: NrgcpSolarchargingTypes.ApiType
    XML_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_0_0_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_0_1_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_0_2_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_1_0_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_1_1_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_1_2_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_2_0_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_2_1_API_TYPE: NrgcpSolarchargingTypes.ApiType
    MODBUS_SUB_2_2_API_TYPE: NrgcpSolarchargingTypes.ApiType
    DXS_API_TYPE: NrgcpSolarchargingTypes.ApiType
    UDP_API_TYPE: NrgcpSolarchargingTypes.ApiType
    class BrandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        DEMO: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        FRONIUS: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        SMA: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        KOSTAL: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        SOLAREDGE: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        MYPV: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        MEC: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        CUSTOM: _ClassVar[NrgcpSolarchargingTypes.BrandType]
        HUAWEI: _ClassVar[NrgcpSolarchargingTypes.BrandType]
    UNKNOWN_TYPE: NrgcpSolarchargingTypes.BrandType
    DEMO: NrgcpSolarchargingTypes.BrandType
    FRONIUS: NrgcpSolarchargingTypes.BrandType
    SMA: NrgcpSolarchargingTypes.BrandType
    KOSTAL: NrgcpSolarchargingTypes.BrandType
    SOLAREDGE: NrgcpSolarchargingTypes.BrandType
    MYPV: NrgcpSolarchargingTypes.BrandType
    MEC: NrgcpSolarchargingTypes.BrandType
    CUSTOM: NrgcpSolarchargingTypes.BrandType
    HUAWEI: NrgcpSolarchargingTypes.BrandType
    class ChargeMinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIN_CHARGING_NEVER: _ClassVar[NrgcpSolarchargingTypes.ChargeMinType]
        MIN_CHARGING_SELECTIVE_WITHOUT_SUP_LIMIT: _ClassVar[NrgcpSolarchargingTypes.ChargeMinType]
        MIN_CHARGING_ALWAYS_WITHOUT_SUP_LIMIT: _ClassVar[NrgcpSolarchargingTypes.ChargeMinType]
        MIN_CHARGING_SELECTIVE_WITH_SUP_LIMIT: _ClassVar[NrgcpSolarchargingTypes.ChargeMinType]
        MIN_CHARGING_ALWAYS_WITH_SUP_LIMIT: _ClassVar[NrgcpSolarchargingTypes.ChargeMinType]
    MIN_CHARGING_NEVER: NrgcpSolarchargingTypes.ChargeMinType
    MIN_CHARGING_SELECTIVE_WITHOUT_SUP_LIMIT: NrgcpSolarchargingTypes.ChargeMinType
    MIN_CHARGING_ALWAYS_WITHOUT_SUP_LIMIT: NrgcpSolarchargingTypes.ChargeMinType
    MIN_CHARGING_SELECTIVE_WITH_SUP_LIMIT: NrgcpSolarchargingTypes.ChargeMinType
    MIN_CHARGING_ALWAYS_WITH_SUP_LIMIT: NrgcpSolarchargingTypes.ChargeMinType
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_TYPE_DATAMANAGER: _ClassVar[NrgcpSolarchargingTypes.DeviceType]
        DEVICE_TYPE_INVERTER: _ClassVar[NrgcpSolarchargingTypes.DeviceType]
        DEVICE_TYPE_ENERGY_METER: _ClassVar[NrgcpSolarchargingTypes.DeviceType]
        DEVICE_TYPE_BATTERY: _ClassVar[NrgcpSolarchargingTypes.DeviceType]
        DEVICE_TYPE_SMART_LOAD: _ClassVar[NrgcpSolarchargingTypes.DeviceType]
    DEVICE_TYPE_DATAMANAGER: NrgcpSolarchargingTypes.DeviceType
    DEVICE_TYPE_INVERTER: NrgcpSolarchargingTypes.DeviceType
    DEVICE_TYPE_ENERGY_METER: NrgcpSolarchargingTypes.DeviceType
    DEVICE_TYPE_BATTERY: NrgcpSolarchargingTypes.DeviceType
    DEVICE_TYPE_SMART_LOAD: NrgcpSolarchargingTypes.DeviceType
    class MeterLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EM_LOCATION_UNKNOWN: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
        EM_LOCATION_GRID: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
        EM_LOCATION_LOAD: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
        EM_LOCATION_AC_GENERATOR: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
        EM_LOCATION_AC_GENERATOR_WITH_BAT: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
        EM_LOCATION_SUB_DEVICE: _ClassVar[NrgcpSolarchargingTypes.MeterLocation]
    EM_LOCATION_UNKNOWN: NrgcpSolarchargingTypes.MeterLocation
    EM_LOCATION_GRID: NrgcpSolarchargingTypes.MeterLocation
    EM_LOCATION_LOAD: NrgcpSolarchargingTypes.MeterLocation
    EM_LOCATION_AC_GENERATOR: NrgcpSolarchargingTypes.MeterLocation
    EM_LOCATION_AC_GENERATOR_WITH_BAT: NrgcpSolarchargingTypes.MeterLocation
    EM_LOCATION_SUB_DEVICE: NrgcpSolarchargingTypes.MeterLocation
    class PhaseSwitchExtTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHASE_SWITCH_EXT_TYPE_DISABLED: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchExtTypes]
        PHASE_SWITCH_EXT_TYPE_DELAY: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchExtTypes]
        PHASE_SWITCH_EXT_TYPE_DELAY_WITH_LIMIT: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchExtTypes]
        PHASE_SWITCH_EXT_TYPE_CUSTOM: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchExtTypes]
    PHASE_SWITCH_EXT_TYPE_DISABLED: NrgcpSolarchargingTypes.PhaseSwitchExtTypes
    PHASE_SWITCH_EXT_TYPE_DELAY: NrgcpSolarchargingTypes.PhaseSwitchExtTypes
    PHASE_SWITCH_EXT_TYPE_DELAY_WITH_LIMIT: NrgcpSolarchargingTypes.PhaseSwitchExtTypes
    PHASE_SWITCH_EXT_TYPE_CUSTOM: NrgcpSolarchargingTypes.PhaseSwitchExtTypes
    class PhaseSwitchTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHASE_SWITCH_TYPE_MANUAL: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchTypes]
        PHASE_SWITCH_TYPE_AUTOMATIC: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchTypes]
        PHASE_SWITCH_TYPE_MIN_CURRENT_MAX_PHASES: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchTypes]
        PHASE_SWITCH_TYPE_MAX_CURRENT_MIN_PHASES: _ClassVar[NrgcpSolarchargingTypes.PhaseSwitchTypes]
    PHASE_SWITCH_TYPE_MANUAL: NrgcpSolarchargingTypes.PhaseSwitchTypes
    PHASE_SWITCH_TYPE_AUTOMATIC: NrgcpSolarchargingTypes.PhaseSwitchTypes
    PHASE_SWITCH_TYPE_MIN_CURRENT_MAX_PHASES: NrgcpSolarchargingTypes.PhaseSwitchTypes
    PHASE_SWITCH_TYPE_MAX_CURRENT_MIN_PHASES: NrgcpSolarchargingTypes.PhaseSwitchTypes
    class PingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PING_ALL_DEVICES: _ClassVar[NrgcpSolarchargingTypes.PingType]
        PING_INV: _ClassVar[NrgcpSolarchargingTypes.PingType]
        PING_EM: _ClassVar[NrgcpSolarchargingTypes.PingType]
        PING_BAT: _ClassVar[NrgcpSolarchargingTypes.PingType]
        PING_SL: _ClassVar[NrgcpSolarchargingTypes.PingType]
    PING_ALL_DEVICES: NrgcpSolarchargingTypes.PingType
    PING_INV: NrgcpSolarchargingTypes.PingType
    PING_EM: NrgcpSolarchargingTypes.PingType
    PING_BAT: NrgcpSolarchargingTypes.PingType
    PING_SL: NrgcpSolarchargingTypes.PingType
    class Priorities(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_NONE: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_SMART_DEVICES: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_BATTERY: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_NRGKICK_25: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_NRGKICK_50: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_NRGKICK_75: _ClassVar[NrgcpSolarchargingTypes.Priorities]
        PRIORITY_NRGKICK: _ClassVar[NrgcpSolarchargingTypes.Priorities]
    PRIORITY_NONE: NrgcpSolarchargingTypes.Priorities
    PRIORITY_SMART_DEVICES: NrgcpSolarchargingTypes.Priorities
    PRIORITY_BATTERY: NrgcpSolarchargingTypes.Priorities
    PRIORITY_NRGKICK_25: NrgcpSolarchargingTypes.Priorities
    PRIORITY_NRGKICK_50: NrgcpSolarchargingTypes.Priorities
    PRIORITY_NRGKICK_75: NrgcpSolarchargingTypes.Priorities
    PRIORITY_NRGKICK: NrgcpSolarchargingTypes.Priorities
    class SolarChargingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOLAR_SERVICE_STATE_UNKNOWN: _ClassVar[NrgcpSolarchargingTypes.SolarChargingState]
        SOLAR_SERVICE_STATE_ENABLED: _ClassVar[NrgcpSolarchargingTypes.SolarChargingState]
        SOLAR_SERVICE_STATE_DISABLED: _ClassVar[NrgcpSolarchargingTypes.SolarChargingState]
    SOLAR_SERVICE_STATE_UNKNOWN: NrgcpSolarchargingTypes.SolarChargingState
    SOLAR_SERVICE_STATE_ENABLED: NrgcpSolarchargingTypes.SolarChargingState
    SOLAR_SERVICE_STATE_DISABLED: NrgcpSolarchargingTypes.SolarChargingState
    class SolarStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STRATEGY: _ClassVar[NrgcpSolarchargingTypes.SolarStrategyType]
        SURPLUS_STRATEGY: _ClassVar[NrgcpSolarchargingTypes.SolarStrategyType]
        HUNDRED_PERCENT_STRATEGY: _ClassVar[NrgcpSolarchargingTypes.SolarStrategyType]
        FEED_IN_LIMIT_STRATEGY: _ClassVar[NrgcpSolarchargingTypes.SolarStrategyType]
    UNKNOWN_STRATEGY: NrgcpSolarchargingTypes.SolarStrategyType
    SURPLUS_STRATEGY: NrgcpSolarchargingTypes.SolarStrategyType
    HUNDRED_PERCENT_STRATEGY: NrgcpSolarchargingTypes.SolarStrategyType
    FEED_IN_LIMIT_STRATEGY: NrgcpSolarchargingTypes.SolarStrategyType
    class SupportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUPPORT_EXTERNAL_POWER: _ClassVar[NrgcpSolarchargingTypes.SupportType]
        SUPPORT_GRID_GRID_POWER: _ClassVar[NrgcpSolarchargingTypes.SupportType]
    SUPPORT_EXTERNAL_POWER: NrgcpSolarchargingTypes.SupportType
    SUPPORT_GRID_GRID_POWER: NrgcpSolarchargingTypes.SupportType
    class AuthSettings(_message.Message):
        __slots__ = ("pw", "username")
        PW_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        pw: str
        username: str
        def __init__(self, pw: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...
    class BatteryFailInfo(_message.Message):
        __slots__ = ("id", "uniqueId")
        ID_FIELD_NUMBER: _ClassVar[int]
        UNIQUEID_FIELD_NUMBER: _ClassVar[int]
        id: int
        uniqueId: str
        def __init__(self, id: _Optional[int] = ..., uniqueId: _Optional[str] = ...) -> None: ...
    class BatteryInfo(_message.Message):
        __slots__ = ("deviceInfo", "maxCapacityWh")
        DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
        MAXCAPACITYWH_FIELD_NUMBER: _ClassVar[int]
        deviceInfo: NrgcpSolarchargingTypes.DeviceInfo
        maxCapacityWh: int
        def __init__(self, deviceInfo: _Optional[_Union[NrgcpSolarchargingTypes.DeviceInfo, _Mapping]] = ..., maxCapacityWh: _Optional[int] = ...) -> None: ...
    class BatterySocSettings(_message.Message):
        __slots__ = ("considerMaxBatPower", "enabled", "maxBatChargePower", "maxSoc", "minSoc")
        CONSIDERMAXBATPOWER_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MAXBATCHARGEPOWER_FIELD_NUMBER: _ClassVar[int]
        MAXSOC_FIELD_NUMBER: _ClassVar[int]
        MINSOC_FIELD_NUMBER: _ClassVar[int]
        considerMaxBatPower: bool
        enabled: bool
        maxBatChargePower: int
        maxSoc: int
        minSoc: int
        def __init__(self, considerMaxBatPower: bool = ..., enabled: bool = ..., maxBatChargePower: _Optional[int] = ..., maxSoc: _Optional[int] = ..., minSoc: _Optional[int] = ...) -> None: ...
    class ChargeMinSettings(_message.Message):
        __slots__ = ("chargeMinType", "maxBatDischargeW", "maxSupportW", "supportType")
        CHARGEMINTYPE_FIELD_NUMBER: _ClassVar[int]
        MAXBATDISCHARGEW_FIELD_NUMBER: _ClassVar[int]
        MAXSUPPORTW_FIELD_NUMBER: _ClassVar[int]
        SUPPORTTYPE_FIELD_NUMBER: _ClassVar[int]
        chargeMinType: NrgcpSolarchargingTypes.ChargeMinType
        maxBatDischargeW: int
        maxSupportW: int
        supportType: NrgcpSolarchargingTypes.SupportType
        def __init__(self, chargeMinType: _Optional[_Union[NrgcpSolarchargingTypes.ChargeMinType, str]] = ..., maxBatDischargeW: _Optional[int] = ..., maxSupportW: _Optional[int] = ..., supportType: _Optional[_Union[NrgcpSolarchargingTypes.SupportType, str]] = ...) -> None: ...
    class DeviceFailInfo(_message.Message):
        __slots__ = ("batFail", "emFail", "invFail", "slFail")
        BATFAIL_FIELD_NUMBER: _ClassVar[int]
        EMFAIL_FIELD_NUMBER: _ClassVar[int]
        INVFAIL_FIELD_NUMBER: _ClassVar[int]
        SLFAIL_FIELD_NUMBER: _ClassVar[int]
        batFail: NrgcpSolarchargingTypes.BatteryFailInfo
        emFail: NrgcpSolarchargingTypes.EnergyMeterFailInfo
        invFail: NrgcpSolarchargingTypes.InverterFailInfo
        slFail: NrgcpSolarchargingTypes.SmartLoadFailInfo
        def __init__(self, batFail: _Optional[_Union[NrgcpSolarchargingTypes.BatteryFailInfo, _Mapping]] = ..., emFail: _Optional[_Union[NrgcpSolarchargingTypes.EnergyMeterFailInfo, _Mapping]] = ..., invFail: _Optional[_Union[NrgcpSolarchargingTypes.InverterFailInfo, _Mapping]] = ..., slFail: _Optional[_Union[NrgcpSolarchargingTypes.SmartLoadFailInfo, _Mapping]] = ...) -> None: ...
    class DeviceInfo(_message.Message):
        __slots__ = ("apiType", "authSettings", "deviceType", "host", "id", "mac", "model", "name", "port", "type", "uniqueId")
        APITYPE_FIELD_NUMBER: _ClassVar[int]
        AUTHSETTINGS_FIELD_NUMBER: _ClassVar[int]
        DEVICETYPE_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MAC_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNIQUEID_FIELD_NUMBER: _ClassVar[int]
        apiType: NrgcpSolarchargingTypes.ApiType
        authSettings: NrgcpSolarchargingTypes.AuthSettings
        deviceType: NrgcpSolarchargingTypes.DeviceType
        host: str
        id: int
        mac: str
        model: str
        name: str
        port: int
        type: NrgcpSolarchargingTypes.BrandType
        uniqueId: str
        def __init__(self, apiType: _Optional[_Union[NrgcpSolarchargingTypes.ApiType, str]] = ..., authSettings: _Optional[_Union[NrgcpSolarchargingTypes.AuthSettings, _Mapping]] = ..., deviceType: _Optional[_Union[NrgcpSolarchargingTypes.DeviceType, str]] = ..., host: _Optional[str] = ..., id: _Optional[int] = ..., mac: _Optional[str] = ..., model: _Optional[str] = ..., name: _Optional[str] = ..., port: _Optional[int] = ..., type: _Optional[_Union[NrgcpSolarchargingTypes.BrandType, str]] = ..., uniqueId: _Optional[str] = ...) -> None: ...
    class DevicePing(_message.Message):
        __slots__ = ("batInfo", "emInfo", "invInfo", "requestInfo", "slInfo")
        BATINFO_FIELD_NUMBER: _ClassVar[int]
        EMINFO_FIELD_NUMBER: _ClassVar[int]
        INVINFO_FIELD_NUMBER: _ClassVar[int]
        REQUESTINFO_FIELD_NUMBER: _ClassVar[int]
        SLINFO_FIELD_NUMBER: _ClassVar[int]
        batInfo: NrgcpSolarchargingTypes.BatteryInfo
        emInfo: NrgcpSolarchargingTypes.EnergyMeterInfo
        invInfo: NrgcpSolarchargingTypes.SolarInverterInfo
        requestInfo: NrgcpSolarchargingTypes.RequestInfo
        slInfo: NrgcpSolarchargingTypes.SmartLoadInfo
        def __init__(self, batInfo: _Optional[_Union[NrgcpSolarchargingTypes.BatteryInfo, _Mapping]] = ..., emInfo: _Optional[_Union[NrgcpSolarchargingTypes.EnergyMeterInfo, _Mapping]] = ..., invInfo: _Optional[_Union[NrgcpSolarchargingTypes.SolarInverterInfo, _Mapping]] = ..., requestInfo: _Optional[_Union[NrgcpSolarchargingTypes.RequestInfo, _Mapping]] = ..., slInfo: _Optional[_Union[NrgcpSolarchargingTypes.SmartLoadInfo, _Mapping]] = ...) -> None: ...
    class DynamicPeakManagerSettings(_message.Message):
        __slots__ = ("enabled", "type")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        type: int
        def __init__(self, enabled: bool = ..., type: _Optional[int] = ...) -> None: ...
    class EnergyMeterData(_message.Message):
        __slots__ = ("gridPowerW",)
        GRIDPOWERW_FIELD_NUMBER: _ClassVar[int]
        gridPowerW: int
        def __init__(self, gridPowerW: _Optional[int] = ...) -> None: ...
    class EnergyMeterFailInfo(_message.Message):
        __slots__ = ("id", "uniqueId")
        ID_FIELD_NUMBER: _ClassVar[int]
        UNIQUEID_FIELD_NUMBER: _ClassVar[int]
        id: int
        uniqueId: str
        def __init__(self, id: _Optional[int] = ..., uniqueId: _Optional[str] = ...) -> None: ...
    class EnergyMeterInfo(_message.Message):
        __slots__ = ("deviceInfo", "isInverted", "measureWithoutPnrgkick", "meterLocation")
        DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
        ISINVERTED_FIELD_NUMBER: _ClassVar[int]
        MEASUREWITHOUTPNRGKICK_FIELD_NUMBER: _ClassVar[int]
        METERLOCATION_FIELD_NUMBER: _ClassVar[int]
        deviceInfo: NrgcpSolarchargingTypes.DeviceInfo
        isInverted: bool
        measureWithoutPnrgkick: bool
        meterLocation: NrgcpSolarchargingTypes.MeterLocation
        def __init__(self, deviceInfo: _Optional[_Union[NrgcpSolarchargingTypes.DeviceInfo, _Mapping]] = ..., isInverted: bool = ..., measureWithoutPnrgkick: bool = ..., meterLocation: _Optional[_Union[NrgcpSolarchargingTypes.MeterLocation, str]] = ...) -> None: ...
    class FullScanInfo(_message.Message):
        __slots__ = ("batInfos", "brandType", "deviceType", "emInfos", "host", "invInfos", "mac", "pingResult", "port", "slInfos")
        class PingResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PING_SUCCESS: _ClassVar[NrgcpSolarchargingTypes.FullScanInfo.PingResult]
            PING_API_DISABLED: _ClassVar[NrgcpSolarchargingTypes.FullScanInfo.PingResult]
            PING_NOT_REACHABLE: _ClassVar[NrgcpSolarchargingTypes.FullScanInfo.PingResult]
        PING_SUCCESS: NrgcpSolarchargingTypes.FullScanInfo.PingResult
        PING_API_DISABLED: NrgcpSolarchargingTypes.FullScanInfo.PingResult
        PING_NOT_REACHABLE: NrgcpSolarchargingTypes.FullScanInfo.PingResult
        BATINFOS_FIELD_NUMBER: _ClassVar[int]
        BRANDTYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICETYPE_FIELD_NUMBER: _ClassVar[int]
        EMINFOS_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        INVINFOS_FIELD_NUMBER: _ClassVar[int]
        MAC_FIELD_NUMBER: _ClassVar[int]
        PINGRESULT_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        SLINFOS_FIELD_NUMBER: _ClassVar[int]
        batInfos: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.BatteryInfo]
        brandType: NrgcpSolarchargingTypes.BrandType
        deviceType: NrgcpSolarchargingTypes.DeviceType
        emInfos: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.EnergyMeterInfo]
        host: str
        invInfos: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SolarInverterInfo]
        mac: str
        pingResult: NrgcpSolarchargingTypes.FullScanInfo.PingResult
        port: int
        slInfos: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SmartLoadInfo]
        def __init__(self, batInfos: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.BatteryInfo, _Mapping]]] = ..., brandType: _Optional[_Union[NrgcpSolarchargingTypes.BrandType, str]] = ..., deviceType: _Optional[_Union[NrgcpSolarchargingTypes.DeviceType, str]] = ..., emInfos: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.EnergyMeterInfo, _Mapping]]] = ..., host: _Optional[str] = ..., invInfos: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SolarInverterInfo, _Mapping]]] = ..., mac: _Optional[str] = ..., pingResult: _Optional[_Union[NrgcpSolarchargingTypes.FullScanInfo.PingResult, str]] = ..., port: _Optional[int] = ..., slInfos: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SmartLoadInfo, _Mapping]]] = ...) -> None: ...
    class GridSettings(_message.Message):
        __slots__ = ("autoGridOffset", "gridOffsetW", "perPhaseOffset")
        AUTOGRIDOFFSET_FIELD_NUMBER: _ClassVar[int]
        GRIDOFFSETW_FIELD_NUMBER: _ClassVar[int]
        PERPHASEOFFSET_FIELD_NUMBER: _ClassVar[int]
        autoGridOffset: bool
        gridOffsetW: int
        perPhaseOffset: bool
        def __init__(self, autoGridOffset: bool = ..., gridOffsetW: _Optional[int] = ..., perPhaseOffset: bool = ...) -> None: ...
    class HoldTimings(_message.Message):
        __slots__ = ("holdOffTimeS", "holdOnTimeS")
        HOLDOFFTIMES_FIELD_NUMBER: _ClassVar[int]
        HOLDONTIMES_FIELD_NUMBER: _ClassVar[int]
        holdOffTimeS: int
        holdOnTimeS: int
        def __init__(self, holdOffTimeS: _Optional[int] = ..., holdOnTimeS: _Optional[int] = ...) -> None: ...
    class InverterFailInfo(_message.Message):
        __slots__ = ("id", "uniqueId")
        ID_FIELD_NUMBER: _ClassVar[int]
        UNIQUEID_FIELD_NUMBER: _ClassVar[int]
        id: int
        uniqueId: str
        def __init__(self, id: _Optional[int] = ..., uniqueId: _Optional[str] = ...) -> None: ...
    class PhaseSwitchSettings(_message.Message):
        __slots__ = ("allowedPhasesMask", "enabled", "extOptions", "fastSwitchThresholdDown", "fastSwitchThresholdUp", "reSwitchDelay", "supportiveBehaviour", "switchDelayDown", "switchDelayUp", "type")
        ALLOWEDPHASESMASK_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        EXTOPTIONS_FIELD_NUMBER: _ClassVar[int]
        FASTSWITCHTHRESHOLDDOWN_FIELD_NUMBER: _ClassVar[int]
        FASTSWITCHTHRESHOLDUP_FIELD_NUMBER: _ClassVar[int]
        RESWITCHDELAY_FIELD_NUMBER: _ClassVar[int]
        SUPPORTIVEBEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
        SWITCHDELAYDOWN_FIELD_NUMBER: _ClassVar[int]
        SWITCHDELAYUP_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        allowedPhasesMask: int
        enabled: bool
        extOptions: NrgcpSolarchargingTypes.PhaseSwitchExtTypes
        fastSwitchThresholdDown: int
        fastSwitchThresholdUp: int
        reSwitchDelay: int
        supportiveBehaviour: int
        switchDelayDown: int
        switchDelayUp: int
        type: NrgcpSolarchargingTypes.PhaseSwitchTypes
        def __init__(self, allowedPhasesMask: _Optional[int] = ..., enabled: bool = ..., extOptions: _Optional[_Union[NrgcpSolarchargingTypes.PhaseSwitchExtTypes, str]] = ..., fastSwitchThresholdDown: _Optional[int] = ..., fastSwitchThresholdUp: _Optional[int] = ..., reSwitchDelay: _Optional[int] = ..., supportiveBehaviour: _Optional[int] = ..., switchDelayDown: _Optional[int] = ..., switchDelayUp: _Optional[int] = ..., type: _Optional[_Union[NrgcpSolarchargingTypes.PhaseSwitchTypes, str]] = ...) -> None: ...
    class RequestInfo(_message.Message):
        __slots__ = ("apiType", "authPw", "authUser", "brandType", "host", "pingType", "port", "unitId")
        APITYPE_FIELD_NUMBER: _ClassVar[int]
        AUTHPW_FIELD_NUMBER: _ClassVar[int]
        AUTHUSER_FIELD_NUMBER: _ClassVar[int]
        BRANDTYPE_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        PINGTYPE_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        UNITID_FIELD_NUMBER: _ClassVar[int]
        apiType: NrgcpSolarchargingTypes.ApiType
        authPw: str
        authUser: str
        brandType: NrgcpSolarchargingTypes.BrandType
        host: str
        pingType: NrgcpSolarchargingTypes.PingType
        port: int
        unitId: int
        def __init__(self, apiType: _Optional[_Union[NrgcpSolarchargingTypes.ApiType, str]] = ..., authPw: _Optional[str] = ..., authUser: _Optional[str] = ..., brandType: _Optional[_Union[NrgcpSolarchargingTypes.BrandType, str]] = ..., host: _Optional[str] = ..., pingType: _Optional[_Union[NrgcpSolarchargingTypes.PingType, str]] = ..., port: _Optional[int] = ..., unitId: _Optional[int] = ...) -> None: ...
    class SmartLoadData(_message.Message):
        __slots__ = ("slPowerW", "slTemp")
        SLPOWERW_FIELD_NUMBER: _ClassVar[int]
        SLTEMP_FIELD_NUMBER: _ClassVar[int]
        slPowerW: int
        slTemp: float
        def __init__(self, slPowerW: _Optional[int] = ..., slTemp: _Optional[float] = ...) -> None: ...
    class SmartLoadFailInfo(_message.Message):
        __slots__ = ("id", "uniqueId")
        ID_FIELD_NUMBER: _ClassVar[int]
        UNIQUEID_FIELD_NUMBER: _ClassVar[int]
        id: int
        uniqueId: str
        def __init__(self, id: _Optional[int] = ..., uniqueId: _Optional[str] = ...) -> None: ...
    class SmartLoadInfo(_message.Message):
        __slots__ = ("deviceInfo",)
        DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
        deviceInfo: NrgcpSolarchargingTypes.DeviceInfo
        def __init__(self, deviceInfo: _Optional[_Union[NrgcpSolarchargingTypes.DeviceInfo, _Mapping]] = ...) -> None: ...
    class SmartLoadTempSettings(_message.Message):
        __slots__ = ("considerMaxSlPower", "enabled", "maxSlPower", "maxTemp", "minTemp")
        CONSIDERMAXSLPOWER_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MAXSLPOWER_FIELD_NUMBER: _ClassVar[int]
        MAXTEMP_FIELD_NUMBER: _ClassVar[int]
        MINTEMP_FIELD_NUMBER: _ClassVar[int]
        considerMaxSlPower: bool
        enabled: bool
        maxSlPower: int
        maxTemp: int
        minTemp: int
        def __init__(self, considerMaxSlPower: bool = ..., enabled: bool = ..., maxSlPower: _Optional[int] = ..., maxTemp: _Optional[int] = ..., minTemp: _Optional[int] = ...) -> None: ...
    class SolarBatteryData(_message.Message):
        __slots__ = ("batPowerW", "batSoc")
        BATPOWERW_FIELD_NUMBER: _ClassVar[int]
        BATSOC_FIELD_NUMBER: _ClassVar[int]
        batPowerW: int
        batSoc: float
        def __init__(self, batPowerW: _Optional[int] = ..., batSoc: _Optional[float] = ...) -> None: ...
    class SolarInverterData(_message.Message):
        __slots__ = ("energyWhDay", "powerW")
        ENERGYWHDAY_FIELD_NUMBER: _ClassVar[int]
        POWERW_FIELD_NUMBER: _ClassVar[int]
        energyWhDay: int
        powerW: int
        def __init__(self, energyWhDay: _Optional[int] = ..., powerW: _Optional[int] = ...) -> None: ...
    class SolarInverterInfo(_message.Message):
        __slots__ = ("deviceInfo", "maxPowerAcW", "maxPowerDcW")
        DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
        MAXPOWERACW_FIELD_NUMBER: _ClassVar[int]
        MAXPOWERDCW_FIELD_NUMBER: _ClassVar[int]
        deviceInfo: NrgcpSolarchargingTypes.DeviceInfo
        maxPowerAcW: int
        maxPowerDcW: int
        def __init__(self, deviceInfo: _Optional[_Union[NrgcpSolarchargingTypes.DeviceInfo, _Mapping]] = ..., maxPowerAcW: _Optional[int] = ..., maxPowerDcW: _Optional[int] = ...) -> None: ...
    class SolarLimits(_message.Message):
        __slots__ = ("feedInLimitW", "maxCurrentAmp", "maxPowerW", "minCurrentAmp", "minPowerW")
        FEEDINLIMITW_FIELD_NUMBER: _ClassVar[int]
        MAXCURRENTAMP_FIELD_NUMBER: _ClassVar[int]
        MAXPOWERW_FIELD_NUMBER: _ClassVar[int]
        MINCURRENTAMP_FIELD_NUMBER: _ClassVar[int]
        MINPOWERW_FIELD_NUMBER: _ClassVar[int]
        feedInLimitW: int
        maxCurrentAmp: float
        maxPowerW: int
        minCurrentAmp: float
        minPowerW: int
        def __init__(self, feedInLimitW: _Optional[int] = ..., maxCurrentAmp: _Optional[float] = ..., maxPowerW: _Optional[int] = ..., minCurrentAmp: _Optional[float] = ..., minPowerW: _Optional[int] = ...) -> None: ...
    class SolarProfile(_message.Message):
        __slots__ = ("battery", "energyMeter", "id", "name", "settings", "smartLoad", "solarInv", "strategy")
        BATTERY_FIELD_NUMBER: _ClassVar[int]
        ENERGYMETER_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SMARTLOAD_FIELD_NUMBER: _ClassVar[int]
        SOLARINV_FIELD_NUMBER: _ClassVar[int]
        STRATEGY_FIELD_NUMBER: _ClassVar[int]
        battery: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.BatteryInfo]
        energyMeter: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.EnergyMeterInfo]
        id: int
        name: str
        settings: NrgcpSolarchargingTypes.SolarSettings
        smartLoad: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SmartLoadInfo]
        solarInv: _containers.RepeatedCompositeFieldContainer[NrgcpSolarchargingTypes.SolarInverterInfo]
        strategy: NrgcpSolarchargingTypes.SolarStrategy
        def __init__(self, battery: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.BatteryInfo, _Mapping]]] = ..., energyMeter: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.EnergyMeterInfo, _Mapping]]] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., settings: _Optional[_Union[NrgcpSolarchargingTypes.SolarSettings, _Mapping]] = ..., smartLoad: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SmartLoadInfo, _Mapping]]] = ..., solarInv: _Optional[_Iterable[_Union[NrgcpSolarchargingTypes.SolarInverterInfo, _Mapping]]] = ..., strategy: _Optional[_Union[NrgcpSolarchargingTypes.SolarStrategy, _Mapping]] = ...) -> None: ...
    class SolarSettings(_message.Message):
        __slots__ = ("avgLoadW", "batterySocSettings", "chargeMinSettings", "dynamicPeakManagerSettings", "globalOffsetW", "gridSettings", "holdTimings", "limits", "phaseSwitchSettings", "priorities", "smartloadTempSettings")
        AVGLOADW_FIELD_NUMBER: _ClassVar[int]
        BATTERYSOCSETTINGS_FIELD_NUMBER: _ClassVar[int]
        CHARGEMINSETTINGS_FIELD_NUMBER: _ClassVar[int]
        DYNAMICPEAKMANAGERSETTINGS_FIELD_NUMBER: _ClassVar[int]
        GLOBALOFFSETW_FIELD_NUMBER: _ClassVar[int]
        GRIDSETTINGS_FIELD_NUMBER: _ClassVar[int]
        HOLDTIMINGS_FIELD_NUMBER: _ClassVar[int]
        LIMITS_FIELD_NUMBER: _ClassVar[int]
        PHASESWITCHSETTINGS_FIELD_NUMBER: _ClassVar[int]
        PRIORITIES_FIELD_NUMBER: _ClassVar[int]
        SMARTLOADTEMPSETTINGS_FIELD_NUMBER: _ClassVar[int]
        avgLoadW: int
        batterySocSettings: NrgcpSolarchargingTypes.BatterySocSettings
        chargeMinSettings: NrgcpSolarchargingTypes.ChargeMinSettings
        dynamicPeakManagerSettings: NrgcpSolarchargingTypes.DynamicPeakManagerSettings
        globalOffsetW: int
        gridSettings: NrgcpSolarchargingTypes.GridSettings
        holdTimings: NrgcpSolarchargingTypes.HoldTimings
        limits: NrgcpSolarchargingTypes.SolarLimits
        phaseSwitchSettings: NrgcpSolarchargingTypes.PhaseSwitchSettings
        priorities: NrgcpSolarchargingTypes.Priorities
        smartloadTempSettings: NrgcpSolarchargingTypes.SmartLoadTempSettings
        def __init__(self, avgLoadW: _Optional[int] = ..., batterySocSettings: _Optional[_Union[NrgcpSolarchargingTypes.BatterySocSettings, _Mapping]] = ..., chargeMinSettings: _Optional[_Union[NrgcpSolarchargingTypes.ChargeMinSettings, _Mapping]] = ..., dynamicPeakManagerSettings: _Optional[_Union[NrgcpSolarchargingTypes.DynamicPeakManagerSettings, _Mapping]] = ..., globalOffsetW: _Optional[int] = ..., gridSettings: _Optional[_Union[NrgcpSolarchargingTypes.GridSettings, _Mapping]] = ..., holdTimings: _Optional[_Union[NrgcpSolarchargingTypes.HoldTimings, _Mapping]] = ..., limits: _Optional[_Union[NrgcpSolarchargingTypes.SolarLimits, _Mapping]] = ..., phaseSwitchSettings: _Optional[_Union[NrgcpSolarchargingTypes.PhaseSwitchSettings, _Mapping]] = ..., priorities: _Optional[_Union[NrgcpSolarchargingTypes.Priorities, str]] = ..., smartloadTempSettings: _Optional[_Union[NrgcpSolarchargingTypes.SmartLoadTempSettings, _Mapping]] = ...) -> None: ...
    class SolarStrategy(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: NrgcpSolarchargingTypes.SolarStrategyType
        def __init__(self, type: _Optional[_Union[NrgcpSolarchargingTypes.SolarStrategyType, str]] = ...) -> None: ...
    def __init__(self) -> None: ...

class NrgcpLicenseServicesTypes(_message.Message):
    __slots__ = ()
    class LicenseServiceInfo(_message.Message):
        __slots__ = ("serviceId", "timeLeftH")
        SERVICEID_FIELD_NUMBER: _ClassVar[int]
        TIMELEFTH_FIELD_NUMBER: _ClassVar[int]
        serviceId: int
        timeLeftH: int
        def __init__(self, serviceId: _Optional[int] = ..., timeLeftH: _Optional[int] = ...) -> None: ...
    class LicenseServices(_message.Message):
        __slots__ = ("numOfActiveServices", "numOfServices", "serviceInfo")
        NUMOFACTIVESERVICES_FIELD_NUMBER: _ClassVar[int]
        NUMOFSERVICES_FIELD_NUMBER: _ClassVar[int]
        SERVICEINFO_FIELD_NUMBER: _ClassVar[int]
        numOfActiveServices: int
        numOfServices: int
        serviceInfo: _containers.RepeatedCompositeFieldContainer[NrgcpLicenseServicesTypes.LicenseServiceInfo]
        def __init__(self, numOfActiveServices: _Optional[int] = ..., numOfServices: _Optional[int] = ..., serviceInfo: _Optional[_Iterable[_Union[NrgcpLicenseServicesTypes.LicenseServiceInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class NrgcpStatisticsTypes(_message.Message):
    __slots__ = ()
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAM_ALL: _ClassVar[NrgcpStatisticsTypes.RequestType]
        RAM_AREA: _ClassVar[NrgcpStatisticsTypes.RequestType]
    RAM_ALL: NrgcpStatisticsTypes.RequestType
    RAM_AREA: NrgcpStatisticsTypes.RequestType
    class RequestInfo(_message.Message):
        __slots__ = ("newestTs", "numDataPoints", "oldestTs", "reqType")
        NEWESTTS_FIELD_NUMBER: _ClassVar[int]
        NUMDATAPOINTS_FIELD_NUMBER: _ClassVar[int]
        OLDESTTS_FIELD_NUMBER: _ClassVar[int]
        REQTYPE_FIELD_NUMBER: _ClassVar[int]
        newestTs: int
        numDataPoints: int
        oldestTs: int
        reqType: NrgcpStatisticsTypes.RequestType
        def __init__(self, newestTs: _Optional[int] = ..., numDataPoints: _Optional[int] = ..., oldestTs: _Optional[int] = ..., reqType: _Optional[_Union[NrgcpStatisticsTypes.RequestType, str]] = ...) -> None: ...
    class SolarChargingStatistics(_message.Message):
        __slots__ = ("batSoc", "pBat", "pGrid", "pLoad", "pNrgkick", "pPv", "pSl", "ts")
        BATSOC_FIELD_NUMBER: _ClassVar[int]
        PBAT_FIELD_NUMBER: _ClassVar[int]
        PGRID_FIELD_NUMBER: _ClassVar[int]
        PLOAD_FIELD_NUMBER: _ClassVar[int]
        PNRGKICK_FIELD_NUMBER: _ClassVar[int]
        PPV_FIELD_NUMBER: _ClassVar[int]
        PSL_FIELD_NUMBER: _ClassVar[int]
        TS_FIELD_NUMBER: _ClassVar[int]
        batSoc: int
        pBat: int
        pGrid: int
        pLoad: int
        pNrgkick: int
        pPv: int
        pSl: int
        ts: int
        def __init__(self, batSoc: _Optional[int] = ..., pBat: _Optional[int] = ..., pGrid: _Optional[int] = ..., pLoad: _Optional[int] = ..., pNrgkick: _Optional[int] = ..., pPv: _Optional[int] = ..., pSl: _Optional[int] = ..., ts: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
