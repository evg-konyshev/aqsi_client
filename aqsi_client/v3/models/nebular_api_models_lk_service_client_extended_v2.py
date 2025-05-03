import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_loyalty_card import NebularApiModelsLkServiceLoyaltyCard


T = TypeVar("T", bound="NebularApiModelsLkServiceClientExtendedV2")


@_attrs_define
class NebularApiModelsLkServiceClientExtendedV2:
    """
    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор клиента</div>
            <div class="apidocs-english">Client identifier</div>
        group_id (Union[Unset, UUID]): <div class="apidocs-russian">Идентификатор группы</div>
            <div class="apidocs-english">Group identifier</div>
        created_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Время создания</div>
            <div class="apidocs-english">Creation time</div>
        updated_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Время последнего обновления</div>
            <div class="apidocs-english">Last update time</div>
        deleted_at (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Время удаления</div>
            <div class="apidocs-english">Removal time</div>
        account_id (Union[Unset, int]): <div class="apidocs-russian">Идентификатор аккаунта</div>
            <div class="apidocs-english">Account identifier</div>
        loyalty_card (Union['NebularApiModelsLkServiceLoyaltyCard', None, Unset]): <div class="apidocs-russian">Карта
            лояльности</div>
            <div class="apidocs-english">Loyalty card</div>
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

    id: Union[None, Unset, str] = UNSET
    group_id: Union[Unset, UUID] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    account_id: Union[Unset, int] = UNSET
    loyalty_card: Union["NebularApiModelsLkServiceLoyaltyCard", None, Unset] = UNSET
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
        from ..models.nebular_api_models_lk_service_loyalty_card import NebularApiModelsLkServiceLoyaltyCard

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        group_id: Union[Unset, str] = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        account_id = self.account_id

        loyalty_card: Union[None, Unset, dict[str, Any]]
        if isinstance(self.loyalty_card, Unset):
            loyalty_card = UNSET
        elif isinstance(self.loyalty_card, NebularApiModelsLkServiceLoyaltyCard):
            loyalty_card = self.loyalty_card.to_dict()
        else:
            loyalty_card = self.loyalty_card

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if loyalty_card is not UNSET:
            field_dict["loyaltyCard"] = loyalty_card
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
        from ..models.nebular_api_models_lk_service_loyalty_card import NebularApiModelsLkServiceLoyaltyCard

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        _group_id = d.pop("groupId", UNSET)
        group_id: Union[Unset, UUID]
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        account_id = d.pop("accountId", UNSET)

        def _parse_loyalty_card(data: object) -> Union["NebularApiModelsLkServiceLoyaltyCard", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loyalty_card_type_1 = NebularApiModelsLkServiceLoyaltyCard.from_dict(data)

                return loyalty_card_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceLoyaltyCard", None, Unset], data)

        loyalty_card = _parse_loyalty_card(d.pop("loyaltyCard", UNSET))

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

        nebular_api_models_lk_service_client_extended_v2 = cls(
            id=id,
            group_id=group_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            account_id=account_id,
            loyalty_card=loyalty_card,
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

        return nebular_api_models_lk_service_client_extended_v2
