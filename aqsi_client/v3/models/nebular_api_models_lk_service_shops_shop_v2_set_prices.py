from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceShopsShopV2SetPrices")


@_attrs_define
class NebularApiModelsLkServiceShopsShopV2SetPrices:
    """Модель магазина версии 2 для установления цены на товар

    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор магазина</div>
            <div class="apidocs-english">Shop identifier</div>
        price (Union[Unset, float]): <div class="apidocs-russian">Цена товара для магазина</div>
            <div class="apidocs-english">Goods price for the store</div>
        max_discount_percent (Union[Unset, float]): <div class="apidocs-russian">Максимальная скидка товара</div>
            <div class="apidocs-english">Maximum goods percent discount</div>
    """

    id: str
    price: Union[Unset, float] = UNSET
    max_discount_percent: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        price = self.price

        max_discount_percent = self.max_discount_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if max_discount_percent is not UNSET:
            field_dict["maxDiscountPercent"] = max_discount_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        price = d.pop("price", UNSET)

        max_discount_percent = d.pop("maxDiscountPercent", UNSET)

        nebular_api_models_lk_service_shops_shop_v2_set_prices = cls(
            id=id,
            price=price,
            max_discount_percent=max_discount_percent,
        )

        return nebular_api_models_lk_service_shops_shop_v2_set_prices
