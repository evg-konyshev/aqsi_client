import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_cashiers_v2_cashier_device import (
        NebularApiModelsLkServiceCashiersV2CashierDevice,
    )
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
    from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg


T = TypeVar("T", bound="NebularApiModelsLkServiceCashiersV2GetCashierResponseV2")


@_attrs_define
class NebularApiModelsLkServiceCashiersV2GetCashierResponseV2:
    """
    Example:
        {'id': '1k23o3kk', 'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'lastLoginTime': None, 'code':
            '34', 'img': None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}], 'pin': '0000', 'devices': None}

    Attributes:
        name (str): <div class="apidocs-russian">Имя кассира</div>
            <div class="apidocs-english">Cashier name</div>
        position (str): <div class="apidocs-russian">
                        Должность кассира
                        Допустимые значения: <b>"Junior Cashier"</b>, <b>"Cashier"</b>, <b>"Admin"</b></div>,
            <b>"Courier"</b>, <b>"Junior Courier"</b><div class="apidocs-english">
                        Cashier position
                        Allowed values: <b>"Junior Cashier"</b>, <b>"Cashier"</b>, <b>"Admin"</b>, <b>"Courier"</b>,
            <b>"Junior Courier"</b></div>
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор кассира</div>
            <div class="apidocs-english">Cashier identifier</div>
        inn (Union[None, Unset, str]): <div class="apidocs-russian">ИНН кассира</div>
            <div class="apidocs-english">Cashier TIN</div>
        last_login_time (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Дата и время последнего
            логина кассира</div>
            <div class="apidocs-english">Last cashier login date and time</div>
        code (Union[None, Unset, str]): <div class="apidocs-russian">Код кассира</div>
            <div class="apidocs-english">Cashier code</div>
        img (Union['NebularApiModelsLkServiceImg', None, Unset]): <div class="apidocs-russian">Изображение кассира</div>
            <div class="apidocs-english">Cashier image</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
        pin (Union[None, Unset, str]): <div class="apidocs-russian">ПИН-код кассира</div>
            <div class="apidocs-english">Cashier PIN</div>
        devices (Union[None, Unset, list['NebularApiModelsLkServiceCashiersV2CashierDevice']]): <div class="apidocs-
            russian">Привязанные устройства</div>
            <div class="apidocs-english">Bound devices</div>
    """

    name: str
    position: str
    id: Union[None, Unset, str] = UNSET
    inn: Union[None, Unset, str] = UNSET
    last_login_time: Union[None, Unset, datetime.datetime] = UNSET
    code: Union[None, Unset, str] = UNSET
    img: Union["NebularApiModelsLkServiceImg", None, Unset] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    pin: Union[None, Unset, str] = UNSET
    devices: Union[None, Unset, list["NebularApiModelsLkServiceCashiersV2CashierDevice"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg

        name = self.name

        position = self.position

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        inn: Union[None, Unset, str]
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        last_login_time: Union[None, Unset, str]
        if isinstance(self.last_login_time, Unset):
            last_login_time = UNSET
        elif isinstance(self.last_login_time, datetime.datetime):
            last_login_time = self.last_login_time.isoformat()
        else:
            last_login_time = self.last_login_time

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        img: Union[None, Unset, dict[str, Any]]
        if isinstance(self.img, Unset):
            img = UNSET
        elif isinstance(self.img, NebularApiModelsLkServiceImg):
            img = self.img.to_dict()
        else:
            img = self.img

        custom_properties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_properties, Unset):
            custom_properties = UNSET
        elif isinstance(self.custom_properties, list):
            custom_properties = []
            for custom_properties_type_0_item_data in self.custom_properties:
                custom_properties_type_0_item = custom_properties_type_0_item_data.to_dict()
                custom_properties.append(custom_properties_type_0_item)

        else:
            custom_properties = self.custom_properties

        pin: Union[None, Unset, str]
        if isinstance(self.pin, Unset):
            pin = UNSET
        else:
            pin = self.pin

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
        field_dict.update(
            {
                "name": name,
                "position": position,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if inn is not UNSET:
            field_dict["inn"] = inn
        if last_login_time is not UNSET:
            field_dict["lastLoginTime"] = last_login_time
        if code is not UNSET:
            field_dict["code"] = code
        if img is not UNSET:
            field_dict["img"] = img
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if pin is not UNSET:
            field_dict["pin"] = pin
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_cashiers_v2_cashier_device import (
            NebularApiModelsLkServiceCashiersV2CashierDevice,
        )
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg

        d = dict(src_dict)
        name = d.pop("name")

        position = d.pop("position")

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_last_login_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_time_type_0 = isoparse(data)

                return last_login_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_login_time = _parse_last_login_time(d.pop("lastLoginTime", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_img(data: object) -> Union["NebularApiModelsLkServiceImg", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                img_type_1 = NebularApiModelsLkServiceImg.from_dict(data)

                return img_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceImg", None, Unset], data)

        img = _parse_img(d.pop("img", UNSET))

        def _parse_custom_properties(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_properties_type_0 = []
                _custom_properties_type_0 = data
                for custom_properties_type_0_item_data in _custom_properties_type_0:
                    custom_properties_type_0_item = NebularApiModelsLkServiceCustomProperty.from_dict(
                        custom_properties_type_0_item_data
                    )

                    custom_properties_type_0.append(custom_properties_type_0_item)

                return custom_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]], data)

        custom_properties = _parse_custom_properties(d.pop("customProperties", UNSET))

        def _parse_pin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pin = _parse_pin(d.pop("pin", UNSET))

        def _parse_devices(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceCashiersV2CashierDevice"]]:
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
                    devices_type_0_item = NebularApiModelsLkServiceCashiersV2CashierDevice.from_dict(
                        devices_type_0_item_data
                    )

                    devices_type_0.append(devices_type_0_item)

                return devices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceCashiersV2CashierDevice"]], data)

        devices = _parse_devices(d.pop("devices", UNSET))

        nebular_api_models_lk_service_cashiers_v2_get_cashier_response_v2 = cls(
            name=name,
            position=position,
            id=id,
            inn=inn,
            last_login_time=last_login_time,
            code=code,
            img=img,
            custom_properties=custom_properties,
            pin=pin,
            devices=devices,
        )

        return nebular_api_models_lk_service_cashiers_v2_get_cashier_response_v2
