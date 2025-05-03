from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_devices_v3_device_setting_v3 import (
        NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3,
    )
    from ..models.nebular_api_models_lk_service_v3_devices_v3_devices_v3_custom_property import (
        NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty,
    )
    from ..models.nebular_api_models_lk_service_v3_devices_v3_devices_v3_shop import (
        NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3GetDeviceResponseV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3GetDeviceResponseV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        imei (str): <div class="apidocs-russian">IMEI</div>
            <div class="apidocs-english">IMEI</div>
        created_at (str): <div class="apidocs-russian">Дата создания</div>
            <div class="apidocs-english"></div>
        updated_at (str): <div class="apidocs-russian">Дата обновления</div>
            <div class="apidocs-english"></div>
        serial_number (Union[None, Unset, str]): <div class="apidocs-russian">Серийный номер устройства</div>
            <div class="apidocs-english">Device serial number</div>
        fs_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер ФН</div>
            <div class="apidocs-english"></div>
        board_serial_number (Union[None, Unset, str]): <div class="apidocs-russian">Заводской номер</div>
            <div class="apidocs-english"></div>
        model (Union[None, Unset, str]): <div class="apidocs-russian">Модель устройства</div>
            <div class="apidocs-english">Device model</div>
        activation_date (Union[None, Unset, str]): <div class="apidocs-russian">Дата активации устройства в формате
            YYYY-MM-DD</div>
            <div class="apidocs-english">Activation date, formt YYYY-MM-DD</div>
        device_setting (Union['NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3', None, Unset]): <div class="apidocs-
            russian">Настройки устройства</div>
            <div class="apidocs-english">Device setting</div>
        shop (Union['NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop', None, Unset]): <div class="apidocs-
            russian">Магазин, в котором находится устройство</div>
            <div class="apidocs-english">Device shop</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty']]):
            <div class="apidocs-russian">Дополнительные параметры</div>
            <div class="apidocs-english">Additional device parameters</div>
    """

    id: str
    imei: str
    created_at: str
    updated_at: str
    serial_number: Union[None, Unset, str] = UNSET
    fs_number: Union[None, Unset, str] = UNSET
    board_serial_number: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    activation_date: Union[None, Unset, str] = UNSET
    device_setting: Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3", None, Unset] = UNSET
    shop: Union["NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop", None, Unset] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_device_setting_v3 import (
            NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3,
        )
        from ..models.nebular_api_models_lk_service_v3_devices_v3_devices_v3_shop import (
            NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop,
        )

        id = self.id

        imei = self.imei

        created_at = self.created_at

        updated_at = self.updated_at

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        fs_number: Union[None, Unset, str]
        if isinstance(self.fs_number, Unset):
            fs_number = UNSET
        else:
            fs_number = self.fs_number

        board_serial_number: Union[None, Unset, str]
        if isinstance(self.board_serial_number, Unset):
            board_serial_number = UNSET
        else:
            board_serial_number = self.board_serial_number

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        activation_date: Union[None, Unset, str]
        if isinstance(self.activation_date, Unset):
            activation_date = UNSET
        else:
            activation_date = self.activation_date

        device_setting: Union[None, Unset, dict[str, Any]]
        if isinstance(self.device_setting, Unset):
            device_setting = UNSET
        elif isinstance(self.device_setting, NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3):
            device_setting = self.device_setting.to_dict()
        else:
            device_setting = self.device_setting

        shop: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shop, Unset):
            shop = UNSET
        elif isinstance(self.shop, NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop):
            shop = self.shop.to_dict()
        else:
            shop = self.shop

        custom_properties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_properties, Unset):
            custom_properties = UNSET
        elif isinstance(self.custom_properties, list):
            custom_properties = []
            for custom_properties_type_0_item_data in self.custom_properties:
                custom_properties_type_0_item = custom_properties_type_0_item_data.to_dict()
                custom_properties.append(custom_properties_type_0_item)

        else:
            custom_properties = self.custom_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "imei": imei,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if fs_number is not UNSET:
            field_dict["fsNumber"] = fs_number
        if board_serial_number is not UNSET:
            field_dict["boardSerialNumber"] = board_serial_number
        if model is not UNSET:
            field_dict["model"] = model
        if activation_date is not UNSET:
            field_dict["activationDate"] = activation_date
        if device_setting is not UNSET:
            field_dict["deviceSetting"] = device_setting
        if shop is not UNSET:
            field_dict["shop"] = shop
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_device_setting_v3 import (
            NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3,
        )
        from ..models.nebular_api_models_lk_service_v3_devices_v3_devices_v3_custom_property import (
            NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty,
        )
        from ..models.nebular_api_models_lk_service_v3_devices_v3_devices_v3_shop import (
            NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop,
        )

        d = dict(src_dict)
        id = d.pop("id")

        imei = d.pop("imei")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        def _parse_fs_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fs_number = _parse_fs_number(d.pop("fsNumber", UNSET))

        def _parse_board_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        board_serial_number = _parse_board_serial_number(d.pop("boardSerialNumber", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_activation_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activation_date = _parse_activation_date(d.pop("activationDate", UNSET))

        def _parse_device_setting(
            data: object,
        ) -> Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_setting_type_1 = NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3.from_dict(data)

                return device_setting_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceV3DevicesV3DeviceSettingV3", None, Unset], data)

        device_setting = _parse_device_setting(d.pop("deviceSetting", UNSET))

        def _parse_shop(data: object) -> Union["NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shop_type_1 = NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop.from_dict(data)

                return shop_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceV3DevicesV3DevicesV3Shop", None, Unset], data)

        shop = _parse_shop(d.pop("shop", UNSET))

        def _parse_custom_properties(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_properties_type_0 = []
                _custom_properties_type_0 = data
                for custom_properties_type_0_item_data in _custom_properties_type_0:
                    custom_properties_type_0_item = (
                        NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty.from_dict(
                            custom_properties_type_0_item_data
                        )
                    )

                    custom_properties_type_0.append(custom_properties_type_0_item)

                return custom_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesV3CustomProperty"]], data)

        custom_properties = _parse_custom_properties(d.pop("customProperties", UNSET))

        nebular_api_models_lk_service_v3_devices_v3_get_device_response_v3 = cls(
            id=id,
            imei=imei,
            created_at=created_at,
            updated_at=updated_at,
            serial_number=serial_number,
            fs_number=fs_number,
            board_serial_number=board_serial_number,
            model=model,
            activation_date=activation_date,
            device_setting=device_setting,
            shop=shop,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_v3_devices_v3_get_device_response_v3
