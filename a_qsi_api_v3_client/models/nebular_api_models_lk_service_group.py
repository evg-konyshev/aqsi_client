from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="NebularApiModelsLkServiceGroup")


@_attrs_define
class NebularApiModelsLkServiceGroup:
    """<div class="apidocs-russian">Группа клиента</div>
    <div class="apidocs-english">Client group</div>

        Attributes:
            id (UUID): <div class="apidocs-russian">Идентификатор группы</div>
                <div class="apidocs-english">Group Identifier</div>
    """

    id: UUID

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        nebular_api_models_lk_service_group = cls(
            id=id,
        )

        return nebular_api_models_lk_service_group
