from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3ErrorV3")


@_attrs_define
class NebularApiModelsLkServiceV3ErrorV3:
    """
    Attributes:
        message (str): <div class="apidocs-russian">Текст ошибки</div>
            <div class="apidocs-english">Error message</div>
        location (str): <div class="apidocs-russian">Расположение ошибки. Допустимые значения: `body`, `params`,
            `query`, `cookies`, `headers`.</div>
            <div class="apidocs-english">Error location. Possible values: `body`, `params`, `query`, `cookies`,
            `headers`.</div>
        path (Union[None, Unset, list[str]]): <div class="apidocs-russian">Путь к ошибочному значению</div>
            <div class="apidocs-english">Ordered array where each element is the accessor to the value where the error
            happened</div>
    """

    message: str
    location: str
    path: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        location = self.location

        path: Union[None, Unset, list[str]]
        if isinstance(self.path, Unset):
            path = UNSET
        elif isinstance(self.path, list):
            path = self.path

        else:
            path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "message": message,
                "location": location,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        location = d.pop("location")

        def _parse_path(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                path_type_0 = cast(list[str], data)

                return path_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        path = _parse_path(d.pop("path", UNSET))

        nebular_api_models_lk_service_v3_error_v3 = cls(
            message=message,
            location=location,
            path=path,
        )

        return nebular_api_models_lk_service_v3_error_v3
