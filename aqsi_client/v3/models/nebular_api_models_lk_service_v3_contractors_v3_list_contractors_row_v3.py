from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceV3ContractorsV3ListContractorsRowV3")


@_attrs_define
class NebularApiModelsLkServiceV3ContractorsV3ListContractorsRowV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        external_id (str): <div class="apidocs-russian">Внешний идентификатор</div>
            <div class="apidocs-english">External id</div>
        name (str): <div class="apidocs-russian">Наименование контрагента</div>
            <div class="apidocs-english">Contractors name</div>
        updated_at (str): <div class="apidocs-russian">Дата и время последнего обновления</div>
            <div class="apidocs-english">Date and time of last update</div>
        inn (Union[None, Unset, str]): <div class="apidocs-russian">Инн контрагента, 10-ти или 12-ти значное</div>
            <div class="apidocs-english">Contractors inn</div>
        phone (Union[None, Unset, str]): <div class="apidocs-russian">Телефон контрагента</div>
            <div class="apidocs-english">Contractors phone</div>
        email (Union[None, Unset, str]): <div class="apidocs-russian">Почта контрагента</div>
            <div class="apidocs-english">Contractors email</div>
    """

    id: str
    external_id: str
    name: str
    updated_at: str
    inn: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        name = self.name

        updated_at = self.updated_at

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
                "id": id,
                "externalId": external_id,
                "name": name,
                "updatedAt": updated_at,
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
        id = d.pop("id")

        external_id = d.pop("externalId")

        name = d.pop("name")

        updated_at = d.pop("updatedAt")

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

        nebular_api_models_lk_service_v3_contractors_v3_list_contractors_row_v3 = cls(
            id=id,
            external_id=external_id,
            name=name,
            updated_at=updated_at,
            inn=inn,
            phone=phone,
            email=email,
        )

        return nebular_api_models_lk_service_v3_contractors_v3_list_contractors_row_v3
