from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2")


@_attrs_define
class NebularApiModelsLkServiceWarehouseV2WarehouseGetShopV2:
    """Модель склада для получения магазина для версии 2

    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор склада</div>
            <div class="apidocs-english">Warehouse identifier</div>
    """

    id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        nebular_api_models_lk_service_warehouse_v2_warehouse_get_shop_v2 = cls(
            id=id,
        )

        return nebular_api_models_lk_service_warehouse_v2_warehouse_get_shop_v2
