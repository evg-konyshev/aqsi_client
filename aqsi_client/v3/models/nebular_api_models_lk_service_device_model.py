from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar("T", bound="NebularApiModelsLkServiceDeviceModel")


@_attrs_define
class NebularApiModelsLkServiceDeviceModel:
    """Модель устройства

    Attributes:
        id (Union[Unset, int]): <div class="apidocs-russian">Идентификатор устройства</div>
            <div class="apidocs-english">Device identifier</div>
        imei (Union[Unset, int]): <div class="apidocs-russian">Имей устройства</div>
            <div class="apidocs-english">Device IMEI</div>
        device_sn (Union[None, Unset, str]): <div class="apidocs-russian">Серийный номер устройства</div>
            <div class="apidocs-english">Device serial number</div>
        shop_id (Union[None, Unset, int]): <div class="apidocs-russian">Идентификатор магазина, если устройство не
            привязано к магазину - null</div>
            <div class="apidocs-english">Store identifier, if the device is not attached to the store - null</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
    """

    id: Union[Unset, int] = UNSET
    imei: Union[Unset, int] = UNSET
    device_sn: Union[None, Unset, str] = UNSET
    shop_id: Union[None, Unset, int] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        imei = self.imei

        device_sn: Union[None, Unset, str]
        if isinstance(self.device_sn, Unset):
            device_sn = UNSET
        else:
            device_sn = self.device_sn

        shop_id: Union[None, Unset, int]
        if isinstance(self.shop_id, Unset):
            shop_id = UNSET
        else:
            shop_id = self.shop_id

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if imei is not UNSET:
            field_dict["imei"] = imei
        if device_sn is not UNSET:
            field_dict["deviceSn"] = device_sn
        if shop_id is not UNSET:
            field_dict["shopId"] = shop_id
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        imei = d.pop("imei", UNSET)

        def _parse_device_sn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_sn = _parse_device_sn(d.pop("deviceSn", UNSET))

        def _parse_shop_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shop_id = _parse_shop_id(d.pop("shopId", UNSET))

        def _parse_custom_properties(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]]:
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
                    custom_properties_type_0_item = NebularApiModelsLkServiceCustomProperty.from_dict(
                        custom_properties_type_0_item_data
                    )

                    custom_properties_type_0.append(custom_properties_type_0_item)

                return custom_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]], data)

        custom_properties = _parse_custom_properties(d.pop("customProperties", UNSET))

        nebular_api_models_lk_service_device_model = cls(
            id=id,
            imei=imei,
            device_sn=device_sn,
            shop_id=shop_id,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_device_model
