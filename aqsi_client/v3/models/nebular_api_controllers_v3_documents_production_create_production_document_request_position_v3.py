from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiControllersV3DocumentsProductionCreateProductionDocumentRequestPositionV3")


@_attrs_define
class NebularApiControllersV3DocumentsProductionCreateProductionDocumentRequestPositionV3:
    """
    Attributes:
        quantity (float): <div class="apidocs-russian">Количество. Макс. кол-во знаков после запятой: 3.</div>
            <div class="apidocs-english">Quantity. Precision: 3.</div>
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор товара из справочника товаров.
            Обязательно, если не передан externalId.</div>
            <div class="apidocs-english">Good id from catalog. Required when externalId missing.</div>
        external_id (Union[None, Unset, str]): <div class="apidocs-russian">Внешний идентификатор товара из справочника
            товаров. Обязательно, если не передан id, иначе игнорируется.</div>
            <div class="apidocs-english">Good external id from catalog. Required when id missing, otherwise ignored.</div>
    """

    quantity: float
    id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

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

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "quantity": quantity,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

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

        nebular_api_controllers_v3_documents_production_create_production_document_request_position_v3 = cls(
            quantity=quantity,
            id=id,
            external_id=external_id,
        )

        return nebular_api_controllers_v3_documents_production_create_production_document_request_position_v3
