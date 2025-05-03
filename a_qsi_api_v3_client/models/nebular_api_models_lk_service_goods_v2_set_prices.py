from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_shops_shop_v2_set_prices import (
        NebularApiModelsLkServiceShopsShopV2SetPrices,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceGoodsV2SetPrices")


@_attrs_define
class NebularApiModelsLkServiceGoodsV2SetPrices:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор товара</div>
            <div class="apidocs-english">Goods identifier</div>
        shops (list['NebularApiModelsLkServiceShopsShopV2SetPrices']): <div class="apidocs-russian">Массив
            магазинов</div>
            <div class="apidocs-english">Array of shops</div>
        default_price (Union[Unset, float]): <div class="apidocs-russian">Цена товара в БД</div>
            <div class="apidocs-english">Product price in the database</div>
    """

    id: str
    shops: list["NebularApiModelsLkServiceShopsShopV2SetPrices"]
    default_price: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        shops = []
        for shops_item_data in self.shops:
            shops_item = shops_item_data.to_dict()
            shops.append(shops_item)

        default_price = self.default_price

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "shops": shops,
            }
        )
        if default_price is not UNSET:
            field_dict["defaultPrice"] = default_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_shops_shop_v2_set_prices import (
            NebularApiModelsLkServiceShopsShopV2SetPrices,
        )

        d = dict(src_dict)
        id = d.pop("id")

        shops = []
        _shops = d.pop("shops")
        for shops_item_data in _shops:
            shops_item = NebularApiModelsLkServiceShopsShopV2SetPrices.from_dict(shops_item_data)

            shops.append(shops_item)

        default_price = d.pop("defaultPrice", UNSET)

        nebular_api_models_lk_service_goods_v2_set_prices = cls(
            id=id,
            shops=shops,
            default_price=default_price,
        )

        return nebular_api_models_lk_service_goods_v2_set_prices
