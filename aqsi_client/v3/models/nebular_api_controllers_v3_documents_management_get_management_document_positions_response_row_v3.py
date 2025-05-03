from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 import (
        NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3,
    )


T = TypeVar("T", bound="NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3")


@_attrs_define
class NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3:
    """
    Attributes:
        id (int): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        quantity (float): <div class="apidocs-russian">Количество</div>
            <div class="apidocs-english">Quantity</div>
        purchase_price (Union[None, Unset, float]): <div class="apidocs-russian">Цена закупки</div>
            <div class="apidocs-english">Purchase price</div>
        reason (Union[None, Unset, str]): <div class="apidocs-russian">Причина оприходования</div>
            <div class="apidocs-english">Reason</div>
        marking_codes (Union[None, Unset, list[str]]): <div class="apidocs-russian">Коды маркировки ! Существует у всех
            документов, кроме Производства</div>
            <div class="apidocs-english">Marking codes</div>
        goods (Union['NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3', None, Unset]): <div
            class="apidocs-russian">Связанный товар из справочника товаров</div>
            <div class="apidocs-english">Related product from catalog</div>
    """

    id: int
    quantity: float
    purchase_price: Union[None, Unset, float] = UNSET
    reason: Union[None, Unset, str] = UNSET
    marking_codes: Union[None, Unset, list[str]] = UNSET
    goods: Union["NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3,
        )

        id = self.id

        quantity = self.quantity

        purchase_price: Union[None, Unset, float]
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        else:
            purchase_price = self.purchase_price

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

        goods: Union[None, Unset, dict[str, Any]]
        if isinstance(self.goods, Unset):
            goods = UNSET
        elif isinstance(self.goods, NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3):
            goods = self.goods.to_dict()
        else:
            goods = self.goods

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "quantity": quantity,
            }
        )
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if reason is not UNSET:
            field_dict["reason"] = reason
        if marking_codes is not UNSET:
            field_dict["markingCodes"] = marking_codes
        if goods is not UNSET:
            field_dict["goods"] = goods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3,
        )

        d = dict(src_dict)
        id = d.pop("id")

        quantity = d.pop("quantity")

        def _parse_purchase_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))

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

        def _parse_goods(
            data: object,
        ) -> Union["NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                goods_type_1 = NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3.from_dict(data)

                return goods_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union["NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3", None, Unset], data
            )

        goods = _parse_goods(d.pop("goods", UNSET))

        nebular_api_controllers_v3_documents_management_get_management_document_positions_response_row_v3 = cls(
            id=id,
            quantity=quantity,
            purchase_price=purchase_price,
            reason=reason,
            marking_codes=marking_codes,
            goods=goods,
        )

        return nebular_api_controllers_v3_documents_management_get_management_document_positions_response_row_v3
