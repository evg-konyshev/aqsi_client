from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceReceiptsV2LoyaltyContent")


@_attrs_define
class NebularApiModelsLkServiceReceiptsV2LoyaltyContent:
    """<div class="apidocs-russian">Дополнительные поля агрегации для лояльности</div>
    <div class="apidocs-english">Additional aggregation fields for loyalty</div>

        Attributes:
            disc_amount (Union[Unset, float]): <div class="apidocs-russian">Сумма без скидок - сумма со скидкой</div>
                <div class="apidocs-english">Amount without discounts - discounted amount</div>
            net_amount (Union[Unset, float]): <div class="apidocs-russian">Сумма после скидок без налога</div>
                <div class="apidocs-english">Amount after discounts without tax</div>
            gross_amount (Union[Unset, float]): <div class="apidocs-russian">Сумма после скидок с учетом налога</div>
                <div class="apidocs-english">Amount after discounts with tax</div>
    """

    disc_amount: Union[Unset, float] = UNSET
    net_amount: Union[Unset, float] = UNSET
    gross_amount: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        disc_amount = self.disc_amount

        net_amount = self.net_amount

        gross_amount = self.gross_amount

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if disc_amount is not UNSET:
            field_dict["discAmount"] = disc_amount
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if gross_amount is not UNSET:
            field_dict["grossAmount"] = gross_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disc_amount = d.pop("discAmount", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        gross_amount = d.pop("grossAmount", UNSET)

        nebular_api_models_lk_service_receipts_v2_loyalty_content = cls(
            disc_amount=disc_amount,
            net_amount=net_amount,
            gross_amount=gross_amount,
        )

        return nebular_api_models_lk_service_receipts_v2_loyalty_content
