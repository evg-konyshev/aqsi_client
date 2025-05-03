from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_controllers_v3_documents_management_get_management_document_positions_response_row_v3 import (
        NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3,
    )


T = TypeVar("T", bound="NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseV3")


@_attrs_define
class NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseV3:
    """
    Attributes:
        rows (Union[None, Unset,
            list['NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3']]):
    """

    rows: Union[
        None, Unset, list["NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3"]
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        rows: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)

        else:
            rows = self.rows

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_controllers_v3_documents_management_get_management_document_positions_response_row_v3 import (
            NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3,
        )

        d = dict(src_dict)

        def _parse_rows(
            data: object,
        ) -> Union[
            None, Unset, list["NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3"]
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in _rows_type_0:
                    rows_type_0_item = (
                        NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3.from_dict(
                            rows_type_0_item_data
                        )
                    )

                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list["NebularApiControllersV3DocumentsManagementGetManagementDocumentPositionsResponseRowV3"],
                ],
                data,
            )

        rows = _parse_rows(d.pop("rows", UNSET))

        nebular_api_controllers_v3_documents_management_get_management_document_positions_response_v3 = cls(
            rows=rows,
        )

        return nebular_api_controllers_v3_documents_management_get_management_document_positions_response_v3
