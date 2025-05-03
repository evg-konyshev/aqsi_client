from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_row_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e import (
        NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    )


T = TypeVar(
    "T",
    bound="NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E",
)


@_attrs_define
class NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E:
    """Информация о списке товаров с количеством страниц для данного запроса

    Example:
        {'rows': [{'id': 'GOOD_STRING_ID', 'group_id': 'GROUP_STRING_ID', 'name': 'Плов', 'type': 'complex', 'sku':
            None, 'unit': 'кг', 'unitCode': None, 'tax': '1', 'productionCost': None, 'price': 193, 'marginPercent': None,
            'customProperties': None}], 'pages': 1}

    Attributes:
        rows (Union[None, Unset, list['NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000Culturene
            utralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85
            D7Bea7798E']]): <div class="apidocs-russian">Список облегченных модели товаров</div>
            <div class="apidocs-english">List of light goods models</div>
        pages (Union[Unset, int]): <div class="apidocs-russian">Количество страниц по данному запросу</div>
            <div class="apidocs-english">Number of pages for this request</div>
    """

    rows: Union[
        None,
        Unset,
        list[
            "NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E"
        ],
    ] = UNSET
    pages: Union[Unset, int] = UNSET

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_row_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e import (
            NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
        )

        d = dict(src_dict)

        def _parse_rows(
            data: object,
        ) -> Union[
            None,
            Unset,
            list[
                "NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E"
            ],
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
                    rows_type_0_item = NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E.from_dict(
                        rows_type_0_item_data
                    )

                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list[
                        "NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E"
                    ],
                ],
                data,
            )

        rows = _parse_rows(d.pop("rows", UNSET))

        pages = d.pop("pages", UNSET)

        nebular_api_models_lk_service_goods_rows_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e = cls(
            rows=rows,
            pages=pages,
        )

        return nebular_api_models_lk_service_goods_rows_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e
