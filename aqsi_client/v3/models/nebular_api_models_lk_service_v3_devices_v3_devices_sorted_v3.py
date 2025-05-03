from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Ключ сортировки. Допустимые значения: <b>"id"</b>,
            <b>"activationDate"</b>, <b>"model"</b>.</div>
            <div class="apidocs-english">Sorting key. Allowed values: <b>"id"</b>, <b>"activationDate"</b>,
            <b>"model"</b>.</div>
        desc (Union[Unset, bool]): <div class="apidocs-russian">Направление сортировки. По умолчанию: <b>false</b></div>
            <div class="apidocs-english">Sort direction. Default: <b>false</b></div>
    """

    id: str
    desc: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        desc = self.desc

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        desc = d.pop("desc", UNSET)

        nebular_api_models_lk_service_v3_devices_v3_devices_sorted_v3 = cls(
            id=id,
            desc=desc,
        )

        return nebular_api_models_lk_service_v3_devices_v3_devices_sorted_v3
