import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_group import NebularApiModelsLkServiceGroup


T = TypeVar("T", bound="NebularApiModelsLkServiceClient")


@_attrs_define
class NebularApiModelsLkServiceClient:
    """
    Example:
        {'group': {'id': '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone': '88005553535', 'additionalPhone':
            None, 'email': 'ivanov@example.com', 'comment': 'Оставляет чаевые', 'passport': '4608999777', 'docType': None,
            'nationality': None, 'address': None}

    Attributes:
        group (NebularApiModelsLkServiceGroup): <div class="apidocs-russian">Группа клиента</div>
            <div class="apidocs-english">Client group</div>
        fio (Union[None, Unset, str]): <div class="apidocs-russian">Имя клиента</div>
            <div class="apidocs-english">Client name</div>
        gender (Union[Unset, int]): <div class="apidocs-russian">
                        Пол клиента (0 - женский, 1 - мужской)
                        По умолчанию: 1
                        Допустимые значения: 0, 1</div>
            <div class="apidocs-english">Client gender (0 - female, 1 - male)
                        Default: 1
                        Allowed values: 0, 1</div>
        inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
            ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian">ИНН клиента, 1228</div>
            <div class="apidocs-english">Client TIN, 1228</div>
        birth_date (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian">Дата рождения, 1243</div>
            <div class="apidocs-english">Date of Birth, 1243</div>
        main_phone (Union[None, Unset, str]): <div class="apidocs-russian">Основной телефон</div>
            <div class="apidocs-english">Primary phone number</div>
        additional_phone (Union[None, Unset, str]): <div class="apidocs-russian">Дополнительный телефон</div>
            <div class="apidocs-english">Additional phone number</div>
        email (Union[None, Unset, str]): <div class="apidocs-russian">Электронная почта</div>
            <div class="apidocs-english">E-mail</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий</div>
            <div class="apidocs-english">Comment</div>
        passport (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian">Cерия и номер паспорта, 1246</div>
            <div class="apidocs-english">Passport series and number, 1246</div>
        doc_type (Union[None, Unset, int]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian">Код вида документа, удостоверяющего личность, 1245</div>
            <div class="apidocs-english">Identification document code, 1245</div>
        nationality (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian">Гражданство, 1244</div>
            <div class="apidocs-english">Nationality, 1244</div>
        address (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian">Адрес клиента, 1254</div>
            <div class="apidocs-english">Client address, 1254</div>
    """

    group: "NebularApiModelsLkServiceGroup"
    fio: Union[None, Unset, str] = UNSET
    gender: Union[Unset, int] = UNSET
    inn: Union[None, Unset, str] = UNSET
    birth_date: Union[None, Unset, datetime.datetime] = UNSET
    main_phone: Union[None, Unset, str] = UNSET
    additional_phone: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    passport: Union[None, Unset, str] = UNSET
    doc_type: Union[None, Unset, int] = UNSET
    nationality: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        fio: Union[None, Unset, str]
        if isinstance(self.fio, Unset):
            fio = UNSET
        else:
            fio = self.fio

        gender = self.gender

        inn: Union[None, Unset, str]
        if isinstance(self.inn, Unset):
            inn = UNSET
        else:
            inn = self.inn

        birth_date: Union[None, Unset, str]
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.datetime):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        main_phone: Union[None, Unset, str]
        if isinstance(self.main_phone, Unset):
            main_phone = UNSET
        else:
            main_phone = self.main_phone

        additional_phone: Union[None, Unset, str]
        if isinstance(self.additional_phone, Unset):
            additional_phone = UNSET
        else:
            additional_phone = self.additional_phone

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        passport: Union[None, Unset, str]
        if isinstance(self.passport, Unset):
            passport = UNSET
        else:
            passport = self.passport

        doc_type: Union[None, Unset, int]
        if isinstance(self.doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = self.doc_type

        nationality: Union[None, Unset, str]
        if isinstance(self.nationality, Unset):
            nationality = UNSET
        else:
            nationality = self.nationality

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "group": group,
            }
        )
        if fio is not UNSET:
            field_dict["fio"] = fio
        if gender is not UNSET:
            field_dict["gender"] = gender
        if inn is not UNSET:
            field_dict["inn"] = inn
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if main_phone is not UNSET:
            field_dict["mainPhone"] = main_phone
        if additional_phone is not UNSET:
            field_dict["additionalPhone"] = additional_phone
        if email is not UNSET:
            field_dict["email"] = email
        if comment is not UNSET:
            field_dict["comment"] = comment
        if passport is not UNSET:
            field_dict["passport"] = passport
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_group import NebularApiModelsLkServiceGroup

        d = dict(src_dict)
        group = NebularApiModelsLkServiceGroup.from_dict(d.pop("group"))

        def _parse_fio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fio = _parse_fio(d.pop("fio", UNSET))

        gender = d.pop("gender", UNSET)

        def _parse_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inn = _parse_inn(d.pop("inn", UNSET))

        def _parse_birth_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data)

                return birth_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        birth_date = _parse_birth_date(d.pop("birthDate", UNSET))

        def _parse_main_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        main_phone = _parse_main_phone(d.pop("mainPhone", UNSET))

        def _parse_additional_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_phone = _parse_additional_phone(d.pop("additionalPhone", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_passport(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        passport = _parse_passport(d.pop("passport", UNSET))

        def _parse_doc_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        doc_type = _parse_doc_type(d.pop("docType", UNSET))

        def _parse_nationality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nationality = _parse_nationality(d.pop("nationality", UNSET))

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        nebular_api_models_lk_service_client = cls(
            group=group,
            fio=fio,
            gender=gender,
            inn=inn,
            birth_date=birth_date,
            main_phone=main_phone,
            additional_phone=additional_phone,
            email=email,
            comment=comment,
            passport=passport,
            doc_type=doc_type,
            nationality=nationality,
            address=address,
        )

        return nebular_api_models_lk_service_client
