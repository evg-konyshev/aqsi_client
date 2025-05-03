from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_agent_type_enum import NebularApiEnumsAgentTypeEnum
from ..models.nebular_api_enums_doc_type_enum import NebularApiEnumsDocTypeEnum
from ..models.nebular_api_enums_electronic_check_enum import NebularApiEnumsElectronicCheckEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_customer_info import NebularApiModelsCommonApiCustomerInfo
    from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
    from ..models.nebular_api_models_common_api_order_dto_position import NebularApiModelsCommonApiOrderDtoPosition
    from ..models.nebular_api_models_integrations_additional_user_attribute import (
        NebularApiModelsIntegrationsAdditionalUserAttribute,
    )
    from ..models.nebular_api_models_integrations_order_check_close import NebularApiModelsIntegrationsOrderCheckClose


T = TypeVar("T", bound="NebularApiModelsCommonApiOrderDtoContent")


@_attrs_define
class NebularApiModelsCommonApiOrderDtoContent:
    """<div class="apidocs-russian"> Содержимое документа</div>
    <div class="apidocs-english">Document content</div>

        Attributes:
            discount_money (Union[Unset, float]): <div class="apidocs-russian">Скидка на заказ, рубли</div>
                <div class="apidocs-english">Order discount, rubles</div>
            discount_percent (Union[Unset, float]): <div class="apidocs-russian">Скидка на заказ, проценты</div>
                <div class="apidocs-english">Order discount, percent</div>
            type_ (Union[NebularApiEnumsDocTypeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2,</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Признак расчета, 1054</div>
                <div class="apidocs-english tag-value">Payment type, 1054</div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Приход</div><div class="apidocs-english">Income</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">2</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Возврат прихода</div><div class="apidocs-english">Income
                return</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">3</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Расход</div><div class="apidocs-english">Outcome</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">4</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Возврат расхода</div><div class="apidocs-english">Outcome
                return</div></div>
            positions (Union[None, Unset, list['NebularApiModelsCommonApiOrderDtoPosition']]): <div class="apidocs-russian
                apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Список предметов расчета, 1059</div>
                <div class="apidocs-english tag-value">Position list, 1059</div>
            check_close (Union['NebularApiModelsIntegrationsOrderCheckClose', None, Unset]): <div class="apidocs-
                russian">Параметры закрытия чека</div>
                <div class="apidocs-english">Check closing options</div>
            customer_contact (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует:
                ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Телефон или электронный адрес покупателя, 1008</div>
                <div class="apidocs-english tag-value">Buyer's Phone or Email, 1008</div>
            payment_agent_operation (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Операция платежного агента, 1044</div>
                <div class="apidocs-english tag-value">Payment agent operation, 1044</div>
            payment_operator_name (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Наименование оператора перевода, 1026</div>
                <div class="apidocs-english tag-value">Name of the payment operator, 1026</div>
            payment_operator_address (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Адрес оператора перевода, 1005</div>
                <div class="apidocs-english tag-value">Payment operator address, 1005</div>
            payment_operator_inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">ИНН оператора перевода, 1016</div>
                <div class="apidocs-english tag-value">TIN of a payment operator, 1016</div>
            agent_type (Union[NebularApiEnumsAgentTypeEnum, None, Unset]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Признак агента, 1057.Может принимать несколько значений сразу, выраженных
                как сумма доступных числовых значений.</div>
                <div class="apidocs-english tag-value">Agent type, 1057. Can accept multiple values as sum of valid numeric
                values.</div>
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
            payment_transfer_operator_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-
                ffd-availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Телефон оператора перевода, 1075
                             Массив строк длиной от 1 до 19 символов, формат +{Ц}, необязательное поле</div>
                <div class="apidocs-english tag-value">Phone number of the transfer operator, 1075
                             Array of strings from 1 to 19 characters long, format +{D}, optional field</div>
            payment_agent_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Телефон платежного агента, 1073</div>
                <div class="apidocs-english tag-value">Payment agent phone numbers , 1073</div>
            payment_operator_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Телефон оператора по приему платежей, 1074
                             Массив строк длиной от 1 до 19 символов, формат +{Ц}, необязательное поле</div>
                <div class="apidocs-english tag-value"> Payment operator phone numbers
                             Array of strings from 1 to 19 characters long, format +{D}, optional field
                            </div>
            supplier_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05</div>
                <div class="apidocs-russian tag-value">Телефон поставщика, 1171</div>
                <div class="apidocs-english tag-value">Supplier phone numbers, 1171</div>
            additional_user_attribute (Union['NebularApiModelsIntegrationsAdditionalUserAttribute', None, Unset]): <div
                class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Дополнительный реквизит пользователя, 1084</div>
                <div class="apidocs-english tag-value">Additional user attribute, 1084</div>
            automat_number (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует:
                ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Номер вендингового автомата, 1036</div>
                <div class="apidocs-english tag-value">Vending machine number</div>
            settlement_address (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Адрес расчетов, 1009 (передавать только при фискализации на разъездную
                торговлю)</div>
                <div class="apidocs-english tag-value">Settlement address, 1009 (set only in case of fiscalization for traveling
                trade)</div>
            settlement_place (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует:
                ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Место расчетов, 1187 (передавать только при фискализации на разъездную
                торговлю)</div>
                <div class="apidocs-english tag-value">Settlement place, , 1187 (set only in case of fiscalization for traveling
                trade)</div>
            additional_attribute (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Дополнительный реквизит чека(БСО), 1192</div>
                <div class="apidocs-english tag-value">Additional attribute, 1192</div>
            customer (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
                1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Покупатель (клиент), 1227</div>
                <div class="apidocs-english tag-value">Buyer (Client), 1227</div>
            customer_inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД
                1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">ИНН покупателя (клиента), 1228 - поле не может принимать в качестве
                значения пустую строку</div>
                <div class="apidocs-english tag-value">TIN of the buyer (client), 1228 - empty string is not a valid value</div>
            customer_info (Union['NebularApiModelsCommonApiCustomerInfo', None, Unset]): <div class="apidocs-russian
                apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
                <div class="apidocs-russian tag-value">Сведения о покупателе(клиенте), 1256</div>
                <div class="apidocs-english tag-value">Customer info, 1256</div>
            industry_attribute (Union['NebularApiModelsCommonApiIndustryAttribute', None, Unset]): <div class="apidocs-
                russian apidocs-ffd-availability">Соответствует: ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.2</div>
                <div class="apidocs-russian tag-value">Отраслевой реквизит чека, 1261</div>
                <div class="apidocs-english tag-value">Receipt industry attribute, 1261</div>
            electronic_check (Union[NebularApiEnumsElectronicCheckEnum, None, Unset]): <div class="apidocs-russian">Данный
                параметр отключает печать фискального документа средствами кассы. И Активирует отправку электронной версии чека
                продажи на контакт указанный в клиенте</div>
                <div class="apidocs-english">Parameter disables paper receipt printing and enables electronic receipt being sent
                to client email or phone number</div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">0</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Печатать</div><div class="apidocs-english">Paper
                receipt</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
                0.25em;">-</div><div class="apidocs-russian">Не печатать</div><div class="apidocs-english">Electronic
                receipt</div></div>
    """

    discount_money: Union[Unset, float] = UNSET
    discount_percent: Union[Unset, float] = UNSET
    type_: Union[NebularApiEnumsDocTypeEnum, None, Unset] = UNSET
    positions: Union[None, Unset, list["NebularApiModelsCommonApiOrderDtoPosition"]] = UNSET
    check_close: Union["NebularApiModelsIntegrationsOrderCheckClose", None, Unset] = UNSET
    customer_contact: Union[None, Unset, str] = UNSET
    payment_agent_operation: Union[None, Unset, str] = UNSET
    payment_operator_name: Union[None, Unset, str] = UNSET
    payment_operator_address: Union[None, Unset, str] = UNSET
    payment_operator_inn: Union[None, Unset, str] = UNSET
    agent_type: Union[NebularApiEnumsAgentTypeEnum, None, Unset] = UNSET
    payment_transfer_operator_phone_numbers: Union[None, Unset, list[str]] = UNSET
    payment_agent_phone_numbers: Union[None, Unset, list[str]] = UNSET
    payment_operator_phone_numbers: Union[None, Unset, list[str]] = UNSET
    supplier_phone_numbers: Union[None, Unset, list[str]] = UNSET
    additional_user_attribute: Union["NebularApiModelsIntegrationsAdditionalUserAttribute", None, Unset] = UNSET
    automat_number: Union[None, Unset, str] = UNSET
    settlement_address: Union[None, Unset, str] = UNSET
    settlement_place: Union[None, Unset, str] = UNSET
    additional_attribute: Union[None, Unset, str] = UNSET
    customer: Union[None, Unset, str] = UNSET
    customer_inn: Union[None, Unset, str] = UNSET
    customer_info: Union["NebularApiModelsCommonApiCustomerInfo", None, Unset] = UNSET
    industry_attribute: Union["NebularApiModelsCommonApiIndustryAttribute", None, Unset] = UNSET
    electronic_check: Union[NebularApiEnumsElectronicCheckEnum, None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_customer_info import NebularApiModelsCommonApiCustomerInfo
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_integrations_additional_user_attribute import (
            NebularApiModelsIntegrationsAdditionalUserAttribute,
        )
        from ..models.nebular_api_models_integrations_order_check_close import (
            NebularApiModelsIntegrationsOrderCheckClose,
        )

        discount_money = self.discount_money

        discount_percent = self.discount_percent

        type_: Union[None, Unset, int]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, NebularApiEnumsDocTypeEnum):
            type_ = self.type_.value
        else:
            type_ = self.type_

        positions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.positions, Unset):
            positions = UNSET
        elif isinstance(self.positions, list):
            positions = []
            for positions_type_0_item_data in self.positions:
                positions_type_0_item = positions_type_0_item_data.to_dict()
                positions.append(positions_type_0_item)

        else:
            positions = self.positions

        check_close: Union[None, Unset, dict[str, Any]]
        if isinstance(self.check_close, Unset):
            check_close = UNSET
        elif isinstance(self.check_close, NebularApiModelsIntegrationsOrderCheckClose):
            check_close = self.check_close.to_dict()
        else:
            check_close = self.check_close

        customer_contact: Union[None, Unset, str]
        if isinstance(self.customer_contact, Unset):
            customer_contact = UNSET
        else:
            customer_contact = self.customer_contact

        payment_agent_operation: Union[None, Unset, str]
        if isinstance(self.payment_agent_operation, Unset):
            payment_agent_operation = UNSET
        else:
            payment_agent_operation = self.payment_agent_operation

        payment_operator_name: Union[None, Unset, str]
        if isinstance(self.payment_operator_name, Unset):
            payment_operator_name = UNSET
        else:
            payment_operator_name = self.payment_operator_name

        payment_operator_address: Union[None, Unset, str]
        if isinstance(self.payment_operator_address, Unset):
            payment_operator_address = UNSET
        else:
            payment_operator_address = self.payment_operator_address

        payment_operator_inn: Union[None, Unset, str]
        if isinstance(self.payment_operator_inn, Unset):
            payment_operator_inn = UNSET
        else:
            payment_operator_inn = self.payment_operator_inn

        agent_type: Union[None, Unset, int]
        if isinstance(self.agent_type, Unset):
            agent_type = UNSET
        elif isinstance(self.agent_type, NebularApiEnumsAgentTypeEnum):
            agent_type = self.agent_type.value
        else:
            agent_type = self.agent_type

        payment_transfer_operator_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_transfer_operator_phone_numbers, Unset):
            payment_transfer_operator_phone_numbers = UNSET
        elif isinstance(self.payment_transfer_operator_phone_numbers, list):
            payment_transfer_operator_phone_numbers = self.payment_transfer_operator_phone_numbers

        else:
            payment_transfer_operator_phone_numbers = self.payment_transfer_operator_phone_numbers

        payment_agent_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_agent_phone_numbers, Unset):
            payment_agent_phone_numbers = UNSET
        elif isinstance(self.payment_agent_phone_numbers, list):
            payment_agent_phone_numbers = self.payment_agent_phone_numbers

        else:
            payment_agent_phone_numbers = self.payment_agent_phone_numbers

        payment_operator_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_operator_phone_numbers, Unset):
            payment_operator_phone_numbers = UNSET
        elif isinstance(self.payment_operator_phone_numbers, list):
            payment_operator_phone_numbers = self.payment_operator_phone_numbers

        else:
            payment_operator_phone_numbers = self.payment_operator_phone_numbers

        supplier_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.supplier_phone_numbers, Unset):
            supplier_phone_numbers = UNSET
        elif isinstance(self.supplier_phone_numbers, list):
            supplier_phone_numbers = self.supplier_phone_numbers

        else:
            supplier_phone_numbers = self.supplier_phone_numbers

        additional_user_attribute: Union[None, Unset, dict[str, Any]]
        if isinstance(self.additional_user_attribute, Unset):
            additional_user_attribute = UNSET
        elif isinstance(self.additional_user_attribute, NebularApiModelsIntegrationsAdditionalUserAttribute):
            additional_user_attribute = self.additional_user_attribute.to_dict()
        else:
            additional_user_attribute = self.additional_user_attribute

        automat_number: Union[None, Unset, str]
        if isinstance(self.automat_number, Unset):
            automat_number = UNSET
        else:
            automat_number = self.automat_number

        settlement_address: Union[None, Unset, str]
        if isinstance(self.settlement_address, Unset):
            settlement_address = UNSET
        else:
            settlement_address = self.settlement_address

        settlement_place: Union[None, Unset, str]
        if isinstance(self.settlement_place, Unset):
            settlement_place = UNSET
        else:
            settlement_place = self.settlement_place

        additional_attribute: Union[None, Unset, str]
        if isinstance(self.additional_attribute, Unset):
            additional_attribute = UNSET
        else:
            additional_attribute = self.additional_attribute

        customer: Union[None, Unset, str]
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        customer_inn: Union[None, Unset, str]
        if isinstance(self.customer_inn, Unset):
            customer_inn = UNSET
        else:
            customer_inn = self.customer_inn

        customer_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.customer_info, Unset):
            customer_info = UNSET
        elif isinstance(self.customer_info, NebularApiModelsCommonApiCustomerInfo):
            customer_info = self.customer_info.to_dict()
        else:
            customer_info = self.customer_info

        industry_attribute: Union[None, Unset, dict[str, Any]]
        if isinstance(self.industry_attribute, Unset):
            industry_attribute = UNSET
        elif isinstance(self.industry_attribute, NebularApiModelsCommonApiIndustryAttribute):
            industry_attribute = self.industry_attribute.to_dict()
        else:
            industry_attribute = self.industry_attribute

        electronic_check: Union[None, Unset, int]
        if isinstance(self.electronic_check, Unset):
            electronic_check = UNSET
        elif isinstance(self.electronic_check, NebularApiEnumsElectronicCheckEnum):
            electronic_check = self.electronic_check.value
        else:
            electronic_check = self.electronic_check

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if discount_money is not UNSET:
            field_dict["discountMoney"] = discount_money
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if type_ is not UNSET:
            field_dict["type"] = type_
        if positions is not UNSET:
            field_dict["positions"] = positions
        if check_close is not UNSET:
            field_dict["checkClose"] = check_close
        if customer_contact is not UNSET:
            field_dict["customerContact"] = customer_contact
        if payment_agent_operation is not UNSET:
            field_dict["paymentAgentOperation"] = payment_agent_operation
        if payment_operator_name is not UNSET:
            field_dict["paymentOperatorName"] = payment_operator_name
        if payment_operator_address is not UNSET:
            field_dict["paymentOperatorAddress"] = payment_operator_address
        if payment_operator_inn is not UNSET:
            field_dict["paymentOperatorINN"] = payment_operator_inn
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type
        if payment_transfer_operator_phone_numbers is not UNSET:
            field_dict["paymentTransferOperatorPhoneNumbers"] = payment_transfer_operator_phone_numbers
        if payment_agent_phone_numbers is not UNSET:
            field_dict["paymentAgentPhoneNumbers"] = payment_agent_phone_numbers
        if payment_operator_phone_numbers is not UNSET:
            field_dict["paymentOperatorPhoneNumbers"] = payment_operator_phone_numbers
        if supplier_phone_numbers is not UNSET:
            field_dict["supplierPhoneNumbers"] = supplier_phone_numbers
        if additional_user_attribute is not UNSET:
            field_dict["additionalUserAttribute"] = additional_user_attribute
        if automat_number is not UNSET:
            field_dict["automatNumber"] = automat_number
        if settlement_address is not UNSET:
            field_dict["settlementAddress"] = settlement_address
        if settlement_place is not UNSET:
            field_dict["settlementPlace"] = settlement_place
        if additional_attribute is not UNSET:
            field_dict["additionalAttribute"] = additional_attribute
        if customer is not UNSET:
            field_dict["customer"] = customer
        if customer_inn is not UNSET:
            field_dict["customerINN"] = customer_inn
        if customer_info is not UNSET:
            field_dict["customerInfo"] = customer_info
        if industry_attribute is not UNSET:
            field_dict["industryAttribute"] = industry_attribute
        if electronic_check is not UNSET:
            field_dict["electronicCheck"] = electronic_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_customer_info import NebularApiModelsCommonApiCustomerInfo
        from ..models.nebular_api_models_common_api_industry_attribute import NebularApiModelsCommonApiIndustryAttribute
        from ..models.nebular_api_models_common_api_order_dto_position import NebularApiModelsCommonApiOrderDtoPosition
        from ..models.nebular_api_models_integrations_additional_user_attribute import (
            NebularApiModelsIntegrationsAdditionalUserAttribute,
        )
        from ..models.nebular_api_models_integrations_order_check_close import (
            NebularApiModelsIntegrationsOrderCheckClose,
        )

        d = dict(src_dict)
        discount_money = d.pop("discountMoney", UNSET)

        discount_percent = d.pop("discountPercent", UNSET)

        def _parse_type_(data: object) -> Union[NebularApiEnumsDocTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                type_type_1 = NebularApiEnumsDocTypeEnum(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsDocTypeEnum, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_positions(data: object) -> Union[None, Unset, list["NebularApiModelsCommonApiOrderDtoPosition"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positions_type_0 = []
                _positions_type_0 = data
                for positions_type_0_item_data in _positions_type_0:
                    positions_type_0_item = NebularApiModelsCommonApiOrderDtoPosition.from_dict(
                        positions_type_0_item_data
                    )

                    positions_type_0.append(positions_type_0_item)

                return positions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsCommonApiOrderDtoPosition"]], data)

        positions = _parse_positions(d.pop("positions", UNSET))

        def _parse_check_close(data: object) -> Union["NebularApiModelsIntegrationsOrderCheckClose", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                check_close_type_1 = NebularApiModelsIntegrationsOrderCheckClose.from_dict(data)

                return check_close_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsOrderCheckClose", None, Unset], data)

        check_close = _parse_check_close(d.pop("checkClose", UNSET))

        def _parse_customer_contact(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer_contact = _parse_customer_contact(d.pop("customerContact", UNSET))

        def _parse_payment_agent_operation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_agent_operation = _parse_payment_agent_operation(d.pop("paymentAgentOperation", UNSET))

        def _parse_payment_operator_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_name = _parse_payment_operator_name(d.pop("paymentOperatorName", UNSET))

        def _parse_payment_operator_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_address = _parse_payment_operator_address(d.pop("paymentOperatorAddress", UNSET))

        def _parse_payment_operator_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_inn = _parse_payment_operator_inn(d.pop("paymentOperatorINN", UNSET))

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

        def _parse_payment_transfer_operator_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_transfer_operator_phone_numbers_type_0 = cast(list[str], data)

                return payment_transfer_operator_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_transfer_operator_phone_numbers = _parse_payment_transfer_operator_phone_numbers(
            d.pop("paymentTransferOperatorPhoneNumbers", UNSET)
        )

        def _parse_payment_agent_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_agent_phone_numbers_type_0 = cast(list[str], data)

                return payment_agent_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_agent_phone_numbers = _parse_payment_agent_phone_numbers(d.pop("paymentAgentPhoneNumbers", UNSET))

        def _parse_payment_operator_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_operator_phone_numbers_type_0 = cast(list[str], data)

                return payment_operator_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_operator_phone_numbers = _parse_payment_operator_phone_numbers(
            d.pop("paymentOperatorPhoneNumbers", UNSET)
        )

        def _parse_supplier_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supplier_phone_numbers_type_0 = cast(list[str], data)

                return supplier_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        supplier_phone_numbers = _parse_supplier_phone_numbers(d.pop("supplierPhoneNumbers", UNSET))

        def _parse_additional_user_attribute(
            data: object,
        ) -> Union["NebularApiModelsIntegrationsAdditionalUserAttribute", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_user_attribute_type_1 = NebularApiModelsIntegrationsAdditionalUserAttribute.from_dict(data)

                return additional_user_attribute_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsAdditionalUserAttribute", None, Unset], data)

        additional_user_attribute = _parse_additional_user_attribute(d.pop("additionalUserAttribute", UNSET))

        def _parse_automat_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        automat_number = _parse_automat_number(d.pop("automatNumber", UNSET))

        def _parse_settlement_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        settlement_address = _parse_settlement_address(d.pop("settlementAddress", UNSET))

        def _parse_settlement_place(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        settlement_place = _parse_settlement_place(d.pop("settlementPlace", UNSET))

        def _parse_additional_attribute(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_attribute = _parse_additional_attribute(d.pop("additionalAttribute", UNSET))

        def _parse_customer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer = _parse_customer(d.pop("customer", UNSET))

        def _parse_customer_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer_inn = _parse_customer_inn(d.pop("customerINN", UNSET))

        def _parse_customer_info(data: object) -> Union["NebularApiModelsCommonApiCustomerInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                customer_info_type_1 = NebularApiModelsCommonApiCustomerInfo.from_dict(data)

                return customer_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCustomerInfo", None, Unset], data)

        customer_info = _parse_customer_info(d.pop("customerInfo", UNSET))

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

        def _parse_electronic_check(data: object) -> Union[NebularApiEnumsElectronicCheckEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                electronic_check_type_1 = NebularApiEnumsElectronicCheckEnum(data)

                return electronic_check_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsElectronicCheckEnum, None, Unset], data)

        electronic_check = _parse_electronic_check(d.pop("electronicCheck", UNSET))

        nebular_api_models_common_api_order_dto_content = cls(
            discount_money=discount_money,
            discount_percent=discount_percent,
            type_=type_,
            positions=positions,
            check_close=check_close,
            customer_contact=customer_contact,
            payment_agent_operation=payment_agent_operation,
            payment_operator_name=payment_operator_name,
            payment_operator_address=payment_operator_address,
            payment_operator_inn=payment_operator_inn,
            agent_type=agent_type,
            payment_transfer_operator_phone_numbers=payment_transfer_operator_phone_numbers,
            payment_agent_phone_numbers=payment_agent_phone_numbers,
            payment_operator_phone_numbers=payment_operator_phone_numbers,
            supplier_phone_numbers=supplier_phone_numbers,
            additional_user_attribute=additional_user_attribute,
            automat_number=automat_number,
            settlement_address=settlement_address,
            settlement_place=settlement_place,
            additional_attribute=additional_attribute,
            customer=customer,
            customer_inn=customer_inn,
            customer_info=customer_info,
            industry_attribute=industry_attribute,
            electronic_check=electronic_check,
        )

        return nebular_api_models_common_api_order_dto_content
