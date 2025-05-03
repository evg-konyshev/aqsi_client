from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_cashier import (
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier,
    )
    from ..models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_shop import (
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3:
    """
    Attributes:
        shop (Union['NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop', None, Unset]): Магазин. Касса
            будет привязана к нему.
        cashiers (Union[None, Unset, list['NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier']]):
            Массив кассиров. Они будут привязаны к кассе. Один из них должен быть с правами "Администратор".
    """

    shop: Union["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop", None, Unset] = UNSET
    cashiers: Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_shop import (
            NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop,
        )

        shop: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shop, Unset):
            shop = UNSET
        elif isinstance(self.shop, NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop):
            shop = self.shop.to_dict()
        else:
            shop = self.shop

        cashiers: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.cashiers, Unset):
            cashiers = UNSET
        elif isinstance(self.cashiers, list):
            cashiers = []
            for cashiers_type_0_item_data in self.cashiers:
                cashiers_type_0_item = cashiers_type_0_item_data.to_dict()
                cashiers.append(cashiers_type_0_item)

        else:
            cashiers = self.cashiers

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if shop is not UNSET:
            field_dict["shop"] = shop
        if cashiers is not UNSET:
            field_dict["cashiers"] = cashiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_cashier import (
            NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier,
        )
        from ..models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_shop import (
            NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop,
        )

        d = dict(src_dict)

        def _parse_shop(
            data: object,
        ) -> Union["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shop_type_1 = NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop.from_dict(data)

                return shop_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Shop", None, Unset], data)

        shop = _parse_shop(d.pop("shop", UNSET))

        def _parse_cashiers(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cashiers_type_0 = []
                _cashiers_type_0 = data
                for cashiers_type_0_item_data in _cashiers_type_0:
                    cashiers_type_0_item = (
                        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier.from_dict(
                            cashiers_type_0_item_data
                        )
                    )

                    cashiers_type_0.append(cashiers_type_0_item)

                return cashiers_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier"]], data
            )

        cashiers = _parse_cashiers(d.pop("cashiers", UNSET))

        nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3 = cls(
            shop=shop,
            cashiers=cashiers,
        )

        return nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3
