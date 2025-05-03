from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiControllersV3DocumentsAppListDocumentsRowV3")


@_attrs_define
class NebularApiControllersV3DocumentsAppListDocumentsRowV3:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор</div>
            <div class="apidocs-english">Id</div>
        external_id (str): <div class="apidocs-russian">Внешний идентификатор</div>
            <div class="apidocs-english">External id</div>
        number (int): <div class="apidocs-russian">Номер документа</div>
            <div class="apidocs-english">Document number</div>
        date_time (str): <div class="apidocs-russian">Дата документа</div>
            <div class="apidocs-english">Document date</div>
        status (str): <div class="apidocs-russian">Статус документа. Допустимые значения: <b>"draft"</b>,
            <b>"complete"</b>.</div>
            <div class="apidocs-english">Document status. Allowed values: <b>"draft"</b>, <b>"complete"</b>.</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий</div>
            <div class="apidocs-english">Comment</div>
    """

    id: str
    external_id: str
    number: int
    date_time: str
    status: str
    comment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        number = self.number

        date_time = self.date_time

        status = self.status

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
                "number": number,
                "dateTime": date_time,
                "status": status,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("externalId")

        number = d.pop("number")

        date_time = d.pop("dateTime")

        status = d.pop("status")

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        nebular_api_controllers_v3_documents_app_list_documents_row_v3 = cls(
            id=id,
            external_id=external_id,
            number=number,
            date_time=date_time,
            status=status,
            comment=comment,
        )

        return nebular_api_controllers_v3_documents_app_list_documents_row_v3
