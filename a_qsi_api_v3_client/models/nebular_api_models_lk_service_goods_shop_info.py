import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceGoodsShopInfo")


@_attrs_define
class NebularApiModelsLkServiceGoodsShopInfo:
    """Модель магазина к которому привязан товар

    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор магазина</div>
            <div class="apidocs-english">Shop identifier</div>
        name (Union[None, Unset, str]): <div class="apidocs-russian">Название магазина</div>
            <div class="apidocs-english">Shop name</div>
        deleted_at (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Время удаления магазина</div>
            <div class="apidocs-english">Shop deletion timestamp</div>
    """

    id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        nebular_api_models_lk_service_goods_shop_info = cls(
            id=id,
            name=name,
            deleted_at=deleted_at,
        )

        return nebular_api_models_lk_service_goods_shop_info
