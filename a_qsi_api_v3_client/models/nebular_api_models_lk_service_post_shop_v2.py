from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar("T", bound="NebularApiModelsLkServicePostShopV2")


@_attrs_define
class NebularApiModelsLkServicePostShopV2:
    """<div class="apidocs-russian">Модель магазина V2</div>
    <div class="apidocs-english">Shop model V2</div>

        Example:
            {'id': 'FRFBRW223545', 'name': 'Магазин иллюзий', 'address': {'data': {'city': 'Москва', 'house': '13',
                'region': '', 'street': 'ул. Кековая', 'country': 'Россия'}, 'value': 'г. Москва, ул. Кековая д.13',
                'unrestricted_value': None}, 'url': None, 'longitude': None, 'latitude': None, 'onlineStore': True,
                'activityType': None, 'customProperties': None}

        Attributes:
            id (str): <div class="apidocs-russian">Идентификатор магазина</div>
                <div class="apidocs-english">Shop id</div>
            name (str): <div class="apidocs-russian">Название магазина</div>
                <div class="apidocs-english">Shop name</div>
            address (Union['NebularApiModelsLkServiceAddress', None, Unset]): <div class="apidocs-russian">Адрес магазина
                (объект dadata, см. https://dadata.ru/api/suggest/#about-address)</div>
                <div class="apidocs-english">Store address (dadata object, see https://dadata.ru/api/suggest/#about-
                address)</div>
            url (Union[None, Unset, str]): <div class="apidocs-russian">Интернет-адрес магазина</div>
                <div class="apidocs-english">Shop internet address</div>
            longitude (Union[None, Unset, str]): <div class="apidocs-russian">Долгота магазина</div>
                <div class="apidocs-english">Shop Longitude</div>
            latitude (Union[None, Unset, str]): <div class="apidocs-russian">Широта магазина</div>
                <div class="apidocs-english">Shop latitude</div>
            online_store (Union[Unset, bool]): <div class="apidocs-russian">Интернет-магазин</div>
                <div class="apidocs-english">Online store</div> Default: False.
            activity_type (Union[None, Unset, str]): <div class="apidocs-russian">Вид деятельности</div>
                <div class="apidocs-english">Activity type</div>
            custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
                russian">Дополнительные параметры</div>
                <div class="apidocs-english">Extra options</div>
    """

    id: str
    name: str
    address: Union["NebularApiModelsLkServiceAddress", None, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    longitude: Union[None, Unset, str] = UNSET
    latitude: Union[None, Unset, str] = UNSET
    online_store: Union[Unset, bool] = False
    activity_type: Union[None, Unset, str] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress

        id = self.id

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

        online_store = self.online_store

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
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if url is not UNSET:
            field_dict["url"] = url
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if online_store is not UNSET:
            field_dict["onlineStore"] = online_store
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_address import NebularApiModelsLkServiceAddress
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

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

        online_store = d.pop("onlineStore", UNSET)

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

        nebular_api_models_lk_service_post_shop_v2 = cls(
            id=id,
            name=name,
            address=address,
            url=url,
            longitude=longitude,
            latitude=latitude,
            online_store=online_store,
            activity_type=activity_type,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_post_shop_v2
