from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_payment_subject_type_enum import NebularApiEnumsPaymentSubjectTypeEnum
from ..models.nebular_api_enums_unit_code_enum import NebularApiEnumsUnitCodeEnum
from ..models.nebular_api_enums_vat_rate_enum import NebularApiEnumsVATRateEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 import (
        NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3")


@_attrs_define
class NebularApiModelsLkServiceV3DocumentsV3DocumentPositionsResponseRowGoodV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        external_id (str): <div class="apidocs-russian">Внешний идентификатор</div>
            <div class="apidocs-english">External id</div>
        name (str): <div class="apidocs-russian">Наименование </div>
            <div class="apidocs-english">Name</div>
        unit (str): <div class="apidocs-russian">Единица измерения (тэг 1197)</div>
            <div class="apidocs-english">Unit of measurement (tag 1197)</div>
        unit_code (NebularApiEnumsUnitCodeEnum): Единица измерения предмета расчета
        subject (NebularApiEnumsPaymentSubjectTypeEnum): Предмет расчета, 1212
        tax (NebularApiEnumsVATRateEnum): Ставка НДС, 1199
        barcodes (list[str]): <div class="apidocs-russian tag-value">Штрихкоды</div>
            <div class="apidocs-english tag-value">Good barcodes list</div>
        sku (Union[None, Unset, str]): <div class="apidocs-russian">Артикул</div>
            <div class="apidocs-english">Article</div>
        last_purchase_price (Union[None, Unset, float]): <div class="apidocs-russian tag-value">Последняя цена
            закупки</div>
            <div class="apidocs-english tag-value">Last purchase price</div>
        deleted_at (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время удаления</div>
            <div class="apidocs-english">Deletion date and time</div>
        group (Union['NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3', None, Unset]): <div
            class="apidocs-russian">Группа товара</div>
            <div class="apidocs-english">Good category</div>
    """

    id: str
    external_id: str
    name: str
    unit: str
    unit_code: NebularApiEnumsUnitCodeEnum
    subject: NebularApiEnumsPaymentSubjectTypeEnum
    tax: NebularApiEnumsVATRateEnum
    barcodes: list[str]
    sku: Union[None, Unset, str] = UNSET
    last_purchase_price: Union[None, Unset, float] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    group: Union["NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3,
        )

        id = self.id

        external_id = self.external_id

        name = self.name

        unit = self.unit

        unit_code = self.unit_code.value

        subject = self.subject.value

        tax = self.tax.value

        barcodes = self.barcodes

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        last_purchase_price: Union[None, Unset, float]
        if isinstance(self.last_purchase_price, Unset):
            last_purchase_price = UNSET
        else:
            last_purchase_price = self.last_purchase_price

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3):
            group = self.group.to_dict()
        else:
            group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
                "name": name,
                "unit": unit,
                "unitCode": unit_code,
                "subject": subject,
                "tax": tax,
                "barcodes": barcodes,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if last_purchase_price is not UNSET:
            field_dict["lastPurchasePrice"] = last_purchase_price
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3,
        )

        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("externalId")

        name = d.pop("name")

        unit = d.pop("unit")

        unit_code = NebularApiEnumsUnitCodeEnum(d.pop("unitCode"))

        subject = NebularApiEnumsPaymentSubjectTypeEnum(d.pop("subject"))

        tax = NebularApiEnumsVATRateEnum(d.pop("tax"))

        barcodes = cast(list[str], d.pop("barcodes"))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_last_purchase_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_purchase_price = _parse_last_purchase_price(d.pop("lastPurchasePrice", UNSET))

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        def _parse_group(
            data: object,
        ) -> Union["NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

        nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3 = cls(
            id=id,
            external_id=external_id,
            name=name,
            unit=unit,
            unit_code=unit_code,
            subject=subject,
            tax=tax,
            barcodes=barcodes,
            sku=sku,
            last_purchase_price=last_purchase_price,
            deleted_at=deleted_at,
            group=group,
        )

        return nebular_api_models_lk_service_v3_documents_v3_document_positions_response_row_good_v3
