from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_v3_devices_v3_list_devices_row_v3 import (
        NebularApiModelsLkServiceV3DevicesV3ListDevicesRowV3,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3")


@_attrs_define
class NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3:
    """
    Attributes:
        rows (list['NebularApiModelsLkServiceV3DevicesV3ListDevicesRowV3']): <div class="apidocs-russian">Список
            записей</div>
            <div class="apidocs-english">Devices list</div>
        pages (int): <div class="apidocs-russian">Количество страниц</div>
            <div class="apidocs-english">Pages count</div>
        count (int): <div class="apidocs-russian">Общее кол-во записей</div>
            <div class="apidocs-english">Total devices count</div>
    """

    rows: list["NebularApiModelsLkServiceV3DevicesV3ListDevicesRowV3"]
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
        from ..models.nebular_api_models_lk_service_v3_devices_v3_list_devices_row_v3 import (
            NebularApiModelsLkServiceV3DevicesV3ListDevicesRowV3,
        )

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = NebularApiModelsLkServiceV3DevicesV3ListDevicesRowV3.from_dict(rows_item_data)

            rows.append(rows_item)

        pages = d.pop("pages")

        count = d.pop("count")

        nebular_api_models_lk_service_v3_devices_v3_list_devices_response_v3 = cls(
            rows=rows,
            pages=pages,
            count=count,
        )

        return nebular_api_models_lk_service_v3_devices_v3_list_devices_response_v3
