import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.nebular_api_enums_adding_type_enum import NebularApiEnumsAddingTypeEnum
from ..models.nebular_api_enums_agent_type_enum import NebularApiEnumsAgentTypeEnum
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
    from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo
    from ..models.nebular_api_models_receipt_models_loyalty import NebularApiModelsReceiptModelsLoyalty
    from ..models.nebular_api_models_receipt_models_modifier_option_pointer import (
        NebularApiModelsReceiptModelsModifierOptionPointer,
    )


T = TypeVar("T", bound="NebularApiModelsReceiptModelsReceiptPositionV32")


@_attrs_define
class NebularApiModelsReceiptModelsReceiptPositionV32:
    """
    Attributes:
        id (str): <div class="apidocs-russian">UUID товара (NOTE: пустая строка, если по свободной цене)</div>
            <div class="apidocs-english">UUID of the product (NOTE: an empty string, if at a free price)</div>
        payment_method_type (NebularApiEnumsPaymentMethodTypeEnum): Способ расчета, 1214
        payment_subject_type (NebularApiEnumsPaymentSubjectTypeEnum): Предмет расчета, 1212
        price (float): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Стоимость единицы предмета расчета</div>
            <div class="apidocs-english tag-value">Unit Cost</div>
        price_brutto (float): <div class="apidocs-russian">Цена до применения скидок</div>
            <div class="apidocs-english">Price before applying discounts</div>
        quantity (float): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Количество предмета расчета</div>
            <div class="apidocs-english tag-value">Quantity</div>
        tax (NebularApiEnumsVATRateEnum): Ставка НДС, 1199
        text (str): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Наименование предмета расчета(товара)</div>
            <div class="apidocs-english tag-value">Position name</div>
        discount_money (Union[Unset, float]): <div class="apidocs-russian">Скидка по позиции, рубли</div>
            <div class="apidocs-english">Discount on position, rubles</div>
        discount_percent (Union[Unset, float]): <div class="apidocs-russian">Скидка по позиции, проценты</div>
            <div class="apidocs-english">Discount on position, percentage</div>
        external_id (Union[None, Unset, str]): <div class="apidocs-russian">Уникальный идентификатор товара в рамках
            аккаунта</div>
            <div class="apidocs-english">Goods account-wide unique identifier</div>
        sku (Union[None, Unset, str]): <div class="apidocs-russian">Код товара</div>
            <div class="apidocs-english">Product code</div>
        modify_options (Union[None, Unset, list['NebularApiModelsReceiptModelsModifierOptionPointer']]): <div
            class="apidocs-russian">Опции модификаторов товара, выбранные при продаже</div>
            <div class="apidocs-english">Product modifier options selected at the time of sale</div>
        loyalties (Union[None, Unset, list['NebularApiModelsReceiptModelsLoyalty']]): <div class="apidocs-
            russian">Cписок акций, примененных на позицию</div>
            <div class="apidocs-english">List of Loyalty offers for position</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
        min_price (Union[None, Unset, float]): <div class="apidocs-russian">Минимальная цена, за которую может быть
            продан товар из этой позиции чека</div>
            <div class="apidocs-english">The minimum price for which goods from this check item can be sold</div>
        supplier_info (Union['NebularApiModelsIntegrationsSupplierInfo', None, Unset]): <div class="apidocs-russian
            apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Данные поставщика, 1224</div>
            <div class="apidocs-english tag-value">Supplier info, 1224</div>
        supplier_inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">ИНН поставщика, 1226</div>
            <div class="apidocs-english tag-value">TIN of the supplier, 1226</div>
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
        agent_info (Union['NebularApiModelsIntegrationsAgentInfo', None, Unset]): <div class="apidocs-russian apidocs-
            ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Данные агента, 1223 (На текущий момент длина сериализованных данных тэга
            не должна превышать 243 байта)</div>
            <div class="apidocs-english tag-value">Agent Data, 1223 (Currently, the length of serialized tag data should not
            exceed 243 bytes)</div>
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
        excise (Union[None, Unset, float]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05, ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Акциз, 1229</div>
            <div class="apidocs-english tag-value">Excise, 1229</div>
        index (Union[Unset, int]):
        added_at (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Дата и время добавления позиции в
            чек или её последнего изменения</div>
            <div class="apidocs-english">Date and time the item was added to the check or its last change</div>
        barcodes (Union[None, Unset, list[str]]): <div class="apidocs-russian">Список штрих-кодов позиции чека</div>
            <div class="apidocs-english">Barcode list of receipt position</div>
        adding_type (Union[Unset, NebularApiEnumsAddingTypeEnum]):
        tax_amount (Union[Unset, float]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05,
            ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
            <div class="apidocs-russian tag-value">Сумма налога по позиции</div>
            <div class="apidocs-english tag-value">Position tax amount</div>
        max_discount_percent (Union[None, Unset, float]): <div class="apidocs-russian">Максимальный процент скидки</div>
            <div class="apidocs-english">Maximum discount percentage</div>
        slot_info (Union['NebularApiModelsLkServiceSlotInfo', None, Unset]): <div class="apidocs-russian">Информация о
            слоте</div>
            <div class="apidocs-english">Slot info</div>
        parent_index (Union[None, Unset, int]): <div class="apidocs-russian">Номер позиции в оригинальном чеке (для чека
            возврата)</div>
            <div class="apidocs-english">Item number in the original receipt (for return receipt)</div>
        unit (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.05</div>
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
        industry_attribute (Union['NebularApiModelsCommonApiIndustryAttribute', None, Unset]): <div class="apidocs-
            russian apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Отраслевой реквизит предмета расчёта, 1260</div>
            <div class="apidocs-english tag-value">Position industry attribute, 1260</div>
        nomenclature_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
            availability">Соответствует: ФФД 1.05</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
            <div class="apidocs-russian tag-value">Код товарной номенклатуры, 1162 (Строка, содержащая base64 кодированный
            массив от 1 до 32 байт либо null)</div>
            <div class="apidocs-english tag-value">Commodity nomenclature code, 1162 (a string containing a base64 encoded
            array of 1 to 32 bytes or null)</div>
        nomenclature_string (Union[None, Unset, str]): <div class="apidocs-russian">Непреобразованное значение
            считанного сканером кода товарной номенклатуры</div>
            <div class="apidocs-english">Unconverted value of the item code read by the scanner</div>
        item_code (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
            1.2</div>
            <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
            <div class="apidocs-russian tag-value">Код Маркированного товара в явном виде (GS-символ спецкод используется
            для разделения групп информации), 2000</div>
            <div class="apidocs-english tag-value">Item code as scanned from barcode with GS symbols, 2000</div>
    """

    id: str
    payment_method_type: NebularApiEnumsPaymentMethodTypeEnum
    payment_subject_type: NebularApiEnumsPaymentSubjectTypeEnum
    price: float
    price_brutto: float
    quantity: float
    tax: NebularApiEnumsVATRateEnum
    text: str
    discount_money: Union[Unset, float] = UNSET
    discount_percent: Union[Unset, float] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    sku: Union[None, Unset, str] = UNSET
    modify_options: Union[None, Unset, list["NebularApiModelsReceiptModelsModifierOptionPointer"]] = UNSET
    loyalties: Union[None, Unset, list["NebularApiModelsReceiptModelsLoyalty"]] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    min_price: Union[None, Unset, float] = UNSET
    supplier_info: Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset] = UNSET
    supplier_inn: Union[None, Unset, str] = UNSET
    agent_type: Union[NebularApiEnumsAgentTypeEnum, None, Unset] = UNSET
    agent_info: Union["NebularApiModelsIntegrationsAgentInfo", None, Unset] = UNSET
    additional_attribute: Union[None, Unset, str] = UNSET
    manufacturer_country_code: Union[None, Unset, str] = UNSET
    customs_declaration_number: Union[None, Unset, str] = UNSET
    excise: Union[None, Unset, float] = UNSET
    index: Union[Unset, int] = UNSET
    added_at: Union[None, Unset, datetime.datetime] = UNSET
    barcodes: Union[None, Unset, list[str]] = UNSET
    adding_type: Union[Unset, NebularApiEnumsAddingTypeEnum] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    max_discount_percent: Union[None, Unset, float] = UNSET
    slot_info: Union["NebularApiModelsLkServiceSlotInfo", None, Unset] = UNSET
    parent_index: Union[None, Unset, int] = UNSET
    unit: Union[None, Unset, str] = UNSET
    unit_code: Union[NebularApiEnumsUnitCodeEnum, None, Unset] = UNSET
    industry_attribute: Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset] = UNSET
    nomenclature_code: Union[None, Unset, str] = UNSET
    nomenclature_string: Union[None, Unset, str] = UNSET
    item_code: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo
        from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo

        id = self.id

        payment_method_type = self.payment_method_type.value

        payment_subject_type = self.payment_subject_type.value

        price = self.price

        price_brutto = self.price_brutto

        quantity = self.quantity

        tax = self.tax.value

        text = self.text

        discount_money = self.discount_money

        discount_percent = self.discount_percent

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        modify_options: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.modify_options, Unset):
            modify_options = UNSET
        elif isinstance(self.modify_options, list):
            modify_options = []
            for modify_options_type_0_item_data in self.modify_options:
                modify_options_type_0_item = modify_options_type_0_item_data.to_dict()
                modify_options.append(modify_options_type_0_item)

        else:
            modify_options = self.modify_options

        loyalties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.loyalties, Unset):
            loyalties = UNSET
        elif isinstance(self.loyalties, list):
            loyalties = []
            for loyalties_type_0_item_data in self.loyalties:
                loyalties_type_0_item = loyalties_type_0_item_data.to_dict()
                loyalties.append(loyalties_type_0_item)

        else:
            loyalties = self.loyalties

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

        min_price: Union[None, Unset, float]
        if isinstance(self.min_price, Unset):
            min_price = UNSET
        else:
            min_price = self.min_price

        supplier_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.supplier_info, Unset):
            supplier_info = UNSET
        elif isinstance(self.supplier_info, NebularApiModelsIntegrationsSupplierInfo):
            supplier_info = self.supplier_info.to_dict()
        else:
            supplier_info = self.supplier_info

        supplier_inn: Union[None, Unset, str]
        if isinstance(self.supplier_inn, Unset):
            supplier_inn = UNSET
        else:
            supplier_inn = self.supplier_inn

        agent_type: Union[None, Unset, int]
        if isinstance(self.agent_type, Unset):
            agent_type = UNSET
        elif isinstance(self.agent_type, NebularApiEnumsAgentTypeEnum):
            agent_type = self.agent_type.value
        else:
            agent_type = self.agent_type

        agent_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.agent_info, Unset):
            agent_info = UNSET
        elif isinstance(self.agent_info, NebularApiModelsIntegrationsAgentInfo):
            agent_info = self.agent_info.to_dict()
        else:
            agent_info = self.agent_info

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

        excise: Union[None, Unset, float]
        if isinstance(self.excise, Unset):
            excise = UNSET
        else:
            excise = self.excise

        index = self.index

        added_at: Union[None, Unset, str]
        if isinstance(self.added_at, Unset):
            added_at = UNSET
        elif isinstance(self.added_at, datetime.datetime):
            added_at = self.added_at.isoformat()
        else:
            added_at = self.added_at

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

        tax_amount = self.tax_amount

        max_discount_percent: Union[None, Unset, float]
        if isinstance(self.max_discount_percent, Unset):
            max_discount_percent = UNSET
        else:
            max_discount_percent = self.max_discount_percent

        slot_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.slot_info, Unset):
            slot_info = UNSET
        elif isinstance(self.slot_info, NebularApiModelsLkServiceSlotInfo):
            slot_info = self.slot_info.to_dict()
        else:
            slot_info = self.slot_info

        parent_index: Union[None, Unset, int]
        if isinstance(self.parent_index, Unset):
            parent_index = UNSET
        else:
            parent_index = self.parent_index

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

        industry_attribute: Union[None, Unset, dict[str, Any]]
        if isinstance(self.industry_attribute, Unset):
            industry_attribute = UNSET
        elif isinstance(self.industry_attribute, NebularApiModelsCommonApiIndustryAttribute):
            industry_attribute = self.industry_attribute.to_dict()
        else:
            industry_attribute = self.industry_attribute

        nomenclature_code: Union[None, Unset, str]
        if isinstance(self.nomenclature_code, Unset):
            nomenclature_code = UNSET
        else:
            nomenclature_code = self.nomenclature_code

        nomenclature_string: Union[None, Unset, str]
        if isinstance(self.nomenclature_string, Unset):
            nomenclature_string = UNSET
        else:
            nomenclature_string = self.nomenclature_string

        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "paymentMethodType": payment_method_type,
                "paymentSubjectType": payment_subject_type,
                "price": price,
                "priceBrutto": price_brutto,
                "quantity": quantity,
                "tax": tax,
                "text": text,
            }
        )
        if discount_money is not UNSET:
            field_dict["discountMoney"] = discount_money
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if modify_options is not UNSET:
            field_dict["modifyOptions"] = modify_options
        if loyalties is not UNSET:
            field_dict["loyalties"] = loyalties
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if supplier_inn is not UNSET:
            field_dict["supplierINN"] = supplier_inn
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type
        if agent_info is not UNSET:
            field_dict["agentInfo"] = agent_info
        if additional_attribute is not UNSET:
            field_dict["additionalAttribute"] = additional_attribute
        if manufacturer_country_code is not UNSET:
            field_dict["manufacturerCountryCode"] = manufacturer_country_code
        if customs_declaration_number is not UNSET:
            field_dict["customsDeclarationNumber"] = customs_declaration_number
        if excise is not UNSET:
            field_dict["excise"] = excise
        if index is not UNSET:
            field_dict["index"] = index
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if adding_type is not UNSET:
            field_dict["addingType"] = adding_type
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if max_discount_percent is not UNSET:
            field_dict["maxDiscountPercent"] = max_discount_percent
        if slot_info is not UNSET:
            field_dict["slotInfo"] = slot_info
        if parent_index is not UNSET:
            field_dict["parentIndex"] = parent_index
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if industry_attribute is not UNSET:
            field_dict["industryAttribute"] = industry_attribute
        if nomenclature_code is not UNSET:
            field_dict["nomenclatureCode"] = nomenclature_code
        if nomenclature_string is not UNSET:
            field_dict["nomenclatureString"] = nomenclature_string
        if item_code is not UNSET:
            field_dict["itemCode"] = item_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_lk_service_slot_info import NebularApiModelsLkServiceSlotInfo
        from ..models.nebular_api_models_receipt_models_loyalty import NebularApiModelsReceiptModelsLoyalty
        from ..models.nebular_api_models_receipt_models_modifier_option_pointer import (
            NebularApiModelsReceiptModelsModifierOptionPointer,
        )

        d = dict(src_dict)
        id = d.pop("id")

        payment_method_type = NebularApiEnumsPaymentMethodTypeEnum(d.pop("paymentMethodType"))

        payment_subject_type = NebularApiEnumsPaymentSubjectTypeEnum(d.pop("paymentSubjectType"))

        price = d.pop("price")

        price_brutto = d.pop("priceBrutto")

        quantity = d.pop("quantity")

        tax = NebularApiEnumsVATRateEnum(d.pop("tax"))

        text = d.pop("text")

        discount_money = d.pop("discountMoney", UNSET)

        discount_percent = d.pop("discountPercent", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_modify_options(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsReceiptModelsModifierOptionPointer"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modify_options_type_0 = []
                _modify_options_type_0 = data
                for modify_options_type_0_item_data in _modify_options_type_0:
                    modify_options_type_0_item = NebularApiModelsReceiptModelsModifierOptionPointer.from_dict(
                        modify_options_type_0_item_data
                    )

                    modify_options_type_0.append(modify_options_type_0_item)

                return modify_options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsReceiptModelsModifierOptionPointer"]], data)

        modify_options = _parse_modify_options(d.pop("modifyOptions", UNSET))

        def _parse_loyalties(data: object) -> Union[None, Unset, list["NebularApiModelsReceiptModelsLoyalty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                loyalties_type_0 = []
                _loyalties_type_0 = data
                for loyalties_type_0_item_data in _loyalties_type_0:
                    loyalties_type_0_item = NebularApiModelsReceiptModelsLoyalty.from_dict(loyalties_type_0_item_data)

                    loyalties_type_0.append(loyalties_type_0_item)

                return loyalties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsReceiptModelsLoyalty"]], data)

        loyalties = _parse_loyalties(d.pop("loyalties", UNSET))

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

        def _parse_min_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_price = _parse_min_price(d.pop("minPrice", UNSET))

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

        def _parse_supplier_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_inn = _parse_supplier_inn(d.pop("supplierINN", UNSET))

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

        def _parse_excise(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        excise = _parse_excise(d.pop("excise", UNSET))

        index = d.pop("index", UNSET)

        def _parse_added_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_at_type_0 = isoparse(data)

                return added_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        added_at = _parse_added_at(d.pop("addedAt", UNSET))

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

        tax_amount = d.pop("taxAmount", UNSET)

        def _parse_max_discount_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_discount_percent = _parse_max_discount_percent(d.pop("maxDiscountPercent", UNSET))

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

        def _parse_parent_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_index = _parse_parent_index(d.pop("parentIndex", UNSET))

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

        def _parse_nomenclature_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nomenclature_code = _parse_nomenclature_code(d.pop("nomenclatureCode", UNSET))

        def _parse_nomenclature_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nomenclature_string = _parse_nomenclature_string(d.pop("nomenclatureString", UNSET))

        def _parse_item_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_code = _parse_item_code(d.pop("itemCode", UNSET))

        nebular_api_models_receipt_models_receipt_position_v32 = cls(
            id=id,
            payment_method_type=payment_method_type,
            payment_subject_type=payment_subject_type,
            price=price,
            price_brutto=price_brutto,
            quantity=quantity,
            tax=tax,
            text=text,
            discount_money=discount_money,
            discount_percent=discount_percent,
            external_id=external_id,
            sku=sku,
            modify_options=modify_options,
            loyalties=loyalties,
            custom_properties=custom_properties,
            min_price=min_price,
            supplier_info=supplier_info,
            supplier_inn=supplier_inn,
            agent_type=agent_type,
            agent_info=agent_info,
            additional_attribute=additional_attribute,
            manufacturer_country_code=manufacturer_country_code,
            customs_declaration_number=customs_declaration_number,
            excise=excise,
            index=index,
            added_at=added_at,
            barcodes=barcodes,
            adding_type=adding_type,
            tax_amount=tax_amount,
            max_discount_percent=max_discount_percent,
            slot_info=slot_info,
            parent_index=parent_index,
            unit=unit,
            unit_code=unit_code,
            industry_attribute=industry_attribute,
            nomenclature_code=nomenclature_code,
            nomenclature_string=nomenclature_string,
            item_code=item_code,
        )

        return nebular_api_models_receipt_models_receipt_position_v32
