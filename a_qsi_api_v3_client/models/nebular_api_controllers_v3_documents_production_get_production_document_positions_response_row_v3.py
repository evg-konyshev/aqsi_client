from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 import (
        NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3,
    )


T = TypeVar("T", bound="NebularApiControllersV3DocumentsProductionGetProductionDocumentPositionsResponseRowV3")


@_attrs_define
class NebularApiControllersV3DocumentsProductionGetProductionDocumentPositionsResponseRowV3:
    """
    Attributes:
        id (int): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        quantity (float): <div class="apidocs-russian">Количество</div>
            <div class="apidocs-english">Quantity</div>
        goods (Union['NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3', None, Unset]): <div
            class="apidocs-russian">Связанный товар из справочника товаров</div>
            <div class="apidocs-english">Related product from catalog</div>
    """

    id: int
    quantity: float
    goods: Union["NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3,
        )

        id = self.id

        quantity = self.quantity

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

        nebular_api_controllers_v3_documents_production_get_production_document_positions_response_row_v3 = cls(
            id=id,
            quantity=quantity,
            goods=goods,
        )

        return nebular_api_controllers_v3_documents_production_get_production_document_positions_response_row_v3
