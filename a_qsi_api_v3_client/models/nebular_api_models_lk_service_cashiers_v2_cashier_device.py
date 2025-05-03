from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NebularApiModelsLkServiceCashiersV2CashierDevice")


@_attrs_define
class NebularApiModelsLkServiceCashiersV2CashierDevice:
    """
    Attributes:
        imei (str): <div class="apidocs-russian">IMEI устройства</div>
            <div class="apidocs-english">Device IMEI</div>
    """

    imei: str

    def to_dict(self) -> dict[str, Any]:
        imei = self.imei

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "imei": imei,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        imei = d.pop("imei")

        nebular_api_models_lk_service_cashiers_v2_cashier_device = cls(
            imei=imei,
        )

        return nebular_api_models_lk_service_cashiers_v2_cashier_device
