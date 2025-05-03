from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.dal_enums_taxation_system_aqsi_enum import DALEnumsTaxationSystemAqsiEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_receipt_models_payment_v3 import NebularApiModelsReceiptModelsPaymentV3


T = TypeVar("T", bound="NebularApiModelsIntegrationsCheckCloseV3")


@_attrs_define
class NebularApiModelsIntegrationsCheckCloseV3:
    """Параметры закрытия чека

    Attributes:
        payments (Union[None, Unset, list['NebularApiModelsReceiptModelsPaymentV3']]): <div class="apidocs-
            russian">Список платежей</div>
            <div class="apidocs-english">Payments list</div>
        taxation_system (Union[Unset, DALEnumsTaxationSystemAqsiEnum]):
    """

    payments: Union[None, Unset, list["NebularApiModelsReceiptModelsPaymentV3"]] = UNSET
    taxation_system: Union[Unset, DALEnumsTaxationSystemAqsiEnum] = UNSET

    def to_dict(self) -> dict[str, Any]:
        payments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.payments, Unset):
            payments = UNSET
        elif isinstance(self.payments, list):
            payments = []
            for payments_type_0_item_data in self.payments:
                payments_type_0_item = payments_type_0_item_data.to_dict()
                payments.append(payments_type_0_item)

        else:
            payments = self.payments

        taxation_system: Union[Unset, int] = UNSET
        if not isinstance(self.taxation_system, Unset):
            taxation_system = self.taxation_system.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if payments is not UNSET:
            field_dict["payments"] = payments
        if taxation_system is not UNSET:
            field_dict["taxationSystem"] = taxation_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_receipt_models_payment_v3 import NebularApiModelsReceiptModelsPaymentV3

        d = dict(src_dict)

        def _parse_payments(data: object) -> Union[None, Unset, list["NebularApiModelsReceiptModelsPaymentV3"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payments_type_0 = []
                _payments_type_0 = data
                for payments_type_0_item_data in _payments_type_0:
                    payments_type_0_item = NebularApiModelsReceiptModelsPaymentV3.from_dict(payments_type_0_item_data)

                    payments_type_0.append(payments_type_0_item)

                return payments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsReceiptModelsPaymentV3"]], data)

        payments = _parse_payments(d.pop("payments", UNSET))

        _taxation_system = d.pop("taxationSystem", UNSET)
        taxation_system: Union[Unset, DALEnumsTaxationSystemAqsiEnum]
        if isinstance(_taxation_system, Unset):
            taxation_system = UNSET
        else:
            taxation_system = DALEnumsTaxationSystemAqsiEnum(_taxation_system)

        nebular_api_models_integrations_check_close_v3 = cls(
            payments=payments,
            taxation_system=taxation_system,
        )

        return nebular_api_models_integrations_check_close_v3
