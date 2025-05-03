import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
    from ..models.nebular_api_models_lk_service_warehouse_v2_warehouse_get_shop_v2 import (
        NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceGetShopV2")


@_attrs_define
class NebularApiModelsLkServiceGetShopV2:
    """
    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор магазина</div>
            <div class="apidocs-english">Store identifier</div>
        warehouses (Union[None, Unset, list['NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2']]): <div
            class="apidocs-russian">Массив складов</div>
            <div class="apidocs-english">Array of warehouses</div>
        name (Union[None, Unset, str]): <div class="apidocs-russian">Название магазина</div>
            <div class="apidocs-english">Shop name</div>
        address (Union['NebularApiModelsLkServiceAddress', None, Unset]): <div class="apidocs-russian">Адрес магазина
            (объект dadata, см. https://dadata.ru/api/suggest/#about-address)</div>
            <div class="apidocs-english">Store address (dadata object, see https://dadata.ru/api/suggest/#abo</div>
        url (Union[None, Unset, str]): <div class="apidocs-russian">Интернет-адрес магазина</div>
            <div class="apidocs-english">Shop internet address</div>
        longitude (Union[None, Unset, str]): <div class="apidocs-russian">Долгота магазина</div>
            <div class="apidocs-english">Shop Longitude</div>
        latitude (Union[None, Unset, str]): <div class="apidocs-russian">Широта магазина</div>
            <div class="apidocs-english">Shop latitude</div>
        russian_name (Union[None, Unset, str]): <div class="apidocs-russian">Название на русском</div>
            <div class="apidocs-english">Name in russian</div>
        english_name (Union[None, Unset, str]): <div class="apidocs-russian">Название на английском</div>
            <div class="apidocs-english">Name in english</div>
        responsible (Union[None, Unset, str]): <div class="apidocs-russian">Ответственный</div>
            <div class="apidocs-english">Responsible</div>
        authority (Union[None, Unset, str]): <div class="apidocs-russian">Владелец</div>
            <div class="apidocs-english">Authority</div>
        phone (Union[None, Unset, str]): <div class="apidocs-russian">Телефон</div>
            <div class="apidocs-english">Phone</div>
        zip_code (Union[None, Unset, str]): <div class="apidocs-russian">Зип код</div>
            <div class="apidocs-english">ZipCode</div>
        online_store (Union[Unset, bool]): <div class="apidocs-russian">Интернет-магазин</div>
            <div class="apidocs-english">OnlineStore</div> Default: False.
        created_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Дата создания магазина</div>
            <div class="apidocs-english">Store creation date</div>
        activity_type (Union[None, Unset, str]): <div class="apidocs-russian">Вид деятельности</div>
            <div class="apidocs-english">Activity type</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
    """

    id: Union[None, Unset, str] = UNSET
    warehouses: Union[None, Unset, list["NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2"]] = UNSET
    name: Union[None, Unset, str] = UNSET
    address: Union["NebularApiModelsLkServiceAddress", None, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    longitude: Union[None, Unset, str] = UNSET
    latitude: Union[None, Unset, str] = UNSET
    russian_name: Union[None, Unset, str] = UNSET
    english_name: Union[None, Unset, str] = UNSET
    responsible: Union[None, Unset, str] = UNSET
    authority: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    zip_code: Union[None, Unset, str] = UNSET
    online_store: Union[Unset, bool] = False
    created_at: Union[Unset, datetime.datetime] = UNSET
    activity_type: Union[None, Unset, str] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        warehouses: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.warehouses, Unset):
            warehouses = UNSET
        elif isinstance(self.warehouses, list):
            warehouses = []
            for warehouses_type_0_item_data in self.warehouses:
                warehouses_type_0_item = warehouses_type_0_item_data.to_dict()
                warehouses.append(warehouses_type_0_item)

        else:
            warehouses = self.warehouses

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, NebularApiModelsLkServiceAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        longitude: Union[None, Unset, str]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: Union[None, Unset, str]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        russian_name: Union[None, Unset, str]
        if isinstance(self.russian_name, Unset):
            russian_name = UNSET
        else:
            russian_name = self.russian_name

        english_name: Union[None, Unset, str]
        if isinstance(self.english_name, Unset):
            english_name = UNSET
        else:
            english_name = self.english_name

        responsible: Union[None, Unset, str]
        if isinstance(self.responsible, Unset):
            responsible = UNSET
        else:
            responsible = self.responsible

        authority: Union[None, Unset, str]
        if isinstance(self.authority, Unset):
            authority = UNSET
        else:
            authority = self.authority

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        zip_code: Union[None, Unset, str]
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        online_store = self.online_store

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        activity_type: Union[None, Unset, str]
        if isinstance(self.activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = self.activity_type

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if warehouses is not UNSET:
            field_dict["warehouses"] = warehouses
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if url is not UNSET:
            field_dict["url"] = url
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if russian_name is not UNSET:
            field_dict["russianName"] = russian_name
        if english_name is not UNSET:
            field_dict["englishName"] = english_name
        if responsible is not UNSET:
            field_dict["responsible"] = responsible
        if authority is not UNSET:
            field_dict["authority"] = authority
        if phone is not UNSET:
            field_dict["phone"] = phone
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if online_store is not UNSET:
            field_dict["onlineStore"] = online_store
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_lk_service_warehouse_v2_warehouse_get_shop_v2 import (
            NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_warehouses(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warehouses_type_0 = []
                _warehouses_type_0 = data
                for warehouses_type_0_item_data in _warehouses_type_0:
                    warehouses_type_0_item = NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2.from_dict(
                        warehouses_type_0_item_data
                    )

                    warehouses_type_0.append(warehouses_type_0_item)

                return warehouses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2"]], data)

        warehouses = _parse_warehouses(d.pop("warehouses", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_address(data: object) -> Union["NebularApiModelsLkServiceAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_1 = NebularApiModelsLkServiceAddress.from_dict(data)

                return address_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceAddress", None, Unset], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_russian_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        russian_name = _parse_russian_name(d.pop("russianName", UNSET))

        def _parse_english_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        english_name = _parse_english_name(d.pop("englishName", UNSET))

        def _parse_responsible(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible = _parse_responsible(d.pop("responsible", UNSET))

        def _parse_authority(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authority = _parse_authority(d.pop("authority", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))

        online_store = d.pop("onlineStore", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_activity_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activity_type = _parse_activity_type(d.pop("activityType", UNSET))

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

        nebular_api_models_lk_service_get_shop_v2 = cls(
            id=id,
            warehouses=warehouses,
            name=name,
            address=address,
            url=url,
            longitude=longitude,
            latitude=latitude,
            russian_name=russian_name,
            english_name=english_name,
            responsible=responsible,
            authority=authority,
            phone=phone,
            zip_code=zip_code,
            online_store=online_store,
            created_at=created_at,
            activity_type=activity_type,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_get_shop_v2
