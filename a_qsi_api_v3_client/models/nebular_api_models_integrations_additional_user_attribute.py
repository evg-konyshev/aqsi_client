from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsIntegrationsAdditionalUserAttribute")


@_attrs_define
class NebularApiModelsIntegrationsAdditionalUserAttribute:
    """<div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
    <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
    <div class="apidocs-russian">Дополнительный реквизит пользователя, 1084</div>
    <div class="apidocs-english">Additional user attribute, 1084</div>

        Attributes:
            name (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
                ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Наименование дополнительного реквизита пользователя, 1085</div>
                <div class="apidocs-english tag-value">Name of the additional user attribute, 1085</div>
            value (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
                ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Значение дополнительного реквизита пользователя, 1086</div>
                <div class="apidocs-english tag-value">The value of the additional user attribute, 1086</div>
    """

    name: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        nebular_api_models_integrations_additional_user_attribute = cls(
            name=name,
            value=value,
        )

        return nebular_api_models_integrations_additional_user_attribute
