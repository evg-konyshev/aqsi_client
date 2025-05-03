from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceLoyaltyCard")


@_attrs_define
class NebularApiModelsLkServiceLoyaltyCard:
    """<div class="apidocs-russian">Карта лояльности</div>
    <div class="apidocs-english">Loyalty card</div>

        Attributes:
            prefix (Union[None, Unset, str]): <div class="apidocs-russian">Префикс карты</div>
                <div class="apidocs-english">Card prefix</div>
            number (Union[None, Unset, str]): <div class="apidocs-russian">Номер карты</div>
                <div class="apidocs-english">Card number</div>
    """

    prefix: Union[None, Unset, str] = UNSET
    number: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        prefix: Union[None, Unset, str]
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_prefix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        nebular_api_models_lk_service_loyalty_card = cls(
            prefix=prefix,
            number=number,
        )

        return nebular_api_models_lk_service_loyalty_card
