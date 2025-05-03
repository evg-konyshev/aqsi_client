import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.nebular_api_enums_adding_type_enum import NebularApiEnumsAddingTypeEnum
from ..models.nebular_api_enums_agent_type_enum import NebularApiEnumsAgentTypeEnum
from ..models.nebular_api_enums_marking_type_enum import NebularApiEnumsMarkingTypeEnum
from ..models.nebular_api_enums_no_return_enum import NebularApiEnumsNoReturnEnum
from ..models.nebular_api_enums_payment_method_type_enum import NebularApiEnumsPaymentMethodTypeEnum
from ..models.nebular_api_enums_payment_subject_type_enum import NebularApiEnumsPaymentSubjectTypeEnum
from ..models.nebular_api_enums_unit_code_enum import NebularApiEnumsUnitCodeEnum
from ..models.nebular_api_enums_vat_rate_enum import NebularApiEnumsVATRateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
    from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
    from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar("T", bound="NebularApiModelsCommonApiOrderDtoExtendedPosition")


@_attrs_define
class NebularApiModelsCommonApiOrderDtoExtendedPosition:
    """
    Attributes:
        quantity (float): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Количество предмета расчета, 1023</div>
            <div class="apidocs-english tag-value">Quantity, 1023</div>
        price (float): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Цена за единицу предмета расчета с учетом скидок и наценок, 1079</div>
            <div class="apidocs-english tag-value">Price per unit of calculation subject to discounts and margins,
            1079</div>
        tax (NebularApiEnumsVATRateEnum): Ставка НДС, 1199
        payment_method_type (NebularApiEnumsPaymentMethodTypeEnum): Способ расчета, 1214
        payment_subject_type (NebularApiEnumsPaymentSubjectTypeEnum): Предмет расчета, 1212
        sold_amount (Union[Unset, float]): <div class="apidocs-russian">Количество проданных единиц товара</div>
            <div class="apidocs-english">Number of units sold</div> Default: 0.0.
        sku (Union[None, Unset, str]): <div class="apidocs-russian">Код товара</div>
            <div class="apidocs-english">Product code</div>
        id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор товара</div>
            <div class="apidocs-english">Product identifier</div>
        discount_money (Union[Unset, float]): <div class="apidocs-russian">Скидка на общую сумму позиции (price * count)
            в валюте заказа. Диапазон значений от 0 до  `price * count`</div>
            <div class="apidocs-english">Discount on the total position amount (price * count) in the order currency. The
            range of values is from 0 to `price * count`</div> Default: 0.0.
        position_id (Union[Unset, UUID]): <div class="apidocs-russian">Идентификатор этой позиции в этом чеке</div>
            <div class="apidocs-english">ID of this position in the receipt</div>
        marking_type (Union[NebularApiEnumsMarkingTypeEnum, None, Unset]): <div class="apidocs-russian">Тип
            маркировки</div>
            <div class="apidocs-english">Marking type</div>
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
        nomenclature_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Код товарной номенклатуры, Код товара для ОФД, закодированный в base64 ,
            1162</div>
            <div class="apidocs-english tag-value">Nomenclature code and Good's code for fiscal data operator in base64
            encoding, 1162</div>
        item_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Код Маркированного товара в явном виде (GS-символ спецкод используется
            для разделения групп информации), 2000</div>
            <div class="apidocs-english tag-value">Item code as scanned from barcode with GS symbols, 2000</div>
        barcodes (Union[None, Unset, list[str]]): <div class="apidocs-russian">Список штрих-кодов позиции отложенного
            заказа</div>
            <div class="apidocs-english">List of barcodes of a pending order item</div>
        adding_type (Union[Unset, NebularApiEnumsAddingTypeEnum]):
        added_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Дата и время добавления позиции в чек
            или её последнего изменения</div>
            <div class="apidocs-english">Date and time the item was added to the receipt or its last update</div>
        editable (Union[Unset, bool]): <div class="apidocs-russian">Возможность редактирования позиции на кассе
            (значение по умолчанию true)</div>
            <div class="apidocs-english">Possibility to edit the position at the checkout (default value is true)</div>
        text (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
            ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Наименование предмета расчета, 1030</div>
            <div class="apidocs-english tag-value">Name of unity, 1030</div>
        agent_info (Union['NebularApiModelsIntegrationsAgentInfo', None, Unset]): <div class="apidocs-russian apidocs-
            ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Данные агента, 1223</div>
            <div class="apidocs-english tag-value">Agent info , 1223</div>
        unit_of_measurement (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Единица измерения предмета расчета, 1197</div>
            <div class="apidocs-english tag-value">Position unit of measurement, 1197</div>
        unit_code (Union[NebularApiEnumsUnitCodeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Мера количества предмета расчета, 2108</div>
            <div class="apidocs-english tag-value">Position unit of measurement, 2108</div>
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
        additional_attribute (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Дополнительный реквизит предмета расчета, 1191</div>
            <div class="apidocs-english tag-value">Additional attribute, 1191</div>
        manufacturer_country_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Код страны происхождения товара, 1230</div>
            <div class="apidocs-english tag-value">Manufacturer country code, 1230</div>
        customs_declaration_number (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Номер таможенной декларации, 1231</div>
            <div class="apidocs-english tag-value">Customs declaration number, 1231</div>
        supplier_inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">ИНН поставщика, 1226</div>
            <div class="apidocs-english tag-value">TIN of the supplier, 1226</div>
        supplier_info (Union['NebularApiModelsIntegrationsSupplierInfo', None, Unset]): <div class="apidocs-russian
            apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Данные поставщика, 1224</div>
            <div class="apidocs-english tag-value">Supplier info, 1224</div>
        excise (Union[None, Unset, float]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Акциз, 1229</div>
            <div class="apidocs-english tag-value">Excise, 1229</div>
        agent_type (Union[NebularApiEnumsAgentTypeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Признак агента по предмету расчета, 1222</div>
            <div class="apidocs-english tag-value">Agent type, 1222</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 0 (1)</div><div style="margin:
            0 0.25em;">-</div><div class="apidocs-russian">Банковский платежный агент</div><div class="apidocs-
            english">Payment bank agent</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 1 (2)</div><div style="margin:
            0 0.25em;">-</div><div class="apidocs-russian">Банковский платежный субагент</div><div class="apidocs-
            english">Payment bank sub agent</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 2 (4)</div><div style="margin:
            0 0.25em;">-</div><div class="apidocs-russian">Платежный агент</div><div class="apidocs-english">Paying
            agent</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 3 (8)</div><div style="margin:
            0 0.25em;">-</div><div class="apidocs-russian">Платежный субагент</div><div class="apidocs-english">Paying sub
            agent</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 4 (16)</div><div
            style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Поверенный</div><div class="apidocs-
            english">Attorney</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 5 (32)</div><div
            style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Комиссионер</div><div class="apidocs-
            english">Comissioner</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 6 (64)</div><div
            style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Иной агент</div><div class="apidocs-english">Other
            agetn</div></div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
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
        discount_percent (Union[Unset, float]): <div class="apidocs-russian">Скидка на позиции, проценты</div>
            <div class="apidocs-english">Discount on positions, percent</div>
        max_discount_percent (Union[Unset, float]): <div class="apidocs-russian">Максимальный процент скидки</div>
            <div class="apidocs-english">Maximum discount percentage</div>
        min_price (Union[Unset, float]): <div class="apidocs-russian">Минимальная цена, за которую может быть продан
            товар из этой позиции</div>
            <div class="apidocs-english">The minimum price for which a product from this position can be sold</div>
        is_weight (Union[Unset, int]): <div class="apidocs-russian">Весовой ли товар 0-Штучный 1-Весовой</div>
            <div class="apidocs-english">Item Type 0-Piece 1-Weight</div> Default: 0.
    """

    quantity: float
    price: float
    tax: NebularApiEnumsVATRateEnum
    payment_method_type: NebularApiEnumsPaymentMethodTypeEnum
    payment_subject_type: NebularApiEnumsPaymentSubjectTypeEnum
    sold_amount: Union[Unset, float] = 0.0
    sku: Union[None, Unset, str] = UNSET
    id: Union[None, UUID, Unset] = UNSET
    discount_money: Union[Unset, float] = 0.0
    position_id: Union[Unset, UUID] = UNSET
    marking_type: Union[NebularApiEnumsMarkingTypeEnum, None, Unset] = UNSET
    nomenclature_code: Union[None, Unset, str] = UNSET
    item_code: Union[None, Unset, str] = UNSET
    barcodes: Union[None, Unset, list[str]] = UNSET
    adding_type: Union[Unset, NebularApiEnumsAddingTypeEnum] = UNSET
    added_at: Union[Unset, datetime.datetime] = UNSET
    editable: Union[Unset, bool] = UNSET
    text: Union[None, Unset, str] = UNSET
    agent_info: Union["NebularApiModelsIntegrationsAgentInfo", None, Unset] = UNSET
    unit_of_measurement: Union[None, Unset, str] = UNSET
    unit_code: Union[NebularApiEnumsUnitCodeEnum, None, Unset] = UNSET
    additional_attribute: Union[None, Unset, str] = UNSET
    manufacturer_country_code: Union[None, Unset, str] = UNSET
    customs_declaration_number: Union[None, Unset, str] = UNSET
    supplier_inn: Union[None, Unset, str] = UNSET
    supplier_info: Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset] = UNSET
    excise: Union[None, Unset, float] = UNSET
    agent_type: Union[NebularApiEnumsAgentTypeEnum, None, Unset] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    industry_attribute: Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset] = UNSET
    no_return: Union[NebularApiEnumsNoReturnEnum, None, Unset] = UNSET
    discount_percent: Union[Unset, float] = UNSET
    max_discount_percent: Union[Unset, float] = UNSET
    min_price: Union[Unset, float] = UNSET
    is_weight: Union[Unset, int] = 0

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo

        quantity = self.quantity

        price = self.price

        tax = self.tax.value

        payment_method_type = self.payment_method_type.value

        payment_subject_type = self.payment_subject_type.value

        sold_amount = self.sold_amount

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        discount_money = self.discount_money

        position_id: Union[Unset, str] = UNSET
        if not isinstance(self.position_id, Unset):
            position_id = str(self.position_id)

        marking_type: Union[None, Unset, int]
        if isinstance(self.marking_type, Unset):
            marking_type = UNSET
        elif isinstance(self.marking_type, NebularApiEnumsMarkingTypeEnum):
            marking_type = self.marking_type.value
        else:
            marking_type = self.marking_type

        nomenclature_code: Union[None, Unset, str]
        if isinstance(self.nomenclature_code, Unset):
            nomenclature_code = UNSET
        else:
            nomenclature_code = self.nomenclature_code

        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        barcodes: Union[None, Unset, list[str]]
        if isinstance(self.barcodes, Unset):
            barcodes = UNSET
        elif isinstance(self.barcodes, list):
            barcodes = self.barcodes

        else:
            barcodes = self.barcodes

        adding_type: Union[Unset, int] = UNSET
        if not isinstance(self.adding_type, Unset):
            adding_type = self.adding_type.value

        added_at: Union[Unset, str] = UNSET
        if not isinstance(self.added_at, Unset):
            added_at = self.added_at.isoformat()

        editable = self.editable

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        agent_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.agent_info, Unset):
            agent_info = UNSET
        elif isinstance(self.agent_info, NebularApiModelsIntegrationsAgentInfo):
            agent_info = self.agent_info.to_dict()
        else:
            agent_info = self.agent_info

        unit_of_measurement: Union[None, Unset, str]
        if isinstance(self.unit_of_measurement, Unset):
            unit_of_measurement = UNSET
        else:
            unit_of_measurement = self.unit_of_measurement

        unit_code: Union[None, Unset, int]
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        elif isinstance(self.unit_code, NebularApiEnumsUnitCodeEnum):
            unit_code = self.unit_code.value
        else:
            unit_code = self.unit_code

        additional_attribute: Union[None, Unset, str]
        if isinstance(self.additional_attribute, Unset):
            additional_attribute = UNSET
        else:
            additional_attribute = self.additional_attribute

        manufacturer_country_code: Union[None, Unset, str]
        if isinstance(self.manufacturer_country_code, Unset):
            manufacturer_country_code = UNSET
        else:
            manufacturer_country_code = self.manufacturer_country_code

        customs_declaration_number: Union[None, Unset, str]
        if isinstance(self.customs_declaration_number, Unset):
            customs_declaration_number = UNSET
        else:
            customs_declaration_number = self.customs_declaration_number

        supplier_inn: Union[None, Unset, str]
        if isinstance(self.supplier_inn, Unset):
            supplier_inn = UNSET
        else:
            supplier_inn = self.supplier_inn

        supplier_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.supplier_info, Unset):
            supplier_info = UNSET
        elif isinstance(self.supplier_info, NebularApiModelsIntegrationsSupplierInfo):
            supplier_info = self.supplier_info.to_dict()
        else:
            supplier_info = self.supplier_info

        excise: Union[None, Unset, float]
        if isinstance(self.excise, Unset):
            excise = UNSET
        else:
            excise = self.excise

        agent_type: Union[None, Unset, int]
        if isinstance(self.agent_type, Unset):
            agent_type = UNSET
        elif isinstance(self.agent_type, NebularApiEnumsAgentTypeEnum):
            agent_type = self.agent_type.value
        else:
            agent_type = self.agent_type

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

        discount_percent = self.discount_percent

        max_discount_percent = self.max_discount_percent

        min_price = self.min_price

        is_weight = self.is_weight

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "quantity": quantity,
                "price": price,
                "tax": tax,
                "paymentMethodType": payment_method_type,
                "paymentSubjectType": payment_subject_type,
            }
        )
        if sold_amount is not UNSET:
            field_dict["soldAmount"] = sold_amount
        if sku is not UNSET:
            field_dict["sku"] = sku
        if id is not UNSET:
            field_dict["id"] = id
        if discount_money is not UNSET:
            field_dict["discountMoney"] = discount_money
        if position_id is not UNSET:
            field_dict["positionId"] = position_id
        if marking_type is not UNSET:
            field_dict["markingType"] = marking_type
        if nomenclature_code is not UNSET:
            field_dict["nomenclatureCode"] = nomenclature_code
        if item_code is not UNSET:
            field_dict["itemCode"] = item_code
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if adding_type is not UNSET:
            field_dict["addingType"] = adding_type
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at
        if editable is not UNSET:
            field_dict["editable"] = editable
        if text is not UNSET:
            field_dict["text"] = text
        if agent_info is not UNSET:
            field_dict["agentInfo"] = agent_info
        if unit_of_measurement is not UNSET:
            field_dict["unitOfMeasurement"] = unit_of_measurement
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if additional_attribute is not UNSET:
            field_dict["additionalAttribute"] = additional_attribute
        if manufacturer_country_code is not UNSET:
            field_dict["manufacturerCountryCode"] = manufacturer_country_code
        if customs_declaration_number is not UNSET:
            field_dict["customsDeclarationNumber"] = customs_declaration_number
        if supplier_inn is not UNSET:
            field_dict["supplierINN"] = supplier_inn
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if excise is not UNSET:
            field_dict["excise"] = excise
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if industry_attribute is not UNSET:
            field_dict["industryAttribute"] = industry_attribute
        if no_return is not UNSET:
            field_dict["noReturn"] = no_return
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if max_discount_percent is not UNSET:
            field_dict["maxDiscountPercent"] = max_discount_percent
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if is_weight is not UNSET:
            field_dict["isWeight"] = is_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)
        quantity = d.pop("quantity")

        price = d.pop("price")

        tax = NebularApiEnumsVATRateEnum(d.pop("tax"))

        payment_method_type = NebularApiEnumsPaymentMethodTypeEnum(d.pop("paymentMethodType"))

        payment_subject_type = NebularApiEnumsPaymentSubjectTypeEnum(d.pop("paymentSubjectType"))

        sold_amount = d.pop("soldAmount", UNSET)

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

        discount_money = d.pop("discountMoney", UNSET)

        _position_id = d.pop("positionId", UNSET)
        position_id: Union[Unset, UUID]
        if isinstance(_position_id, Unset):
            position_id = UNSET
        else:
            position_id = UUID(_position_id)

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

        def _parse_nomenclature_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nomenclature_code = _parse_nomenclature_code(d.pop("nomenclatureCode", UNSET))

        def _parse_item_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_code = _parse_item_code(d.pop("itemCode", UNSET))

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

        _adding_type = d.pop("addingType", UNSET)
        adding_type: Union[Unset, NebularApiEnumsAddingTypeEnum]
        if isinstance(_adding_type, Unset):
            adding_type = UNSET
        else:
            adding_type = NebularApiEnumsAddingTypeEnum(_adding_type)

        _added_at = d.pop("addedAt", UNSET)
        added_at: Union[Unset, datetime.datetime]
        if isinstance(_added_at, Unset):
            added_at = UNSET
        else:
            added_at = isoparse(_added_at)

        editable = d.pop("editable", UNSET)

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_agent_info(data: object) -> Union["NebularApiModelsIntegrationsAgentInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_info_type_1 = NebularApiModelsIntegrationsAgentInfo.from_dict(data)

                return agent_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsAgentInfo", None, Unset], data)

        agent_info = _parse_agent_info(d.pop("agentInfo", UNSET))

        def _parse_unit_of_measurement(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit_of_measurement = _parse_unit_of_measurement(d.pop("unitOfMeasurement", UNSET))

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

        def _parse_additional_attribute(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_attribute = _parse_additional_attribute(d.pop("additionalAttribute", UNSET))

        def _parse_manufacturer_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer_country_code = _parse_manufacturer_country_code(d.pop("manufacturerCountryCode", UNSET))

        def _parse_customs_declaration_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customs_declaration_number = _parse_customs_declaration_number(d.pop("customsDeclarationNumber", UNSET))

        def _parse_supplier_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_inn = _parse_supplier_inn(d.pop("supplierINN", UNSET))

        def _parse_supplier_info(data: object) -> Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                supplier_info_type_1 = NebularApiModelsIntegrationsSupplierInfo.from_dict(data)

                return supplier_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset], data)

        supplier_info = _parse_supplier_info(d.pop("supplierInfo", UNSET))

        def _parse_excise(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        excise = _parse_excise(d.pop("excise", UNSET))

        def _parse_agent_type(data: object) -> Union[NebularApiEnumsAgentTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                agent_type_type_1 = NebularApiEnumsAgentTypeEnum(data)

                return agent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsAgentTypeEnum, None, Unset], data)

        agent_type = _parse_agent_type(d.pop("agentType", UNSET))

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

        discount_percent = d.pop("discountPercent", UNSET)

        max_discount_percent = d.pop("maxDiscountPercent", UNSET)

        min_price = d.pop("minPrice", UNSET)

        is_weight = d.pop("isWeight", UNSET)

        nebular_api_models_common_api_order_dto_extended_position = cls(
            quantity=quantity,
            price=price,
            tax=tax,
            payment_method_type=payment_method_type,
            payment_subject_type=payment_subject_type,
            sold_amount=sold_amount,
            sku=sku,
            id=id,
            discount_money=discount_money,
            position_id=position_id,
            marking_type=marking_type,
            nomenclature_code=nomenclature_code,
            item_code=item_code,
            barcodes=barcodes,
            adding_type=adding_type,
            added_at=added_at,
            editable=editable,
            text=text,
            agent_info=agent_info,
            unit_of_measurement=unit_of_measurement,
            unit_code=unit_code,
            additional_attribute=additional_attribute,
            manufacturer_country_code=manufacturer_country_code,
            customs_declaration_number=customs_declaration_number,
            supplier_inn=supplier_inn,
            supplier_info=supplier_info,
            excise=excise,
            agent_type=agent_type,
            custom_properties=custom_properties,
            industry_attribute=industry_attribute,
            no_return=no_return,
            discount_percent=discount_percent,
            max_discount_percent=max_discount_percent,
            min_price=min_price,
            is_weight=is_weight,
        )

        return nebular_api_models_common_api_order_dto_extended_position
