import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiDateTimeModel")


@_attrs_define
class NebularApiModelsCommonApiDateTimeModel:
    """
    Example:
        {'dateTime': '2025-04-29T20:13:37.5863697+00:00'}

    Attributes:
        date_time (Union[Unset, datetime.datetime]):
    """

    date_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        date_time: Union[Unset, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, datetime.datetime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        nebular_api_models_common_api_date_time_model = cls(
            date_time=date_time,
        )

        return nebular_api_models_common_api_date_time_model
