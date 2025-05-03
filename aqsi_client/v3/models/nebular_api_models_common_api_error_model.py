from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiErrorModel")


@_attrs_define
class NebularApiModelsCommonApiErrorModel:
    """
    Attributes:
        errors (Union[None, Unset, list[str]]):
        code (Union[None, Unset, str]):
    """

    errors: Union[None, Unset, list[str]] = UNSET
    code: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        errors: Union[None, Unset, list[str]]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_errors(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        nebular_api_models_common_api_error_model = cls(
            errors=errors,
            code=code,
        )

        return nebular_api_models_common_api_error_model
