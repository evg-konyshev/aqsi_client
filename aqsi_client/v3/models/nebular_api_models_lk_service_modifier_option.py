from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceModifierOption")


@_attrs_define
class NebularApiModelsLkServiceModifierOption:
    """Опции модификатора товара

    Attributes:
        id (UUID): <div class="apidocs-russian">Идентификатор опции</div>
            <div class="apidocs-english">Option identifier</div>
        modifier_id (UUID): <div class="apidocs-russian">Идентификатор модификатора</div>
            <div class="apidocs-english">Modifier identifier</div>
        goods_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор товара, ингредиента или
            составного товара</div>
            <div class="apidocs-english">Product, ingredient, or compound product identifier</div>
        dummy_name (Union[None, Unset, str]): <div class="apidocs-russian">Название опции</div>
            <div class="apidocs-english">Option name</div>
        quantity (Union[None, Unset, float]): <div class="apidocs-russian">Кол-во/вес</div>
            <div class="apidocs-english">Qty / Weight</div>
        cost (Union[None, Unset, float]): <div class="apidocs-russian">Стоимость</div>
            <div class="apidocs-english">Cost</div>
    """

    id: UUID
    modifier_id: UUID
    goods_id: Union[None, UUID, Unset] = UNSET
    dummy_name: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    cost: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        modifier_id = str(self.modifier_id)

        goods_id: Union[None, Unset, str]
        if isinstance(self.goods_id, Unset):
            goods_id = UNSET
        elif isinstance(self.goods_id, UUID):
            goods_id = str(self.goods_id)
        else:
            goods_id = self.goods_id

        dummy_name: Union[None, Unset, str]
        if isinstance(self.dummy_name, Unset):
            dummy_name = UNSET
        else:
            dummy_name = self.dummy_name

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        cost: Union[None, Unset, float]
        if isinstance(self.cost, Unset):
            cost = UNSET
        else:
            cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "modifierId": modifier_id,
            }
        )
        if goods_id is not UNSET:
            field_dict["goodsId"] = goods_id
        if dummy_name is not UNSET:
            field_dict["dummyName"] = dummy_name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        modifier_id = UUID(d.pop("modifierId"))

        def _parse_goods_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                goods_id_type_0 = UUID(data)

                return goods_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        goods_id = _parse_goods_id(d.pop("goodsId", UNSET))

        def _parse_dummy_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dummy_name = _parse_dummy_name(d.pop("dummyName", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost = _parse_cost(d.pop("cost", UNSET))

        nebular_api_models_lk_service_modifier_option = cls(
            id=id,
            modifier_id=modifier_id,
            goods_id=goods_id,
            dummy_name=dummy_name,
            quantity=quantity,
            cost=cost,
        )

        return nebular_api_models_lk_service_modifier_option
