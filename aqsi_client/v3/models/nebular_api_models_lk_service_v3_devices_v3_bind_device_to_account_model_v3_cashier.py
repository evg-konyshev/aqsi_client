from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3Cashier:
    """
    Attributes:
        id (Union[None, UUID, Unset]): Идентификатор кассира.
            ! Обязательно, если не передан externalId.
        external_id (Union[None, Unset, str]): Внешний идентификатор кассира.
            ! Обязательно, если не передан id, иначе игнорируется.
    """

    id: Union[None, UUID, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_cashier = cls(
            id=id,
            external_id=external_id,
        )

        return nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3_cashier
