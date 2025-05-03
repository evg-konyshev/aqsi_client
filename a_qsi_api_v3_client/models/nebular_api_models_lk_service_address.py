from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_shop_data import NebularApiModelsLkServiceShopData


T = TypeVar("T", bound="NebularApiModelsLkServiceAddress")


@_attrs_define
class NebularApiModelsLkServiceAddress:
    """<div class="apidocs-russian">Адрес магазина (объект dadata, см. https://dadata.ru/api/suggest/#about-address)</div>
    <div class="apidocs-english">Store address (dadata object, see https://dadata.ru/api/suggest/#abo</div>

        Attributes:
            data (Union['NebularApiModelsLkServiceShopData', None, Unset]): <div class="apidocs-russian">Адрессные данные о
                магазине</div>
                <div class="apidocs-english">Store address information</div>
            value (Union[None, Unset, str]): <div class="apidocs-russian">Адрес одной строкой (как показывается в списке
                подсказок)</div>
                <div class="apidocs-english">Address in one line (as shown in the list of prompts)</div>
            unrestricted_value (Union[None, Unset, str]): <div class="apidocs-russian">Адрес одной строкой (полный, от
                региона)</div>
                <div class="apidocs-english">Address in one line (full, from the region)</div>
    """

    data: Union["NebularApiModelsLkServiceShopData", None, Unset] = UNSET
    value: Union[None, Unset, str] = UNSET
    unrestricted_value: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_shop_data import NebularApiModelsLkServiceShopData

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, NebularApiModelsLkServiceShopData):
            data = self.data.to_dict()
        else:
            data = self.data

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        unrestricted_value: Union[None, Unset, str]
        if isinstance(self.unrestricted_value, Unset):
            unrestricted_value = UNSET
        else:
            unrestricted_value = self.unrestricted_value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if value is not UNSET:
            field_dict["value"] = value
        if unrestricted_value is not UNSET:
            field_dict["unrestricted_value"] = unrestricted_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_shop_data import NebularApiModelsLkServiceShopData

        d = dict(src_dict)

        def _parse_data(data: object) -> Union["NebularApiModelsLkServiceShopData", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = NebularApiModelsLkServiceShopData.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceShopData", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_unrestricted_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unrestricted_value = _parse_unrestricted_value(d.pop("unrestricted_value", UNSET))

        nebular_api_models_lk_service_address = cls(
            data=data,
            value=value,
            unrestricted_value=unrestricted_value,
        )

        return nebular_api_models_lk_service_address
