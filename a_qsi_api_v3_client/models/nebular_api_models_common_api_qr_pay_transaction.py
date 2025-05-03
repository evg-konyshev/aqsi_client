from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiQrPayTransaction")


@_attrs_define
class NebularApiModelsCommonApiQrPayTransaction:
    """
    Attributes:
        operation_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор операции</div>
            <div class="apidocs-english">Operation identifier</div>
        order_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор чека</div>
            <div class="apidocs-english">Receipt identifier</div>
    """

    operation_id: Union[None, Unset, str] = UNSET
    order_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id: Union[None, Unset, str]
        if isinstance(self.operation_id, Unset):
            operation_id = UNSET
        else:
            operation_id = self.operation_id

        order_id: Union[None, Unset, str]
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        operation_id = _parse_operation_id(d.pop("operationId", UNSET))

        def _parse_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_id = _parse_order_id(d.pop("orderId", UNSET))

        nebular_api_models_common_api_qr_pay_transaction = cls(
            operation_id=operation_id,
            order_id=order_id,
        )

        return nebular_api_models_common_api_qr_pay_transaction
