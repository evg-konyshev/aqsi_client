from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_unit_code_enum import NebularApiEnumsUnitCodeEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar(
    "T",
    bound="NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E",
)


@_attrs_define
class NebularApiModelsLkServiceRow2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E:
    """Облегченная модель товара

    Attributes:
        id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор товара</div>
            <div class="apidocs-english">Goods identifier</div>
        group_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор категории</div>
            <div class="apidocs-english">Category identifier</div>
        name (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
            ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Имя товара</div>
            <div class="apidocs-english tag-value">Goods name</div>
        type_ (Union[None, Unset, str]): <div class="apidocs-russian">Тип товара (возможные значения: simple,
            ingredient, complex)</div>
            <div class="apidocs-english">Goods type (possible values: simple, ingredient, complex)</div>
        sku (Union[None, Unset, str]): <div class="apidocs-russian">Артикул товара</div>
            <div class="apidocs-english">Goods vendor code</div>
        unit (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Единица измерения, 1197</div>
            <div class="apidocs-english tag-value">Unit of measurement, 1197</div>
        unit_code (Union[NebularApiEnumsUnitCodeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Единица измерения, 2108</div>
            <div class="apidocs-english tag-value">Unit of measurement, 2108</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">0</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Штука или Единица</div><div class="apidocs-
            english">Unit</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">10</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Грамм</div><div class="apidocs-english">Gram</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">11</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Килограмм</div><div class="apidocs-english">Kilogram</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">12</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Тонна</div><div class="apidocs-english">Ton</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">20</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Сантиметр</div><div class="apidocs-english">Centimetre</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">21</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Дециметр</div><div class="apidocs-english">Decimeter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">22</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Метр</div><div class="apidocs-english">Metre</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">30</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Квадратный сантиметр</div><div class="apidocs-english">Square
            centimeter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">31</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Квадратный дециметр</div><div class="apidocs-english">Square
            decimeter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">32</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Квадратный метр</div><div class="apidocs-english">Square
            meter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">40</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Миллилитр</div><div class="apidocs-english">Milliliter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">41</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Литр</div><div class="apidocs-english">Litre</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">42</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Кубический метр</div><div class="apidocs-english">Cubic
            meter</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">50</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Киловатт час</div><div class="apidocs-english">Kilowatt
            hour</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">51</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Гигакаллория</div><div class="apidocs-
            english">Gigacallory</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">70</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Сутки (день)</div><div class="apidocs-english">Day</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">71</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Час</div><div class="apidocs-english">Hour</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">72</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Минута</div><div class="apidocs-english">Minute</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">73</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Секунда</div><div class="apidocs-english">Second</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">80</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Килобайт</div><div class="apidocs-english">Kilobytes</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">81</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Мегабайт</div><div class="apidocs-english">Megabytes</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">82</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Гигабайт</div><div class="apidocs-english">Gigabytes</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">83</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Терабайт</div><div class="apidocs-english">Terabyte</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">255</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Иное</div><div class="apidocs-english">Other</div></div>
        tax (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
            ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Ставка налога на товар</div>
            <div class="apidocs-english tag-value">Product tax rate</div>
        production_cost (Union[None, Unset, float]): <div class="apidocs-russian">Себестоимость</div>
            <div class="apidocs-english">Cost price</div>
        price (Union[None, Unset, float]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Цена за единицу</div>
            <div class="apidocs-english tag-value">Unit price</div>
        margin_percent (Union[None, Unset, float]): <div class="apidocs-russian">Наценка</div>
            <div class="apidocs-english">Extra charge</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
    """

    id: Union[None, Unset, str] = UNSET
    group_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    sku: Union[None, Unset, str] = UNSET
    unit: Union[None, Unset, str] = UNSET
    unit_code: Union[NebularApiEnumsUnitCodeEnum, None, Unset] = UNSET
    tax: Union[None, Unset, str] = UNSET
    production_cost: Union[None, Unset, float] = UNSET
    price: Union[None, Unset, float] = UNSET
    margin_percent: Union[None, Unset, float] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        group_id: Union[None, Unset, str]
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        unit: Union[None, Unset, str]
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        unit_code: Union[None, Unset, int]
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        elif isinstance(self.unit_code, NebularApiEnumsUnitCodeEnum):
            unit_code = self.unit_code.value
        else:
            unit_code = self.unit_code

        tax: Union[None, Unset, str]
        if isinstance(self.tax, Unset):
            tax = UNSET
        else:
            tax = self.tax

        production_cost: Union[None, Unset, float]
        if isinstance(self.production_cost, Unset):
            production_cost = UNSET
        else:
            production_cost = self.production_cost

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        margin_percent: Union[None, Unset, float]
        if isinstance(self.margin_percent, Unset):
            margin_percent = UNSET
        else:
            margin_percent = self.margin_percent

        custom_properties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_properties, Unset):
            custom_properties = UNSET
        elif isinstance(self.custom_properties, list):
            custom_properties = []
            for custom_properties_type_0_item_data in self.custom_properties:
                custom_properties_type_0_item = custom_properties_type_0_item_data.to_dict()
                custom_properties.append(custom_properties_type_0_item)

        else:
            custom_properties = self.custom_properties

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sku is not UNSET:
            field_dict["sku"] = sku
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if tax is not UNSET:
            field_dict["tax"] = tax
        if production_cost is not UNSET:
            field_dict["productionCost"] = production_cost
        if price is not UNSET:
            field_dict["price"] = price
        if margin_percent is not UNSET:
            field_dict["marginPercent"] = margin_percent
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_unit_code(data: object) -> Union[NebularApiEnumsUnitCodeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                unit_code_type_1 = NebularApiEnumsUnitCodeEnum(data)

                return unit_code_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsUnitCodeEnum, None, Unset], data)

        unit_code = _parse_unit_code(d.pop("unitCode", UNSET))

        def _parse_tax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax = _parse_tax(d.pop("tax", UNSET))

        def _parse_production_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        production_cost = _parse_production_cost(d.pop("productionCost", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_margin_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        margin_percent = _parse_margin_percent(d.pop("marginPercent", UNSET))

        def _parse_custom_properties(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_properties_type_0 = []
                _custom_properties_type_0 = data
                for custom_properties_type_0_item_data in _custom_properties_type_0:
                    custom_properties_type_0_item = NebularApiModelsLkServiceCustomProperty.from_dict(
                        custom_properties_type_0_item_data
                    )

                    custom_properties_type_0.append(custom_properties_type_0_item)

                return custom_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]], data)

        custom_properties = _parse_custom_properties(d.pop("customProperties", UNSET))

        nebular_api_models_lk_service_row_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e = cls(
            id=id,
            group_id=group_id,
            name=name,
            type_=type_,
            sku=sku,
            unit=unit,
            unit_code=unit_code,
            tax=tax,
            production_cost=production_cost,
            price=price,
            margin_percent=margin_percent,
            custom_properties=custom_properties,
        )

        return nebular_api_models_lk_service_row_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e
