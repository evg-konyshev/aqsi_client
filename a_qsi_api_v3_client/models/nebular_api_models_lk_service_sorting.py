from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceSorting")


@_attrs_define
class NebularApiModelsLkServiceSorting:
    """
    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Название поля для сортировки из модели</div>
            <div class="apidocs-english">Field name to sort</div>
        desc (Union[Unset, bool]): <div class="apidocs-russian">Признак сортировки по убыванию (true - сортировать по
            убыванию, false - по возрастанию)</div>
            <div class="apidocs-english">Descending sorting flag (true - descending sorting, false - ascending
            sorting)</div>
    """

    id: Union[None, Unset, str] = UNSET
    desc: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        desc = self.desc

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        desc = d.pop("desc", UNSET)

        nebular_api_models_lk_service_sorting = cls(
            id=id,
            desc=desc,
        )

        return nebular_api_models_lk_service_sorting
