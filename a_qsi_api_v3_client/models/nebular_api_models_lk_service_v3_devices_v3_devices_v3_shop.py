from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop:
    """
    Attributes:
        id (str):
        external_id (str):
    """

    id: str
    external_id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("externalId")

        nebular_api_models_lk_service_v3_devices_v3_devices_v3_shop = cls(
            id=id,
            external_id=external_id,
        )

        return nebular_api_models_lk_service_v3_devices_v3_devices_v3_shop
