from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiCustomerInfo")


@_attrs_define
class NebularApiModelsCommonApiCustomerInfo:
    """
    Attributes:
        birth_date (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Дата рождения покупателя (клиента) (в формате ГГГГ-ММ-ДД), 1243</div>
            <div class="apidocs-english tag-value">Customer birth date(YYYY-MM-DD), 1243</div>
        nationality (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Гражданство, 1244</div>
            <div class="apidocs-english tag-value">Nationality, 1244</div>
        doc_type (Union[None, Unset, int]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Код вида документа, удостоверяющего личность, 1245</div>
            <div class="apidocs-english tag-value">Identification document code, 1245</div>
        passport (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Данные документа, удостоверяющего личность, 1246</div>
            <div class="apidocs-english tag-value">Passport series and number, 1246</div>
        address (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Адрес покупателя (клиента), 1254</div>
            <div class="apidocs-english tag-value">Client address, 1254</div>
    """

    birth_date: Union[None, Unset, str] = UNSET
    nationality: Union[None, Unset, str] = UNSET
    doc_type: Union[None, Unset, int] = UNSET
    passport: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        birth_date: Union[None, Unset, str]
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = self.birth_date

        nationality: Union[None, Unset, str]
        if isinstance(self.nationality, Unset):
            nationality = UNSET
        else:
            nationality = self.nationality

        doc_type: Union[None, Unset, int]
        if isinstance(self.doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = self.doc_type

        passport: Union[None, Unset, str]
        if isinstance(self.passport, Unset):
            passport = UNSET
        else:
            passport = self.passport

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if passport is not UNSET:
            field_dict["passport"] = passport
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_birth_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        birth_date = _parse_birth_date(d.pop("birthDate", UNSET))

        def _parse_nationality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nationality = _parse_nationality(d.pop("nationality", UNSET))

        def _parse_doc_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        doc_type = _parse_doc_type(d.pop("docType", UNSET))

        def _parse_passport(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        passport = _parse_passport(d.pop("passport", UNSET))

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        nebular_api_models_common_api_customer_info = cls(
            birth_date=birth_date,
            nationality=nationality,
            doc_type=doc_type,
            passport=passport,
            address=address,
        )

        return nebular_api_models_common_api_customer_info
