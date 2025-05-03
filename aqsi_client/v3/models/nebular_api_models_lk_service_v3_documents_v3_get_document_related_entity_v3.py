from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3")


@_attrs_define
class NebularApiModelsLkServiceV3DocumentsV3GetDocumentRelatedEntityV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        external_id (str): <div class="apidocs-russian">Внешний идентификатор</div>
            <div class="apidocs-english">External id</div>
        name (str): <div class="apidocs-russian">Наименование </div>
            <div class="apidocs-english">Name</div>
        deleted_at (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время удаления</div>
            <div class="apidocs-english">Deletion date and time</div>
    """

    id: str
    external_id: str
    name: str
    deleted_at: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        name = self.name

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
                "name": name,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("externalId")

        name = d.pop("name")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3 = cls(
            id=id,
            external_id=external_id,
            name=name,
            deleted_at=deleted_at,
        )

        return nebular_api_models_lk_service_v3_documents_v3_get_document_related_entity_v3
