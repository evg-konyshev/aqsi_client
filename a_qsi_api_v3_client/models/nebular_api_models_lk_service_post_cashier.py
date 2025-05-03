from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
    from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg


T = TypeVar("T", bound="NebularApiModelsLkServicePostCashier")


@_attrs_define
class NebularApiModelsLkServicePostCashier:
    """Модель отправки данных для создания/изменения кассира

    Example:
        {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin': '0000', 'code': '34', 'devices': [4, 47],
            'img': None, 'externalId': '1k23o3kk', 'shops': None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}

    Attributes:
        name (str): <div class="apidocs-russian">Имя кассира</div>
            <div class="apidocs-english">Cashier's name</div>
        position (str): <div class="apidocs-russian">Должность кассира Допустимые значения: <b>"Junior Cashier"</b>,
            <b>"Cashier"</b>, <b>"Admin"</b>, <b>"Courier"</b>, <b>"Junior Courier"</b></div>
            <div class="apidocs-english">Cashier position Allowed values: <b>"Junior Cashier"</b>, <b>"Cashier"</b>,
            <b>"Admin"</b>, <b>"Courier"</b>, <b>"Junior Courier"</b></div>
        inn (Union[None, Unset, str]): <div class="apidocs-russian">ИНН кассира</div>
            <div class="apidocs-english">Cashier TIN</div>
        pin (Union[None, Unset, str]): <div class="apidocs-russian">ПИН-код кассира</div>
            <div class="apidocs-english">Cashier PIN</div>
        code (Union[None, Unset, str]): <div class="apidocs-russian">Код кассира</div>
            <div class="apidocs-english">Cashier Code</div>
        devices (Union[None, Unset, list[int]]): <div class="apidocs-russian">Список ID устройств для привязки к
            кассиру</div>
            <div class="apidocs-english">List of device IDs for binding to the cashier</div>
        img (Union['NebularApiModelsLkServiceImg', None, Unset]): <div class="apidocs-russian">Изображение кассира</div>
            <div class="apidocs-english">Cashier image</div>
        external_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор кассира во внешней
            системе</div>
            <div class="apidocs-english">Cashier external system ID</div>
        shops (Union[None, Unset, list[Any]]): <div class="apidocs-russian">Список ID или кодов магазина для привязки
            кассира к кассам этого магазина</div>
            <div class="apidocs-english">List of store IDs or store codes for associating cashier with these stores’
            devices</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
    """

    name: str
    position: str
    inn: Union[None, Unset, str] = UNSET
    pin: Union[None, Unset, str] = UNSET
    code: Union[None, Unset, str] = UNSET
    devices: Union[None, Unset, list[int]] = UNSET
    img: Union["NebularApiModelsLkServiceImg", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    shops: Union[None, Unset, list[Any]] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg

        name = self.name

        position = self.position

        inn: Union[None, Unset, str]
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        pin: Union[None, Unset, str]
        if isinstance(self.pin, Unset):
            pin = UNSET
        else:
            pin = self.pin

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        devices: Union[None, Unset, list[int]]
        if isinstance(self.devices, Unset):
            devices = UNSET
        elif isinstance(self.devices, list):
            devices = self.devices

        else:
            devices = self.devices

        img: Union[None, Unset, dict[str, Any]]
        if isinstance(self.img, Unset):
            img = UNSET
        elif isinstance(self.img, NebularApiModelsLkServiceImg):
            img = self.img.to_dict()
        else:
            img = self.img

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        shops: Union[None, Unset, list[Any]]
        if isinstance(self.shops, Unset):
            shops = UNSET
        elif isinstance(self.shops, list):
            shops = self.shops

        else:
            shops = self.shops

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

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "position": position,
            }
        )
        if inn is not UNSET:
            field_dict["inn"] = inn
        if pin is not UNSET:
            field_dict["pin"] = pin
        if code is not UNSET:
            field_dict["code"] = code
        if devices is not UNSET:
            field_dict["devices"] = devices
        if img is not UNSET:
            field_dict["img"] = img
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if shops is not UNSET:
            field_dict["shops"] = shops
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg

        d = dict(src_dict)
        name = d.pop("name")

        position = d.pop("position")

        def _parse_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_pin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pin = _parse_pin(d.pop("pin", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_devices(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                devices_type_0 = cast(list[int], data)

                return devices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        devices = _parse_devices(d.pop("devices", UNSET))

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

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_shops(data: object) -> Union[None, Unset, list[Any]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shops_type_0 = cast(list[Any], data)

                return shops_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Any]], data)

        shops = _parse_shops(d.pop("shops", UNSET))

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

        nebular_api_models_lk_service_post_cashier = cls(
            name=name,
            position=position,
            inn=inn,
            pin=pin,
            code=code,
            devices=devices,
            img=img,
            external_id=external_id,
            shops=shops,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_post_cashier
