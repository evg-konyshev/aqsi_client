from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_error_v3 import NebularApiModelsLkServiceV3ErrorV3


T = TypeVar("T", bound="NebularApiModelsLkServiceV3ErrorModelV3")


@_attrs_define
class NebularApiModelsLkServiceV3ErrorModelV3:
    """
    Attributes:
        message (str): <div class="apidocs-russian">Описание ошибки</div>
            <div class="apidocs-english">Error description</div>
        reason (str): <div class="apidocs-russian">Краткая причина ошибки</div>
            <div class="apidocs-english">Error reason</div>
        errors (Union[None, Unset, list['NebularApiModelsLkServiceV3ErrorV3']]): <div class="apidocs-russian">Список
            расширенных ошибок</div>
            <div class="apidocs-english">Extended errors list</div>
    """

    message: str
    reason: str
    errors: Union[None, Unset, list["NebularApiModelsLkServiceV3ErrorV3"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        reason = self.reason

        errors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "message": message,
                "reason": reason,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_error_v3 import NebularApiModelsLkServiceV3ErrorV3

        d = dict(src_dict)
        message = d.pop("message")

        reason = d.pop("reason")

        def _parse_errors(data: object) -> Union[None, Unset, list["NebularApiModelsLkServiceV3ErrorV3"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = NebularApiModelsLkServiceV3ErrorV3.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceV3ErrorV3"]], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        nebular_api_models_lk_service_v3_error_model_v3 = cls(
            message=message,
            reason=reason,
            errors=errors,
        )

        return nebular_api_models_lk_service_v3_error_model_v3
