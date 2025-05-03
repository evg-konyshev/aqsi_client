from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiCheque")


@_attrs_define
class NebularApiModelsCommonApiCheque:
    """<div class="apidocs-russian">Спасибо позиция</div>
    <div class="apidocs-english">Spasibo position</div>

        Attributes:
            amount (Union[Unset, int]): <div class="apidocs-russian">Полная сумма всех товаров данной категории</div>
                <div class="apidocs-english">Total amount of products that category</div>
            product (Union[None, Unset, str]): <div class="apidocs-russian">Название товара</div>
                <div class="apidocs-english">Product name</div>
            quantity (Union[Unset, float]): <div class="apidocs-russian">Количество товара</div>
                <div class="apidocs-english">Product quantity</div>
    """

    amount: Union[Unset, int] = UNSET
    product: Union[None, Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        product: Union[None, Unset, str]
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if product is not UNSET:
            field_dict["product"] = product
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        def _parse_product(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product = _parse_product(d.pop("product", UNSET))

        quantity = d.pop("quantity", UNSET)

        nebular_api_models_common_api_cheque = cls(
            amount=amount,
            product=product,
            quantity=quantity,
        )

        return nebular_api_models_common_api_cheque
