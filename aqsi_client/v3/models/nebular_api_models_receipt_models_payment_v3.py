from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_device_payment_type_enum import NebularApiEnumsDevicePaymentTypeEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_acquiring_data_v3 import NebularApiModelsCommonApiAcquiringDataV3


T = TypeVar("T", bound="NebularApiModelsReceiptModelsPaymentV3")


@_attrs_define
class NebularApiModelsReceiptModelsPaymentV3:
    """Оплата версии 3

    Attributes:
        type_ (NebularApiEnumsDevicePaymentTypeEnum):
        amount (float): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Cумма оплаты (значение поля должно быть больше нуля)</div>
            <div class="apidocs-english tag-value">Payment amount (field value must be greater than zero)</div>
        acquiring_data (Union['NebularApiModelsCommonApiAcquiringDataV3', None, Unset]): <div class="apidocs-
            russian">Эквайринговый слип</div>
            <div class="apidocs-english">Acquiring slip</div>
        processed_at (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время проведения оплаты</div>
            <div class="apidocs-english">Date and time of payment</div>
        index (Union[None, Unset, int]): <div class="apidocs-russian">Номер платежа в чеке</div>
            <div class="apidocs-english">Number of payment in receipt</div>
        parent_index (Union[None, Unset, int]): <div class="apidocs-russian">Номер платежа в оригинальном чеке (для чека
            возврата)</div>
            <div class="apidocs-english">Number of payment in the original receipt (for the return receipt)</div>
    """

    type_: NebularApiEnumsDevicePaymentTypeEnum
    amount: float
    acquiring_data: Union["NebularApiModelsCommonApiAcquiringDataV3", None, Unset] = UNSET
    processed_at: Union[None, Unset, str] = UNSET
    index: Union[None, Unset, int] = UNSET
    parent_index: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_acquiring_data_v3 import NebularApiModelsCommonApiAcquiringDataV3

        type_ = self.type_.value

        amount = self.amount

        acquiring_data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.acquiring_data, Unset):
            acquiring_data = UNSET
        elif isinstance(self.acquiring_data, NebularApiModelsCommonApiAcquiringDataV3):
            acquiring_data = self.acquiring_data.to_dict()
        else:
            acquiring_data = self.acquiring_data

        processed_at: Union[None, Unset, str]
        if isinstance(self.processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = self.processed_at

        index: Union[None, Unset, int]
        if isinstance(self.index, Unset):
            index = UNSET
        else:
            index = self.index

        parent_index: Union[None, Unset, int]
        if isinstance(self.parent_index, Unset):
            parent_index = UNSET
        else:
            parent_index = self.parent_index

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "type": type_,
                "amount": amount,
            }
        )
        if acquiring_data is not UNSET:
            field_dict["acquiringData"] = acquiring_data
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if index is not UNSET:
            field_dict["index"] = index
        if parent_index is not UNSET:
            field_dict["parentIndex"] = parent_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_acquiring_data_v3 import NebularApiModelsCommonApiAcquiringDataV3

        d = dict(src_dict)
        type_ = NebularApiEnumsDevicePaymentTypeEnum(d.pop("type"))

        amount = d.pop("amount")

        def _parse_acquiring_data(data: object) -> Union["NebularApiModelsCommonApiAcquiringDataV3", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                acquiring_data_type_1 = NebularApiModelsCommonApiAcquiringDataV3.from_dict(data)

                return acquiring_data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiAcquiringDataV3", None, Unset], data)

        acquiring_data = _parse_acquiring_data(d.pop("acquiringData", UNSET))

        def _parse_processed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        processed_at = _parse_processed_at(d.pop("processedAt", UNSET))

        def _parse_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index = _parse_index(d.pop("index", UNSET))

        def _parse_parent_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_index = _parse_parent_index(d.pop("parentIndex", UNSET))

        nebular_api_models_receipt_models_payment_v3 = cls(
            type_=type_,
            amount=amount,
            acquiring_data=acquiring_data,
            processed_at=processed_at,
            index=index,
            parent_index=parent_index,
        )

        return nebular_api_models_receipt_models_payment_v3
