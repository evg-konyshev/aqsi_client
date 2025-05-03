from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_marking_type_enum import NebularApiEnumsMarkingTypeEnum
from ..models.nebular_api_enums_no_return_enum import NebularApiEnumsNoReturnEnum
from ..models.nebular_api_enums_payment_method_type_enum import NebularApiEnumsPaymentMethodTypeEnum
from ..models.nebular_api_enums_payment_subject_type_enum import NebularApiEnumsPaymentSubjectTypeEnum
from ..models.nebular_api_enums_unit_code_enum import NebularApiEnumsUnitCodeEnum
from ..models.nebular_api_enums_vat_rate_enum import NebularApiEnumsVATRateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
    from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg
    from ..models.nebular_api_models_lk_service_receipt_properties import NebularApiModelsLkServiceReceiptProperties
    from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo


T = TypeVar("T", bound="NebularApiModelsLkServiceGoodsExtendedGoodDtoV2")


@_attrs_define
class NebularApiModelsLkServiceGoodsExtendedGoodDtoV2:
    """
    Attributes:
        id (str): <div class="apidocs-russian">Уникальный идентификатор товара в рамках аккаунта</div>
            <div class="apidocs-english">Goods account-wide unique identifier</div>
        group_id (str): <div class="apidocs-russian">Идентификатор категории</div>
            <div class="apidocs-english">Category identifier</div>
        type_ (str): <div class="apidocs-russian">Тип товара (возможные значения: simple, ingredient, complex)</div>
            <div class="apidocs-english">Goods type (possible values: simple, ingredient, complex)</div> Default: 'simple'.
        tax (NebularApiEnumsVATRateEnum): Ставка НДС, 1199
        unit (str): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Единица измерения, 1197</div>
            <div class="apidocs-english tag-value">Unit of measurement, 1197</div>
        subject (NebularApiEnumsPaymentSubjectTypeEnum): Предмет расчета, 1212
        name (str): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Имя товара</div>
            <div class="apidocs-english tag-value">Goods name</div>
        payment_method_type (NebularApiEnumsPaymentMethodTypeEnum): Способ расчета, 1214
        production_cost (Union[None, Unset, float]): <div class="apidocs-russian">Себестоимость</div>
            <div class="apidocs-english">Cost price</div>
        margin_percent (Union[None, Unset, float]): <div class="apidocs-russian">Наценка</div>
            <div class="apidocs-english">Extra charge</div>
        is_weight (Union[Unset, int]): <div class="apidocs-russian">Весовой ли товар 0-Штучный 1-Весовой</div>
            <div class="apidocs-english">Item Type 0-Piece 1-Weight</div> Default: 0.
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
        is_orderable (Union[Unset, bool]): <div class="apidocs-russian">Возможность закупки товара у населения</div>
            <div class="apidocs-english">The ability to purchase goods from the population</div> Default: False.
        slot_info (Union['NebularApiModelsLkServiceSlotInfo', None, Unset]): <div class="apidocs-russian">Информация о
            слоте</div>
            <div class="apidocs-english">Slot info</div>
        sku (Union[None, Unset, str]): <div class="apidocs-russian">Артикул товара</div>
            <div class="apidocs-english">Goods vendor code</div>
        field_1_c_sku (Union[None, Unset, str]): <div class="apidocs-russian">SKU товара в 1С</div>
            <div class="apidocs-english">Goods 1C system SKU</div>
        price (Union[None, Unset, float]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Цена за единицу</div>
            <div class="apidocs-english tag-value">Unit price</div>
        barcodes (Union[None, Unset, list[str]]): <div class="apidocs-russian">Штрих-коды товаров (штрих-код должен
            состоять только из цифр, допустимая длина - от 4 до 22 цифр)</div>
            <div class="apidocs-english">Product barcodes (barcode must only contain 4-22 digits)</div>
        img (Union['NebularApiModelsLkServiceImg', None, Unset]): <div class="apidocs-russian">Изображение товара</div>
            <div class="apidocs-english">Goods image</div>
        last_purchase_price (Union[None, Unset, float]): <div class="apidocs-russian">Последняя цена закупки</div>
            <div class="apidocs-english">Last purchase price</div>
        accounting_method (Union[None, Unset, str]): <div class="apidocs-russian">Метод списания (возможные значения:
            children, self, self first, none)</div>
            <div class="apidocs-english">Withdraw method (possible values: children, self, self first, none)</div>
        cooking_time_minutes (Union[None, Unset, int]): <div class="apidocs-russian">Время приготовления, минуты</div>
            <div class="apidocs-english">Cooking time, minutes</div>
        cooking_time_seconds (Union[None, Unset, int]): <div class="apidocs-russian">Время приготовления, секунды</div>
            <div class="apidocs-english">Cooking time, seconds</div>
        cooking_receipt (Union[None, Unset, str]): <div class="apidocs-russian">Рецепт приготовления</div>
            <div class="apidocs-english">Recipe</div>
        non_tradable (Union[Unset, bool]): <div class="apidocs-russian">Не для продажи</div>
            <div class="apidocs-english">Non Tradable</div> Default: False.
        marking_type (Union[NebularApiEnumsMarkingTypeEnum, None, Unset]): <div class="apidocs-russian">Тип маркировки
            (при наличии)</div>
            <div class="apidocs-english">Marking Type (if any)</div>
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
        min_price (Union[None, Unset, float]): <div class="apidocs-russian">Минимальная цена</div>
            <div class="apidocs-english">Minimum price</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
        receipt_properties (Union['NebularApiModelsLkServiceReceiptProperties', None, Unset]): <div class="apidocs-
            russian">Параметры по умолчанию для позиции чека</div>
            <div class="apidocs-english">Default options for receipt item</div>
        max_discount_percent (Union[None, Unset, float]): <div class="apidocs-russian">Максимальный процент скидки</div>
            <div class="apidocs-english">Maximum discount percentage</div>
        nomenclature_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Код товара для ОФД, 1162 (Заполняется если требуется дополнительный
            реквизит "Код товара", Поле должно содержать ровно 13 цифр)</div>
            <div class="apidocs-english tag-value">Good's code for fiscal data operator, 1162 (Fill this field if additional
            props "Good's code" is needed, 13-digit field)</div>
        industry_attribute (Union['NebularApiModelsCommonApiIndustryAttribute', None, Unset]): <div class="apidocs-
            russian apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Отраслевой реквизит предмета расчёта, 1260</div>
            <div class="apidocs-english tag-value">Position industry attribute, 1260</div>
        no_return (Union[NebularApiEnumsNoReturnEnum, None, Unset]): <div class="apidocs-russian">Данный параметр
            позволяет полностью отключить возможность возврата позиции.</div>
            <div class="apidocs-english">This parameter allows completely disable position refund</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">0</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Выключен</div><div class="apidocs-english">Off</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Включен</div><div class="apidocs-english">On</div></div>
    """

    id: str
    group_id: str
    tax: NebularApiEnumsVATRateEnum
    unit: str
    subject: NebularApiEnumsPaymentSubjectTypeEnum
    name: str
    payment_method_type: NebularApiEnumsPaymentMethodTypeEnum
    type_: str = "simple"
    production_cost: Union[None, Unset, float] = UNSET
    margin_percent: Union[None, Unset, float] = UNSET
    is_weight: Union[Unset, int] = 0
    unit_code: Union[NebularApiEnumsUnitCodeEnum, None, Unset] = UNSET
    is_orderable: Union[Unset, bool] = False
    slot_info: Union["NebularApiModelsLkServiceSlotInfo", None, Unset] = UNSET
    sku: Union[None, Unset, str] = UNSET
    field_1_c_sku: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    barcodes: Union[None, Unset, list[str]] = UNSET
    img: Union["NebularApiModelsLkServiceImg", None, Unset] = UNSET
    last_purchase_price: Union[None, Unset, float] = UNSET
    accounting_method: Union[None, Unset, str] = UNSET
    cooking_time_minutes: Union[None, Unset, int] = UNSET
    cooking_time_seconds: Union[None, Unset, int] = UNSET
    cooking_receipt: Union[None, Unset, str] = UNSET
    non_tradable: Union[Unset, bool] = False
    marking_type: Union[NebularApiEnumsMarkingTypeEnum, None, Unset] = UNSET
    min_price: Union[None, Unset, float] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    receipt_properties: Union["NebularApiModelsLkServiceReceiptProperties", None, Unset] = UNSET
    max_discount_percent: Union[None, Unset, float] = UNSET
    nomenclature_code: Union[None, Unset, str] = UNSET
    industry_attribute: Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset] = UNSET
    no_return: Union[NebularApiEnumsNoReturnEnum, None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg
        from ..models.nebular_api_models_lk_service_receipt_properties import NebularApiModelsLkServiceReceiptProperties
        from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo

        id = self.id

        group_id = self.group_id

        type_ = self.type_

        tax = self.tax.value

        unit = self.unit

        subject = self.subject.value

        name = self.name

        payment_method_type = self.payment_method_type.value

        production_cost: Union[None, Unset, float]
        if isinstance(self.production_cost, Unset):
            production_cost = UNSET
        else:
            production_cost = self.production_cost

        margin_percent: Union[None, Unset, float]
        if isinstance(self.margin_percent, Unset):
            margin_percent = UNSET
        else:
            margin_percent = self.margin_percent

        is_weight = self.is_weight

        unit_code: Union[None, Unset, int]
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        elif isinstance(self.unit_code, NebularApiEnumsUnitCodeEnum):
            unit_code = self.unit_code.value
        else:
            unit_code = self.unit_code

        is_orderable = self.is_orderable

        slot_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.slot_info, Unset):
            slot_info = UNSET
        elif isinstance(self.slot_info, NebularApiModelsLkServiceSlotInfo):
            slot_info = self.slot_info.to_dict()
        else:
            slot_info = self.slot_info

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        field_1_c_sku: Union[None, Unset, str]
        if isinstance(self.field_1_c_sku, Unset):
            field_1_c_sku = UNSET
        else:
            field_1_c_sku = self.field_1_c_sku

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        barcodes: Union[None, Unset, list[str]]
        if isinstance(self.barcodes, Unset):
            barcodes = UNSET
        elif isinstance(self.barcodes, list):
            barcodes = self.barcodes

        else:
            barcodes = self.barcodes

        img: Union[None, Unset, dict[str, Any]]
        if isinstance(self.img, Unset):
            img = UNSET
        elif isinstance(self.img, NebularApiModelsLkServiceImg):
            img = self.img.to_dict()
        else:
            img = self.img

        last_purchase_price: Union[None, Unset, float]
        if isinstance(self.last_purchase_price, Unset):
            last_purchase_price = UNSET
        else:
            last_purchase_price = self.last_purchase_price

        accounting_method: Union[None, Unset, str]
        if isinstance(self.accounting_method, Unset):
            accounting_method = UNSET
        else:
            accounting_method = self.accounting_method

        cooking_time_minutes: Union[None, Unset, int]
        if isinstance(self.cooking_time_minutes, Unset):
            cooking_time_minutes = UNSET
        else:
            cooking_time_minutes = self.cooking_time_minutes

        cooking_time_seconds: Union[None, Unset, int]
        if isinstance(self.cooking_time_seconds, Unset):
            cooking_time_seconds = UNSET
        else:
            cooking_time_seconds = self.cooking_time_seconds

        cooking_receipt: Union[None, Unset, str]
        if isinstance(self.cooking_receipt, Unset):
            cooking_receipt = UNSET
        else:
            cooking_receipt = self.cooking_receipt

        non_tradable = self.non_tradable

        marking_type: Union[None, Unset, int]
        if isinstance(self.marking_type, Unset):
            marking_type = UNSET
        elif isinstance(self.marking_type, NebularApiEnumsMarkingTypeEnum):
            marking_type = self.marking_type.value
        else:
            marking_type = self.marking_type

        min_price: Union[None, Unset, float]
        if isinstance(self.min_price, Unset):
            min_price = UNSET
        else:
            min_price = self.min_price

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

        receipt_properties: Union[None, Unset, dict[str, Any]]
        if isinstance(self.receipt_properties, Unset):
            receipt_properties = UNSET
        elif isinstance(self.receipt_properties, NebularApiModelsLkServiceReceiptProperties):
            receipt_properties = self.receipt_properties.to_dict()
        else:
            receipt_properties = self.receipt_properties

        max_discount_percent: Union[None, Unset, float]
        if isinstance(self.max_discount_percent, Unset):
            max_discount_percent = UNSET
        else:
            max_discount_percent = self.max_discount_percent

        nomenclature_code: Union[None, Unset, str]
        if isinstance(self.nomenclature_code, Unset):
            nomenclature_code = UNSET
        else:
            nomenclature_code = self.nomenclature_code

        industry_attribute: Union[None, Unset, dict[str, Any]]
        if isinstance(self.industry_attribute, Unset):
            industry_attribute = UNSET
        elif isinstance(self.industry_attribute, NebularApiModelsCommonApiIndustryAttribute):
            industry_attribute = self.industry_attribute.to_dict()
        else:
            industry_attribute = self.industry_attribute

        no_return: Union[None, Unset, int]
        if isinstance(self.no_return, Unset):
            no_return = UNSET
        elif isinstance(self.no_return, NebularApiEnumsNoReturnEnum):
            no_return = self.no_return.value
        else:
            no_return = self.no_return

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "type": type_,
                "tax": tax,
                "unit": unit,
                "subject": subject,
                "name": name,
                "paymentMethodType": payment_method_type,
            }
        )
        if production_cost is not UNSET:
            field_dict["productionCost"] = production_cost
        if margin_percent is not UNSET:
            field_dict["marginPercent"] = margin_percent
        if is_weight is not UNSET:
            field_dict["isWeight"] = is_weight
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if is_orderable is not UNSET:
            field_dict["isOrderable"] = is_orderable
        if slot_info is not UNSET:
            field_dict["slotInfo"] = slot_info
        if sku is not UNSET:
            field_dict["sku"] = sku
        if field_1_c_sku is not UNSET:
            field_dict["1cSku"] = field_1_c_sku
        if price is not UNSET:
            field_dict["price"] = price
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if img is not UNSET:
            field_dict["img"] = img
        if last_purchase_price is not UNSET:
            field_dict["lastPurchasePrice"] = last_purchase_price
        if accounting_method is not UNSET:
            field_dict["accountingMethod"] = accounting_method
        if cooking_time_minutes is not UNSET:
            field_dict["cookingTimeMinutes"] = cooking_time_minutes
        if cooking_time_seconds is not UNSET:
            field_dict["cookingTimeSeconds"] = cooking_time_seconds
        if cooking_receipt is not UNSET:
            field_dict["cookingReceipt"] = cooking_receipt
        if non_tradable is not UNSET:
            field_dict["nonTradable"] = non_tradable
        if marking_type is not UNSET:
            field_dict["markingType"] = marking_type
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if receipt_properties is not UNSET:
            field_dict["receiptProperties"] = receipt_properties
        if max_discount_percent is not UNSET:
            field_dict["maxDiscountPercent"] = max_discount_percent
        if nomenclature_code is not UNSET:
            field_dict["nomenclatureCode"] = nomenclature_code
        if industry_attribute is not UNSET:
            field_dict["industryAttribute"] = industry_attribute
        if no_return is not UNSET:
            field_dict["noReturn"] = no_return

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_lk_service_img import NebularApiModelsLkServiceImg
        from ..models.nebular_api_models_lk_service_receipt_properties import NebularApiModelsLkServiceReceiptProperties
        from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo

        d = dict(src_dict)
        id = d.pop("id")

        group_id = d.pop("group_id")

        type_ = d.pop("type")

        tax = NebularApiEnumsVATRateEnum(d.pop("tax"))

        unit = d.pop("unit")

        subject = NebularApiEnumsPaymentSubjectTypeEnum(d.pop("subject"))

        name = d.pop("name")

        payment_method_type = NebularApiEnumsPaymentMethodTypeEnum(d.pop("paymentMethodType"))

        def _parse_production_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        production_cost = _parse_production_cost(d.pop("productionCost", UNSET))

        def _parse_margin_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        margin_percent = _parse_margin_percent(d.pop("marginPercent", UNSET))

        is_weight = d.pop("isWeight", UNSET)

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

        is_orderable = d.pop("isOrderable", UNSET)

        def _parse_slot_info(data: object) -> Union["NebularApiModelsLkServiceSlotInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slot_info_type_1 = NebularApiModelsLkServiceSlotInfo.from_dict(data)

                return slot_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceSlotInfo", None, Unset], data)

        slot_info = _parse_slot_info(d.pop("slotInfo", UNSET))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_field_1_c_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field_1_c_sku = _parse_field_1_c_sku(d.pop("1cSku", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_barcodes(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                barcodes_type_0 = cast(list[str], data)

                return barcodes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        barcodes = _parse_barcodes(d.pop("barcodes", UNSET))

        def _parse_img(data: object) -> Union["NebularApiModelsLkServiceImg", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                img_type_1 = NebularApiModelsLkServiceImg.from_dict(data)

                return img_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceImg", None, Unset], data)

        img = _parse_img(d.pop("img", UNSET))

        def _parse_last_purchase_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_purchase_price = _parse_last_purchase_price(d.pop("lastPurchasePrice", UNSET))

        def _parse_accounting_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accounting_method = _parse_accounting_method(d.pop("accountingMethod", UNSET))

        def _parse_cooking_time_minutes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cooking_time_minutes = _parse_cooking_time_minutes(d.pop("cookingTimeMinutes", UNSET))

        def _parse_cooking_time_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cooking_time_seconds = _parse_cooking_time_seconds(d.pop("cookingTimeSeconds", UNSET))

        def _parse_cooking_receipt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cooking_receipt = _parse_cooking_receipt(d.pop("cookingReceipt", UNSET))

        non_tradable = d.pop("nonTradable", UNSET)

        def _parse_marking_type(data: object) -> Union[NebularApiEnumsMarkingTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                marking_type_type_1 = NebularApiEnumsMarkingTypeEnum(data)

                return marking_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsMarkingTypeEnum, None, Unset], data)

        marking_type = _parse_marking_type(d.pop("markingType", UNSET))

        def _parse_min_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_price = _parse_min_price(d.pop("minPrice", UNSET))

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

        def _parse_receipt_properties(data: object) -> Union["NebularApiModelsLkServiceReceiptProperties", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receipt_properties_type_1 = NebularApiModelsLkServiceReceiptProperties.from_dict(data)

                return receipt_properties_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceReceiptProperties", None, Unset], data)

        receipt_properties = _parse_receipt_properties(d.pop("receiptProperties", UNSET))

        def _parse_max_discount_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_discount_percent = _parse_max_discount_percent(d.pop("maxDiscountPercent", UNSET))

        def _parse_nomenclature_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nomenclature_code = _parse_nomenclature_code(d.pop("nomenclatureCode", UNSET))

        def _parse_industry_attribute(data: object) -> Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industry_attribute_type_1 = NebularApiModelsCommonApiIndustryAttribute.from_dict(data)

                return industry_attribute_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset], data)

        industry_attribute = _parse_industry_attribute(d.pop("industryAttribute", UNSET))

        def _parse_no_return(data: object) -> Union[NebularApiEnumsNoReturnEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                no_return_type_1 = NebularApiEnumsNoReturnEnum(data)

                return no_return_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsNoReturnEnum, None, Unset], data)

        no_return = _parse_no_return(d.pop("noReturn", UNSET))

        nebular_api_models_lk_service_goods_extended_good_dto_v2 = cls(
            id=id,
            group_id=group_id,
            type_=type_,
            tax=tax,
            unit=unit,
            subject=subject,
            name=name,
            payment_method_type=payment_method_type,
            production_cost=production_cost,
            margin_percent=margin_percent,
            is_weight=is_weight,
            unit_code=unit_code,
            is_orderable=is_orderable,
            slot_info=slot_info,
            sku=sku,
            field_1_c_sku=field_1_c_sku,
            price=price,
            barcodes=barcodes,
            img=img,
            last_purchase_price=last_purchase_price,
            accounting_method=accounting_method,
            cooking_time_minutes=cooking_time_minutes,
            cooking_time_seconds=cooking_time_seconds,
            cooking_receipt=cooking_receipt,
            non_tradable=non_tradable,
            marking_type=marking_type,
            min_price=min_price,
            custom_properties=custom_properties,
            receipt_properties=receipt_properties,
            max_discount_percent=max_discount_percent,
            nomenclature_code=nomenclature_code,
            industry_attribute=industry_attribute,
            no_return=no_return,
        )

        return nebular_api_models_lk_service_goods_extended_good_dto_v2
