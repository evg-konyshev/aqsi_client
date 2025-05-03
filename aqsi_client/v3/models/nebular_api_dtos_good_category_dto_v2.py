from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_marking_type_enum import NebularApiEnumsMarkingTypeEnum
from ..models.nebular_api_enums_payment_method_type_enum import NebularApiEnumsPaymentMethodTypeEnum
from ..models.nebular_api_enums_payment_subject_type_enum import NebularApiEnumsPaymentSubjectTypeEnum
from ..models.nebular_api_enums_unit_code_enum import NebularApiEnumsUnitCodeEnum
from ..models.nebular_api_enums_vat_rate_enum import NebularApiEnumsVATRateEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar("T", bound="NebularApiDtosGoodCategoryDtoV2")


@_attrs_define
class NebularApiDtosGoodCategoryDtoV2:
    """Товарная категория

    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор категории</div>
            <div class="apidocs-english">Category identifier</div>
        name (str): <div class="apidocs-russian">Название категории</div>
            <div class="apidocs-english">Category name</div>
        default_subject (NebularApiEnumsPaymentSubjectTypeEnum): Предмет расчета, 1212
        default_tax (NebularApiEnumsVATRateEnum): Ставка НДС, 1199
        default_unit (str): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Единица измерения категории по умолчанию, 1197</div>
            <div class="apidocs-english tag-value">Default Category Unit, 1197</div>
        default_payment_method_type (NebularApiEnumsPaymentMethodTypeEnum): Способ расчета, 1214
        number (Union[Unset, int]): <div class="apidocs-russian">Номер по порядку</div>
            <div class="apidocs-english">Number in order</div>
        parent (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор родительской категории</div>
            <div class="apidocs-english">Parent Category identifier</div>
        default_unit_code (Union[NebularApiEnumsUnitCodeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Единица измерения категории по умолчанию, 2108</div>
            <div class="apidocs-english tag-value">Default Category Unit, 2108</div>
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
        default_marking_type (Union[NebularApiEnumsMarkingTypeEnum, None, Unset]): <div class="apidocs-russian">Тип
            маркировки (при наличии)</div>
            <div class="apidocs-english">Marking type (if any)</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Товары из натурального меха</div><div class="apidocs-
            english">Natural fur goods</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">2</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Лекарственные товары</div><div class="apidocs-
            english">Medicines</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">3</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Табачная продукция</div><div class="apidocs-
            english">Tobacco</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">4</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Обувные товары</div><div class="apidocs-english">Shoes</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">5</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Духи и туалетная вода</div><div class="apidocs-
            english">Perfume</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">6</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Шины и покрышки пневматические резиновые новые</div><div
            class="apidocs-english">Tires</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">7</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian"><s>Предметы одежды, включая рабочую одежду, изготовленные из
            натуральной или композиционной кожи.</s> Используйте 11, Товары легкой промышленности.</div><div class="apidocs-
            english"><s>Leather clothes.</s> Use 11, Light industry goods instead.</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">8</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian"><s>Блузки, блузы и блузоны трикотажные машинного или ручного
            вязания, женские или для девочек.</s> Используйте 11, Товары легкой промышленности.</div><div class="apidocs-
            english"><s>Blouses.</s> Use 11, Light industry goods instead.</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">9</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian"><s>Пальто, полупальто, накидки, плащи, куртки (включая лыжные),
            ветровки, штормовки и аналогичные изделия мужские или для мальчиков.</s> Используйте 11, Товары легкой
            промышленности.</div><div class="apidocs-english"><s>Man coats.</s> Use 11, Light industry goods
            instead.</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">10</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian"><s>Пальто, полупальто, накидки, плащи, куртки (включая лыжные),
            ветровки, штормовки и аналогичные изделия женские или для девочек.</s> Используйте 11, Товары легкой
            промышленности.</div><div class="apidocs-english"><s>Woman coats.</s> Use 11, Light industry goods
            instead.</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">11</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Товары легкой промышленности</div><div class="apidocs-
            english">Light industry goods</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">12</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Фотокамеры (кроме кинокамер), фотовспышки и лампы-вспышки</div><div
            class="apidocs-english">Cameras</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">13</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Молочная продукция</div><div class="apidocs-
            english">Dairy</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">14</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Велосипеды и велосипедные рамы</div><div class="apidocs-
            english">Bicycles</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">15</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Альтернативная табачная продукция</div><div class="apidocs-
            english">Alternative tobacco</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">16</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Биологически активные добавки к пище (БАД)</div><div
            class="apidocs-english">Dietary supplements</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">17</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Никотиносодержащая продукция</div><div class="apidocs-
            english">Nicotine-containing products</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">18</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Пиво, напитки, изготовленные на основе пива, и слабоалкогольные
            напитки с маркировкой ЧЗ, подлежащие списанию в УТМ ЕГАИС</div><div class="apidocs-english">Beer</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">19</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Медицинские изделия</div><div class="apidocs-english">Medical
            goods</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">20</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Антисептики и дезинфицирующие средства</div><div class="apidocs-
            english">Antiseptics</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">21</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Упакованная вода</div><div class="apidocs-
            english">BottledWater</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">22</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Алкогольная продукция ЕГАИСа</div><div class="apidocs-
            english">AlcoholEGAIS</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">23</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Немаркированные слабоалкогольные напитки, подлежащие списанию в УТМ
            ЕГАИС</div><div class="apidocs-english">Unmarked Low Alcohol</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">24</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Безалкогольное пиво</div><div class="apidocs-english">NON ALCOHOLIC
            BEER</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">25</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Соковая продукция и безалкогольные напитки</div><div
            class="apidocs-english">SOFT DRINKS</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">26</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Корма для животных</div><div class="apidocs-english">Pet
            food</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">27</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Морепродукты</div><div class="apidocs-english">Sea food</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">28</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Ветеринарные препараты</div><div class="apidocs-english">Vet
            pharma</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">29</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Консервированная продукция</div><div class="apidocs-
            english">Conserve</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">30</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Растительные масла</div><div class="apidocs-english">Vegetable
            oil</div></div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
    """

    id: str
    name: str
    default_subject: NebularApiEnumsPaymentSubjectTypeEnum
    default_tax: NebularApiEnumsVATRateEnum
    default_unit: str
    default_payment_method_type: NebularApiEnumsPaymentMethodTypeEnum
    number: Union[Unset, int] = UNSET
    parent: Union[None, Unset, str] = UNSET
    default_unit_code: Union[NebularApiEnumsUnitCodeEnum, None, Unset] = UNSET
    default_marking_type: Union[NebularApiEnumsMarkingTypeEnum, None, Unset] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        default_subject = self.default_subject.value

        default_tax = self.default_tax.value

        default_unit = self.default_unit

        default_payment_method_type = self.default_payment_method_type.value

        number = self.number

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        default_unit_code: Union[None, Unset, int]
        if isinstance(self.default_unit_code, Unset):
            default_unit_code = UNSET
        elif isinstance(self.default_unit_code, NebularApiEnumsUnitCodeEnum):
            default_unit_code = self.default_unit_code.value
        else:
            default_unit_code = self.default_unit_code

        default_marking_type: Union[None, Unset, int]
        if isinstance(self.default_marking_type, Unset):
            default_marking_type = UNSET
        elif isinstance(self.default_marking_type, NebularApiEnumsMarkingTypeEnum):
            default_marking_type = self.default_marking_type.value
        else:
            default_marking_type = self.default_marking_type

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
        field_dict.update(
            {
                "id": id,
                "name": name,
                "defaultSubject": default_subject,
                "defaultTax": default_tax,
                "defaultUnit": default_unit,
                "defaultPaymentMethodType": default_payment_method_type,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if parent is not UNSET:
            field_dict["parent"] = parent
        if default_unit_code is not UNSET:
            field_dict["defaultUnitCode"] = default_unit_code
        if default_marking_type is not UNSET:
            field_dict["defaultMarkingType"] = default_marking_type
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        default_subject = NebularApiEnumsPaymentSubjectTypeEnum(d.pop("defaultSubject"))

        default_tax = NebularApiEnumsVATRateEnum(d.pop("defaultTax"))

        default_unit = d.pop("defaultUnit")

        default_payment_method_type = NebularApiEnumsPaymentMethodTypeEnum(d.pop("defaultPaymentMethodType"))

        number = d.pop("number", UNSET)

        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_default_unit_code(data: object) -> Union[NebularApiEnumsUnitCodeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                default_unit_code_type_1 = NebularApiEnumsUnitCodeEnum(data)

                return default_unit_code_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsUnitCodeEnum, None, Unset], data)

        default_unit_code = _parse_default_unit_code(d.pop("defaultUnitCode", UNSET))

        def _parse_default_marking_type(data: object) -> Union[NebularApiEnumsMarkingTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                default_marking_type_type_1 = NebularApiEnumsMarkingTypeEnum(data)

                return default_marking_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsMarkingTypeEnum, None, Unset], data)

        default_marking_type = _parse_default_marking_type(d.pop("defaultMarkingType", UNSET))

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

        nebular_api_dtos_good_category_dto_v2 = cls(
            id=id,
            name=name,
            default_subject=default_subject,
            default_tax=default_tax,
            default_unit=default_unit,
            default_payment_method_type=default_payment_method_type,
            number=number,
            parent=parent,
            default_unit_code=default_unit_code,
            default_marking_type=default_marking_type,
            custom_properties=custom_properties,
        )

        return nebular_api_dtos_good_category_dto_v2
