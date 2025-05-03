from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_devices_v3_device_settings_profile_v3 import (
        NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор настроек</div>
            <div class="apidocs-english"></div>
        device_settings_profile (Union['NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3', None, Unset]):
            <div class="apidocs-russian">Профиль настроек устройства.Если профиль null, то настройки являются
            индивидуальными.Если заполнено, то настройки являются настройками профиля.</div>
            <div class="apidocs-english"></div>
    """

    id: str
    device_settings_profile: Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_device_settings_profile_v3 import (
            NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3,
        )

        id = self.id

        device_settings_profile: Union[None, Unset, dict[str, Any]]
        if isinstance(self.device_settings_profile, Unset):
            device_settings_profile = UNSET
        elif isinstance(self.device_settings_profile, NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3):
            device_settings_profile = self.device_settings_profile.to_dict()
        else:
            device_settings_profile = self.device_settings_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if device_settings_profile is not UNSET:
            field_dict["deviceSettingsProfile"] = device_settings_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_device_settings_profile_v3 import (
            NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_device_settings_profile(
            data: object,
        ) -> Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_settings_profile_type_1 = NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3.from_dict(
                    data
                )

                return device_settings_profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingsProfileV3", None, Unset], data)

        device_settings_profile = _parse_device_settings_profile(d.pop("deviceSettingsProfile", UNSET))

        nebular_api_models_lk_service_v3_devices_v3_device_setting_v3 = cls(
            id=id,
            device_settings_profile=device_settings_profile,
        )

        return nebular_api_models_lk_service_v3_devices_v3_device_setting_v3
