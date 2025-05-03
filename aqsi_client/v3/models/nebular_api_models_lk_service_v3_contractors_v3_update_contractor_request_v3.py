from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3")


@_attrs_define
class NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3:
    """
    Attributes:
        name (str): <div class="apidocs-russian">Наименование контрагента</div>
            <div class="apidocs-english">Contractors name</div>
        inn (Union[None, Unset, str]): <div class="apidocs-russian">Инн контрагента, 10-ти или 12-ти значное</div>
            <div class="apidocs-english">Contractors inn</div>
        phone (Union[None, Unset, str]): <div class="apidocs-russian">Телефон контрагента</div>
            <div class="apidocs-english">Contractors phone</div>
        email (Union[None, Unset, str]): <div class="apidocs-russian">Почта контрагента</div>
            <div class="apidocs-english">Contractors email</div>
    """

    name: str
    inn: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        inn: Union[None, Unset, str]
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if inn is not UNSET:
            field_dict["inn"] = inn
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        nebular_api_models_lk_service_v3_contractors_v3_update_contractor_request_v3 = cls(
            name=name,
            inn=inn,
            phone=phone,
            email=email,
        )

        return nebular_api_models_lk_service_v3_contractors_v3_update_contractor_request_v3
