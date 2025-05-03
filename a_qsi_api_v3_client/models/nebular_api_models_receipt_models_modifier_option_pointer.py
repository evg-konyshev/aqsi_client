from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsReceiptModelsModifierOptionPointer")


@_attrs_define
class NebularApiModelsReceiptModelsModifierOptionPointer:
    """Опции модификатора товара

    Attributes:
        id (Union[Unset, UUID]): <div class="apidocs-russian">Идентификатор опции</div>
            <div class="apidocs-english">Option identifier</div>
        quantity (Union[Unset, int]): <div class="apidocs-russian">Кол-во раз, которое опция добавлена к товару</div>
            <div class="apidocs-english">Number of times the option is added to the product</div>
    """

    id: Union[Unset, UUID] = UNSET
    quantity: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        quantity = d.pop("quantity", UNSET)

        nebular_api_models_receipt_models_modifier_option_pointer = cls(
            id=id,
            quantity=quantity,
        )

        return nebular_api_models_receipt_models_modifier_option_pointer
