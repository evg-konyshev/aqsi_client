from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceShopData")


@_attrs_define
class NebularApiModelsLkServiceShopData:
    """<div class="apidocs-russian">Адрессные данные о магазине</div>
    <div class="apidocs-english">Store address information</div>

        Attributes:
            city (Union[None, Unset, str]): <div class="apidocs-russian">Город</div>
                <div class="apidocs-english">City</div>
            house (Union[None, Unset, str]): <div class="apidocs-russian">Дом</div>
                <div class="apidocs-english">House</div>
            region (Union[None, Unset, str]): <div class="apidocs-russian">Регион</div>
                <div class="apidocs-english">Region</div>
            street (Union[None, Unset, str]): <div class="apidocs-russian">Улица</div>
                <div class="apidocs-english">Street</div>
            country (Union[None, Unset, str]): <div class="apidocs-russian">Страна</div>
                <div class="apidocs-english">Country</div>
    """

    city: Union[None, Unset, str] = UNSET
    house: Union[None, Unset, str] = UNSET
    region: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        house: Union[None, Unset, str]
        if isinstance(self.house, Unset):
            house = UNSET
        else:
            house = self.house

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if house is not UNSET:
            field_dict["house"] = house
        if region is not UNSET:
            field_dict["region"] = region
        if street is not UNSET:
            field_dict["street"] = street
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_house(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        house = _parse_house(d.pop("house", UNSET))

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))

        nebular_api_models_lk_service_shop_data = cls(
            city=city,
            house=house,
            region=region,
            street=street,
            country=country,
        )

        return nebular_api_models_lk_service_shop_data
