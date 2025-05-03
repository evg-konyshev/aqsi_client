from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiGuidModel")


@_attrs_define
class NebularApiModelsCommonApiGuidModel:
    """
    Example:
        {'guid': '00000000-0000-0000-0000-000000000000'}

    Attributes:
        guid (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Identifier</div>
    """

    guid: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        guid: Union[None, Unset, str]
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_guid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guid = _parse_guid(d.pop("guid", UNSET))

        nebular_api_models_common_api_guid_model = cls(
            guid=guid,
        )

        return nebular_api_models_common_api_guid_model
