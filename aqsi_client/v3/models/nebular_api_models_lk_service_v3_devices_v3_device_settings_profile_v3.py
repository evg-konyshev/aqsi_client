from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор профиля настроек</div>
            <div class="apidocs-english"></div>
    """

    id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        nebular_api_models_lk_service_v3_devices_v3_device_settings_profile_v3 = cls(
            id=id,
        )

        return nebular_api_models_lk_service_v3_devices_v3_device_settings_profile_v3
