from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceBindDeviceToAccountModel")


@_attrs_define
class NebularApiModelsLkServiceBindDeviceToAccountModel:
    """
    Attributes:
        shop_id (Union[None, Unset, str]): <div class="apidocs-russian">ID магазина привязки устройства</div>
            <div class="apidocs-english">Device biding shop ID</div>
    """

    shop_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        shop_id: Union[None, Unset, str]
        if isinstance(self.shop_id, Unset):
            shop_id = UNSET
        else:
            shop_id = self.shop_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if shop_id is not UNSET:
            field_dict["shopId"] = shop_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_shop_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop_id = _parse_shop_id(d.pop("shopId", UNSET))

        nebular_api_models_lk_service_bind_device_to_account_model = cls(
            shop_id=shop_id,
        )

        return nebular_api_models_lk_service_bind_device_to_account_model
