from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 import (
        NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3,
    )


T = TypeVar("T", bound="NebularApiControllersV3DocumentsProductionGetProductionDocumentResponseV3")


@_attrs_define
class NebularApiControllersV3DocumentsProductionGetProductionDocumentResponseV3:
    """
    Attributes:
        warehouse (NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3):
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        external_id (str): <div class="apidocs-russian">Внешний идентификатор</div>
            <div class="apidocs-english">External id</div>
        number (int): <div class="apidocs-russian">Номер документа</div>
            <div class="apidocs-english">Document number</div>
        date_time (str): <div class="apidocs-russian">Дата документа</div>
            <div class="apidocs-english">Document date</div>
        status (str): <div class="apidocs-russian">Статус документа. Допустимые значения: <b>"draft"</b>,
            <b>"complete"</b>.</div>
            <div class="apidocs-english">Document status. Allowed values: <b>"draft"</b>, <b>"complete"</b>.</div>
        is_edo (bool): <div class="apidocs-russian">Флаг ЭДО</div>
            <div class="apidocs-english">Is document from EDO</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий</div>
            <div class="apidocs-english">Comment</div>
    """

    warehouse: "NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3"
    id: str
    external_id: str
    number: int
    date_time: str
    status: str
    is_edo: bool
    comment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        warehouse = self.warehouse.to_dict()

        id = self.id

        external_id = self.external_id

        number = self.number

        date_time = self.date_time

        status = self.status

        is_edo = self.is_edo

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "warehouse": warehouse,
                "id": id,
                "externalId": external_id,
                "number": number,
                "dateTime": date_time,
                "status": status,
                "isEdo": is_edo,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 import (
            NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3,
        )

        d = dict(src_dict)
        warehouse = NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3.from_dict(d.pop("warehouse"))

        id = d.pop("id")

        external_id = d.pop("externalId")

        number = d.pop("number")

        date_time = d.pop("dateTime")

        status = d.pop("status")

        is_edo = d.pop("isEdo")

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        nebular_api_controllers_v3_documents_production_get_production_document_response_v3 = cls(
            warehouse=warehouse,
            id=id,
            external_id=external_id,
            number=number,
            date_time=date_time,
            status=status,
            is_edo=is_edo,
            comment=comment,
        )

        return nebular_api_controllers_v3_documents_production_get_production_document_response_v3
