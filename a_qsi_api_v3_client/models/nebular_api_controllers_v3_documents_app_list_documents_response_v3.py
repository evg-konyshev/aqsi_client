from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.nebular_api_controllers_v3_documents_app_list_documents_row_v3 import (
        NebularApiControllersV3DocumentsAppListDocumentsRowV3,
    )


T = TypeVar("T", bound="NebularApiControllersV3DocumentsAppListDocumentsResponseV3")


@_attrs_define
class NebularApiControllersV3DocumentsAppListDocumentsResponseV3:
    """
    Attributes:
        rows (list['NebularApiControllersV3DocumentsAppListDocumentsRowV3']): <div class="apidocs-russian">Список
            записей</div>
            <div class="apidocs-english">Records list</div>
        pages (int): <div class="apidocs-russian">Количество страниц</div>
            <div class="apidocs-english">Pages count</div>
        count (int): <div class="apidocs-russian">Общее кол-во документов</div>
            <div class="apidocs-english">Total documents count</div>
    """

    rows: list["NebularApiControllersV3DocumentsAppListDocumentsRowV3"]
    pages: int
    count: int

    def to_dict(self) -> dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        pages = self.pages

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "rows": rows,
                "pages": pages,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_controllers_v3_documents_app_list_documents_row_v3 import (
            NebularApiControllersV3DocumentsAppListDocumentsRowV3,
        )

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = NebularApiControllersV3DocumentsAppListDocumentsRowV3.from_dict(rows_item_data)

            rows.append(rows_item)

        pages = d.pop("pages")

        count = d.pop("count")

        nebular_api_controllers_v3_documents_app_list_documents_response_v3 = cls(
            rows=rows,
            pages=pages,
            count=count,
        )

        return nebular_api_controllers_v3_documents_app_list_documents_response_v3
