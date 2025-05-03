import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiOperationalAttribute")


@_attrs_define
class NebularApiModelsCommonApiOperationalAttribute:
    """<div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
    <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
    <div class="apidocs-russian">Операционный реквизит чека, 1270</div>
    <div class="apidocs-english">Receipt operational attribute, 1270</div>

        Attributes:
            id (Union[None, Unset, int]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
                <div class="apidocs-russian tag-value">Идентификатор операции, 1271</div>
                <div class="apidocs-english tag-value">Operation id, 1271</div>
            value (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
                1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
                <div class="apidocs-russian tag-value">Данные операции, 1272</div>
                <div class="apidocs-english tag-value">Operation data, 1272</div>
            date (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
                <div class="apidocs-russian tag-value">Дата, время операции, 1273</div>
                <div class="apidocs-english tag-value">Operation date and time, 1273</div>
    """

    id: Union[None, Unset, int] = UNSET
    value: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        nebular_api_models_common_api_operational_attribute = cls(
            id=id,
            value=value,
            date=date,
        )

        return nebular_api_models_common_api_operational_attribute
