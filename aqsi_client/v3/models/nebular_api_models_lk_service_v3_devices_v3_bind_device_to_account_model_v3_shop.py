from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop:
    """
    Attributes:
        external_id (Union[None, Unset, str]): <div class="apidocs-russian">Внешний ID магазина.</div>
            <div class="apidocs-english">Device biding external shop ID.</div>
    """

    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_shop = cls(
            external_id=external_id,
        )

        return nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_shop
