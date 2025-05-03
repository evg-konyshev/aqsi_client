from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsIntegrationsSupplierInfo")


@_attrs_define
class NebularApiModelsIntegrationsSupplierInfo:
    """<div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
    <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
    <div class="apidocs-russian">Данные поставщика, 1224</div>
    <div class="apidocs-english">Supplier info, 1224</div>

        Attributes:
            name (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
                ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Наименование поставщика, 1225</div>
                <div class="apidocs-english tag-value">Supplier name, 1225</div>
            phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Телефон поставщика, 1171. Массив строк длиной от 1 до 19 символов</div>
                <div class="apidocs-english tag-value">Supplier's phone number, 1171. An array of strings from 1 to 19
                characters length</div>
    """

    name: Union[None, Unset, str] = UNSET
    phone_numbers: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = self.phone_numbers

        else:
            phone_numbers = self.phone_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers

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

        def _parse_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = cast(list[str], data)

                return phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        phone_numbers = _parse_phone_numbers(d.pop("phoneNumbers", UNSET))

        nebular_api_models_integrations_supplier_info = cls(
            name=name,
            phone_numbers=phone_numbers,
        )

        return nebular_api_models_integrations_supplier_info
