from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.nebular_api_enums_input_method_enum import NebularApiEnumsInputMethodEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsReceiptModelsBaseClientInfo")


@_attrs_define
class NebularApiModelsReceiptModelsBaseClientInfo:
    """<div class="apidocs-russian">Информация о клиенте</div>
    <div class="apidocs-english">Client info</div>

        Attributes:
            id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор клиента</div>
                <div class="apidocs-english">Client identifier</div>
            discount_card (Union[None, Unset, str]): <div class="apidocs-russian">Номер карты лояльности</div>
                <div class="apidocs-english">Loyalty card number</div>
            input_method (Union[Unset, NebularApiEnumsInputMethodEnum]):
    """

    id: Union[None, UUID, Unset] = UNSET
    discount_card: Union[None, Unset, str] = UNSET
    input_method: Union[Unset, NebularApiEnumsInputMethodEnum] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        discount_card: Union[None, Unset, str]
        if isinstance(self.discount_card, Unset):
            discount_card = UNSET
        else:
            discount_card = self.discount_card

        input_method: Union[Unset, int] = UNSET
        if not isinstance(self.input_method, Unset):
            input_method = self.input_method.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if discount_card is not UNSET:
            field_dict["discountCard"] = discount_card
        if input_method is not UNSET:
            field_dict["inputMethod"] = input_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_discount_card(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discount_card = _parse_discount_card(d.pop("discountCard", UNSET))

        _input_method = d.pop("inputMethod", UNSET)
        input_method: Union[Unset, NebularApiEnumsInputMethodEnum]
        if isinstance(_input_method, Unset):
            input_method = UNSET
        else:
            input_method = NebularApiEnumsInputMethodEnum(_input_method)

        nebular_api_models_receipt_models_base_client_info = cls(
            id=id,
            discount_card=discount_card,
            input_method=input_method,
        )

        return nebular_api_models_receipt_models_base_client_info
