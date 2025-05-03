from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceSlotInfo")


@_attrs_define
class NebularApiModelsLkServiceSlotInfo:
    """
    Attributes:
        slot_id (Union[Unset, int]): <div class="apidocs-russian">Идентификатор слота</div>
            <div class="apidocs-english">Slot identifier</div>
        is_blocked (Union[Unset, bool]): <div class="apidocs-russian">Заблокирован ли данный slotID</div>
            <div class="apidocs-english">Is this slotID blocked</div>
        max_value (Union[Unset, float]): <div class="apidocs-russian">Идентификатор слота</div>
            <div class="apidocs-english">Slot identifier</div>
    """

    slot_id: Union[Unset, int] = UNSET
    is_blocked: Union[Unset, bool] = UNSET
    max_value: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        slot_id = self.slot_id

        is_blocked = self.is_blocked

        max_value = self.max_value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if slot_id is not UNSET:
            field_dict["slotId"] = slot_id
        if is_blocked is not UNSET:
            field_dict["isBlocked"] = is_blocked
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slot_id = d.pop("slotId", UNSET)

        is_blocked = d.pop("isBlocked", UNSET)

        max_value = d.pop("maxValue", UNSET)

        nebular_api_models_lk_service_slot_info = cls(
            slot_id=slot_id,
            is_blocked=is_blocked,
            max_value=max_value,
        )

        return nebular_api_models_lk_service_slot_info
