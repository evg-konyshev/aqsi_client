from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiControllersV3DocumentsManagementCreateManagementDocumentRequestPositionV3")


@_attrs_define
class NebularApiControllersV3DocumentsManagementCreateManagementDocumentRequestPositionV3:
    """
    Attributes:
        quantity (float): <div class="apidocs-russian">Количество. Макс. кол-во знаков после запятой: 3.</div>
            <div class="apidocs-english">Quantity. Precision: 3.</div>
        purchase_price (float): <div class="apidocs-russian">Цена закупки. Макс.кол-во знаков после запятой: 2.</div>
            <div class="apidocs-english">Purchase price. Precision: 2.</div>
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор товара из справочника товаров.
            Обязательно, если не передан externalId.</div>
            <div class="apidocs-english">Good id from catalog. Required when externalId missing.</div>
        external_id (Union[None, Unset, str]): <div class="apidocs-russian">Внешний идентификатор товара из справочника
            товаров. Обязательно, если не передан id, иначе игнорируется.</div>
            <div class="apidocs-english">Good external id from catalog. Required when id missing, otherwise ignored.</div>
        reason (Union[None, Unset, str]): <div class="apidocs-russian">Причина оприходования</div>
            <div class="apidocs-english">Reason</div>
        marking_codes (Union[None, Unset, list[str]]): <div class="apidocs-russian">Коды маркировки</div>
            <div class="apidocs-english">Marking codes</div>
    """

    quantity: float
    purchase_price: float
    id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    reason: Union[None, Unset, str] = UNSET
    marking_codes: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        purchase_price = self.purchase_price

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        marking_codes: Union[None, Unset, list[str]]
        if isinstance(self.marking_codes, Unset):
            marking_codes = UNSET
        elif isinstance(self.marking_codes, list):
            marking_codes = self.marking_codes

        else:
            marking_codes = self.marking_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "quantity": quantity,
                "purchasePrice": purchase_price,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if marking_codes is not UNSET:
            field_dict["markingCodes"] = marking_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        purchase_price = d.pop("purchasePrice")

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_marking_codes(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                marking_codes_type_0 = cast(list[str], data)

                return marking_codes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        marking_codes = _parse_marking_codes(d.pop("markingCodes", UNSET))

        nebular_api_controllers_v3_documents_management_create_management_document_request_position_v3 = cls(
            quantity=quantity,
            purchase_price=purchase_price,
            id=id,
            external_id=external_id,
            reason=reason,
            marking_codes=marking_codes,
        )

        return nebular_api_controllers_v3_documents_management_create_management_document_request_position_v3
