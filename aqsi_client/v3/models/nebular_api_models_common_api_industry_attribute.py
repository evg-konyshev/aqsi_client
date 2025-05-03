from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiIndustryAttribute")


@_attrs_define
class NebularApiModelsCommonApiIndustryAttribute:
    """
    Attributes:
        foiv_id (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Идентификатор ФОИВ, 1262. Должно быть одним из: 001, 002, 003, 004, 005,
            006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027,
            028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049,
            050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071,
            072.</div>
            <div class="apidocs-english tag-value">FOIV id, 1262. Should be one of: 001, 002, 003, 004, 005, 006, 007, 008,
            009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030,
            031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052,
            053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071, 072.</div>
        cause_document_date (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Дата документа основания (Формат дд.мм.гг), 1263</div>
            <div class="apidocs-english tag-value">Cause document date (DD.MM.YY), 1263</div>
        cause_document_number (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Номер документа основания, 1264</div>
            <div class="apidocs-english tag-value">Cause document number, 1264</div>
        value (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Значение отраслевого реквизита, 1265</div>
            <div class="apidocs-english tag-value">Industry attribute value, 1265</div>
    """

    foiv_id: Union[None, Unset, str] = UNSET
    cause_document_date: Union[None, Unset, str] = UNSET
    cause_document_number: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        foiv_id: Union[None, Unset, str]
        if isinstance(self.foiv_id, Unset):
            foiv_id = UNSET
        else:
            foiv_id = self.foiv_id

        cause_document_date: Union[None, Unset, str]
        if isinstance(self.cause_document_date, Unset):
            cause_document_date = UNSET
        else:
            cause_document_date = self.cause_document_date

        cause_document_number: Union[None, Unset, str]
        if isinstance(self.cause_document_number, Unset):
            cause_document_number = UNSET
        else:
            cause_document_number = self.cause_document_number

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if foiv_id is not UNSET:
            field_dict["foivId"] = foiv_id
        if cause_document_date is not UNSET:
            field_dict["causeDocumentDate"] = cause_document_date
        if cause_document_number is not UNSET:
            field_dict["causeDocumentNumber"] = cause_document_number
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_foiv_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foiv_id = _parse_foiv_id(d.pop("foivId", UNSET))

        def _parse_cause_document_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cause_document_date = _parse_cause_document_date(d.pop("causeDocumentDate", UNSET))

        def _parse_cause_document_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cause_document_number = _parse_cause_document_number(d.pop("causeDocumentNumber", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        nebular_api_models_common_api_industry_attribute = cls(
            foiv_id=foiv_id,
            cause_document_date=cause_document_date,
            cause_document_number=cause_document_number,
            value=value,
        )

        return nebular_api_models_common_api_industry_attribute
