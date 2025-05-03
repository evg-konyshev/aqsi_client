from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_device_model import NebularApiModelsLkServiceDeviceModel


T = TypeVar("T", bound="NebularApiModelsLkServiceDeviceList")


@_attrs_define
class NebularApiModelsLkServiceDeviceList:
    """Модель, содержащая список устройств

    Example:
        {'devices': [{'id': 3, 'imei': 234000300, 'deviceSn': '1234567890123456', 'shopId': 1, 'customProperties':
            [{'key': 'TerminalId', 'value': 'asdee'}]}, {'id': 4, 'imei': 0, 'deviceSn': '1234234334333344', 'shopId': None,
            'customProperties': None}]}

    Attributes:
        devices (Union[None, Unset, list['NebularApiModelsLkServiceDeviceModel']]): <div class="apidocs-
            russian">Устройства</div>
            <div class="apidocs-english">Devices</div>
    """

    devices: Union[None, Unset, list["NebularApiModelsLkServiceDeviceModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        devices: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.devices, Unset):
            devices = UNSET
        elif isinstance(self.devices, list):
            devices = []
            for devices_type_0_item_data in self.devices:
                devices_type_0_item = devices_type_0_item_data.to_dict()
                devices.append(devices_type_0_item)

        else:
            devices = self.devices

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_device_model import NebularApiModelsLkServiceDeviceModel

        d = dict(src_dict)

        def _parse_devices(data: object) -> Union[None, Unset, list["NebularApiModelsLkServiceDeviceModel"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                devices_type_0 = []
                _devices_type_0 = data
                for devices_type_0_item_data in _devices_type_0:
                    devices_type_0_item = NebularApiModelsLkServiceDeviceModel.from_dict(devices_type_0_item_data)

                    devices_type_0.append(devices_type_0_item)

                return devices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceDeviceModel"]], data)

        devices = _parse_devices(d.pop("devices", UNSET))

        nebular_api_models_lk_service_device_list = cls(
            devices=devices,
        )

        return nebular_api_models_lk_service_device_list
