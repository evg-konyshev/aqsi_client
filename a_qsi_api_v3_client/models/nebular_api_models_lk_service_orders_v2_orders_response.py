from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_dtos_get_order_status_with_receipts_content import (
        NebularApiDtosGetOrderStatusWithReceiptsContent,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceOrdersV2OrdersResponse")


@_attrs_define
class NebularApiModelsLkServiceOrdersV2OrdersResponse:
    """
    Attributes:
        rows (Union[None, Unset, list['NebularApiDtosGetOrderStatusWithReceiptsContent']]): <div class="apidocs-
            russian">Список заказов</div>
            <div class="apidocs-english">Orders list</div>
        pages (Union[Unset, int]): <div class="apidocs-russian">Количество страниц по данному запросу</div>
            <div class="apidocs-english">Number of pages for this request</div>
        no_data (Union[Unset, bool]): <div class="apidocs-russian">Признак отстутствия данных (при заданных параметрах
            фильтрации)</div>
            <div class="apidocs-english">Sign of lack of data (with specified filtering parameters)</div>
    """

    rows: Union[None, Unset, list["NebularApiDtosGetOrderStatusWithReceiptsContent"]] = UNSET
    pages: Union[Unset, int] = UNSET
    no_data: Union[Unset, bool] = UNSET

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

        pages = self.pages

        no_data = self.no_data

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if pages is not UNSET:
            field_dict["pages"] = pages
        if no_data is not UNSET:
            field_dict["noData"] = no_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_dtos_get_order_status_with_receipts_content import (
            NebularApiDtosGetOrderStatusWithReceiptsContent,
        )

        d = dict(src_dict)

        def _parse_rows(data: object) -> Union[None, Unset, list["NebularApiDtosGetOrderStatusWithReceiptsContent"]]:
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
                    rows_type_0_item = NebularApiDtosGetOrderStatusWithReceiptsContent.from_dict(rows_type_0_item_data)

                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiDtosGetOrderStatusWithReceiptsContent"]], data)

        rows = _parse_rows(d.pop("rows", UNSET))

        pages = d.pop("pages", UNSET)

        no_data = d.pop("noData", UNSET)

        nebular_api_models_lk_service_orders_v2_orders_response = cls(
            rows=rows,
            pages=pages,
            no_data=no_data,
        )

        return nebular_api_models_lk_service_orders_v2_orders_response
