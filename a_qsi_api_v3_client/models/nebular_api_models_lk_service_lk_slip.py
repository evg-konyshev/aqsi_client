from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.nebular_api_enums_cashless_payments_enum import NebularApiEnumsCashlessPaymentsEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_qr_pay_transaction import NebularApiModelsCommonApiQrPayTransaction
    from ..models.nebular_api_models_common_api_spasibo import NebularApiModelsCommonApiSpasibo
    from ..models.nebular_api_models_lk_service_get_receipt_cashier import NebularApiModelsLkServiceGetReceiptCashier


T = TypeVar("T", bound="NebularApiModelsLkServiceLkSlip")


@_attrs_define
class NebularApiModelsLkServiceLkSlip:
    """
    Attributes:
        type_ (str): <div class="apidocs-russian">Тип слипа. Возможные значения: `purchase`, `void`, `refund`,
            `purchasewithcashback`</div>
            <div class="apidocs-english">Type of slip. Possible values: `purchase`,` void`, `refund`,`
            purchasewithcashback`</div>
        cashier (Union['NebularApiModelsLkServiceGetReceiptCashier', None, Unset]): <div class="apidocs-russian">Модель
            кассира для отображения в чеке</div>
            <div class="apidocs-english">Cashier model for presentation in receipt</div>
        date (Union[None, Unset, str]): <div class="apidocs-russian">Дата операции</div>
            <div class="apidocs-english">Date of operation</div>
        cashier_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор кассира</div>
            <div class="apidocs-english">Cashier identifier</div>
        amount (Union[Unset, float]): <div class="apidocs-russian">Сумма</div>
            <div class="apidocs-english">Amount</div>
        tsi (Union[None, Unset, str]): <div class="apidocs-russian">TSI - атрибут слипа</div>
            <div class="apidocs-english">TSI - slip attribute</div>
        rrn (Union[None, Unset, str]): <div class="apidocs-russian">Аттрибут слипа. Номер операции для возвратов</div>
            <div class="apidocs-english">Slip attribute. Transaction number for returns</div>
        expiration_date (Union[None, Unset, str]): <div class="apidocs-russian">Дата окончания срока действия
            карты</div>
            <div class="apidocs-english">Card expiration date</div>
        company_name (Union[None, Unset, str]): <div class="apidocs-russian">Название организации</div>
            <div class="apidocs-english">Company name</div>
        customer_contact (Union[None, Unset, str]): <div class="apidocs-russian">Email или телефон клиента</div>
            <div class="apidocs-english">Email or customer phone</div>
        calculation_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес установки ККТ для проведения
            расчетов</div>
            <div class="apidocs-english">Cash register installation address</div>
        error_code (Union[None, Unset, str]): <div class="apidocs-russian">Код ошибки при оплате</div>
            <div class="apidocs-english">Payment error code</div>
        error_message (Union[None, Unset, str]): <div class="apidocs-russian">Описание ошибки при оплате</div>
            <div class="apidocs-english">Description of payment error</div>
        text (Union[None, Unset, str]): <div class="apidocs-russian">Текст слипа</div>
            <div class="apidocs-english">Slip text</div>
        cardholder (Union[None, Unset, str]): <div class="apidocs-russian">Имя держателя карты</div>
            <div class="apidocs-english">Card holder name</div>
        acquirer_agent_name (Union[None, Unset, str]): <div class="apidocs-russian">Посредник до банка эквайера</div>
            <div class="apidocs-english">Intermediary to the acquirer bank</div>
        cashless_type (Union[NebularApiEnumsCashlessPaymentsEnum, None, Unset]): <div class="apidocs-russian">Типы
            безналичной оплаты</div>
            <div class="apidocs-english">Types of cashless payments</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Безналичные</div><div class="apidocs-english">Cashless</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">2</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Картой</div><div class="apidocs-english">Card</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">3</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">QR-код</div><div class="apidocs-english">QR-code</div></div>
        qr_pay_transaction (Union['NebularApiModelsCommonApiQrPayTransaction', None, Unset]): <div class="apidocs-
            russian">Транзакция при оплате сервисом QR-Pay</div>
            <div class="apidocs-english">QR-Pay transaction (filled only in case of using QR-Pay service)</div>
        merchant_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор владельца терминала</div>
            <div class="apidocs-english">Terminal owner identifier</div>
        currency (Union[None, Unset, int]): <div class="apidocs-russian">Код валюты согласно ISO 4217 </div>
            <div class="apidocs-english">Currency code in ISO-4127</div>
        resp_code (Union[None, Unset, str]): <div class="apidocs-russian">Код ответа при оплате</div>
            <div class="apidocs-english">Payment response code</div>
        id (Union[None, UUID, Unset]): <div class="apidocs-russian">Uuid слипа</div>
            <div class="apidocs-english">Uuid slip</div>
        acquirer_bank_name (Union[None, Unset, str]): <div class="apidocs-russian">Наименование банка</div>
            <div class="apidocs-english">Acquirer bank name</div>
        transaction_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор операции в банке</div>
            <div class="apidocs-english">Bank transaction identifier</div>
        slip_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер слипа</div>
            <div class="apidocs-english">Slip number</div>
        approval_code (Union[None, Unset, str]): <div class="apidocs-russian">Код подтверждения</div>
            <div class="apidocs-english">Approval code</div>
        terminal_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор терминала</div>
            <div class="apidocs-english">Terminal identifier</div>
        spasibo (Union['NebularApiModelsCommonApiSpasibo', None, Unset]): <div class="apidocs-russian">"Спасибо"
            транзакции по платежу</div>
            <div class="apidocs-english">"Spasibo" transactions for a payment</div>
        mask_pan (Union[None, Unset, str]): <div class="apidocs-russian">Маскированный номер карты</div>
            <div class="apidocs-english">Masked card number</div>
        aid (Union[None, Unset, str]): <div class="apidocs-russian">AID - номер авторизации в сети</div>
            <div class="apidocs-english">AID - network authorization number</div>
        tvr (Union[None, Unset, str]): <div class="apidocs-russian">TVR - атрибут слипа</div>
            <div class="apidocs-english">TVR - slip attribute</div>
        apn (Union[None, Unset, str]): <div class="apidocs-russian">APN - атрибут слипа. Тип сети авторизации(Тип
            карты)</div>
            <div class="apidocs-english">APN - attribute of the slip. Authorization Network Type (Card Type)</div>
        iin (Union[None, Unset, str]): <div class="apidocs-russian">IIN - атрибут слипа. Тип карты MasterCard/Visa</div>
            <div class="apidocs-english">IIN - attribute of the slip. Card type masterCard/visa</div>
        sign_needed (Union[None, Unset, bool]): <div class="apidocs-russian">Требуется ли подпись клиента</div>
            <div class="apidocs-english">Is customer signature required</div>
    """

    type_: str
    cashier: Union["NebularApiModelsLkServiceGetReceiptCashier", None, Unset] = UNSET
    date: Union[None, Unset, str] = UNSET
    cashier_id: Union[None, UUID, Unset] = UNSET
    amount: Union[Unset, float] = UNSET
    tsi: Union[None, Unset, str] = UNSET
    rrn: Union[None, Unset, str] = UNSET
    expiration_date: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    customer_contact: Union[None, Unset, str] = UNSET
    calculation_address: Union[None, Unset, str] = UNSET
    error_code: Union[None, Unset, str] = UNSET
    error_message: Union[None, Unset, str] = UNSET
    text: Union[None, Unset, str] = UNSET
    cardholder: Union[None, Unset, str] = UNSET
    acquirer_agent_name: Union[None, Unset, str] = UNSET
    cashless_type: Union[NebularApiEnumsCashlessPaymentsEnum, None, Unset] = UNSET
    qr_pay_transaction: Union["NebularApiModelsCommonApiQrPayTransaction", None, Unset] = UNSET
    merchant_id: Union[None, Unset, str] = UNSET
    currency: Union[None, Unset, int] = UNSET
    resp_code: Union[None, Unset, str] = UNSET
    id: Union[None, UUID, Unset] = UNSET
    acquirer_bank_name: Union[None, Unset, str] = UNSET
    transaction_id: Union[None, Unset, str] = UNSET
    slip_number: Union[None, Unset, str] = UNSET
    approval_code: Union[None, Unset, str] = UNSET
    terminal_id: Union[None, Unset, str] = UNSET
    spasibo: Union["NebularApiModelsCommonApiSpasibo", None, Unset] = UNSET
    mask_pan: Union[None, Unset, str] = UNSET
    aid: Union[None, Unset, str] = UNSET
    tvr: Union[None, Unset, str] = UNSET
    apn: Union[None, Unset, str] = UNSET
    iin: Union[None, Unset, str] = UNSET
    sign_needed: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_qr_pay_transaction import NebularApiModelsCommonApiQrPayTransaction
        from ..models.nebular_api_models_common_api_spasibo import NebularApiModelsCommonApiSpasibo
        from ..models.nebular_api_models_lk_service_get_receipt_cashier import (
            NebularApiModelsLkServiceGetReceiptCashier,
        )

        type_ = self.type_

        cashier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cashier, Unset):
            cashier = UNSET
        elif isinstance(self.cashier, NebularApiModelsLkServiceGetReceiptCashier):
            cashier = self.cashier.to_dict()
        else:
            cashier = self.cashier

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        cashier_id: Union[None, Unset, str]
        if isinstance(self.cashier_id, Unset):
            cashier_id = UNSET
        elif isinstance(self.cashier_id, UUID):
            cashier_id = str(self.cashier_id)
        else:
            cashier_id = self.cashier_id

        amount = self.amount

        tsi: Union[None, Unset, str]
        if isinstance(self.tsi, Unset):
            tsi = UNSET
        else:
            tsi = self.tsi

        rrn: Union[None, Unset, str]
        if isinstance(self.rrn, Unset):
            rrn = UNSET
        else:
            rrn = self.rrn

        expiration_date: Union[None, Unset, str]
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = self.expiration_date

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        customer_contact: Union[None, Unset, str]
        if isinstance(self.customer_contact, Unset):
            customer_contact = UNSET
        else:
            customer_contact = self.customer_contact

        calculation_address: Union[None, Unset, str]
        if isinstance(self.calculation_address, Unset):
            calculation_address = UNSET
        else:
            calculation_address = self.calculation_address

        error_code: Union[None, Unset, str]
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        cardholder: Union[None, Unset, str]
        if isinstance(self.cardholder, Unset):
            cardholder = UNSET
        else:
            cardholder = self.cardholder

        acquirer_agent_name: Union[None, Unset, str]
        if isinstance(self.acquirer_agent_name, Unset):
            acquirer_agent_name = UNSET
        else:
            acquirer_agent_name = self.acquirer_agent_name

        cashless_type: Union[None, Unset, int]
        if isinstance(self.cashless_type, Unset):
            cashless_type = UNSET
        elif isinstance(self.cashless_type, NebularApiEnumsCashlessPaymentsEnum):
            cashless_type = self.cashless_type.value
        else:
            cashless_type = self.cashless_type

        qr_pay_transaction: Union[None, Unset, dict[str, Any]]
        if isinstance(self.qr_pay_transaction, Unset):
            qr_pay_transaction = UNSET
        elif isinstance(self.qr_pay_transaction, NebularApiModelsCommonApiQrPayTransaction):
            qr_pay_transaction = self.qr_pay_transaction.to_dict()
        else:
            qr_pay_transaction = self.qr_pay_transaction

        merchant_id: Union[None, Unset, str]
        if isinstance(self.merchant_id, Unset):
            merchant_id = UNSET
        else:
            merchant_id = self.merchant_id

        currency: Union[None, Unset, int]
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        resp_code: Union[None, Unset, str]
        if isinstance(self.resp_code, Unset):
            resp_code = UNSET
        else:
            resp_code = self.resp_code

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        acquirer_bank_name: Union[None, Unset, str]
        if isinstance(self.acquirer_bank_name, Unset):
            acquirer_bank_name = UNSET
        else:
            acquirer_bank_name = self.acquirer_bank_name

        transaction_id: Union[None, Unset, str]
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = self.transaction_id

        slip_number: Union[None, Unset, str]
        if isinstance(self.slip_number, Unset):
            slip_number = UNSET
        else:
            slip_number = self.slip_number

        approval_code: Union[None, Unset, str]
        if isinstance(self.approval_code, Unset):
            approval_code = UNSET
        else:
            approval_code = self.approval_code

        terminal_id: Union[None, Unset, str]
        if isinstance(self.terminal_id, Unset):
            terminal_id = UNSET
        else:
            terminal_id = self.terminal_id

        spasibo: Union[None, Unset, dict[str, Any]]
        if isinstance(self.spasibo, Unset):
            spasibo = UNSET
        elif isinstance(self.spasibo, NebularApiModelsCommonApiSpasibo):
            spasibo = self.spasibo.to_dict()
        else:
            spasibo = self.spasibo

        mask_pan: Union[None, Unset, str]
        if isinstance(self.mask_pan, Unset):
            mask_pan = UNSET
        else:
            mask_pan = self.mask_pan

        aid: Union[None, Unset, str]
        if isinstance(self.aid, Unset):
            aid = UNSET
        else:
            aid = self.aid

        tvr: Union[None, Unset, str]
        if isinstance(self.tvr, Unset):
            tvr = UNSET
        else:
            tvr = self.tvr

        apn: Union[None, Unset, str]
        if isinstance(self.apn, Unset):
            apn = UNSET
        else:
            apn = self.apn

        iin: Union[None, Unset, str]
        if isinstance(self.iin, Unset):
            iin = UNSET
        else:
            iin = self.iin

        sign_needed: Union[None, Unset, bool]
        if isinstance(self.sign_needed, Unset):
            sign_needed = UNSET
        else:
            sign_needed = self.sign_needed

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "type": type_,
            }
        )
        if cashier is not UNSET:
            field_dict["cashier"] = cashier
        if date is not UNSET:
            field_dict["date"] = date
        if cashier_id is not UNSET:
            field_dict["cashierId"] = cashier_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if tsi is not UNSET:
            field_dict["tsi"] = tsi
        if rrn is not UNSET:
            field_dict["rrn"] = rrn
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if customer_contact is not UNSET:
            field_dict["customerContact"] = customer_contact
        if calculation_address is not UNSET:
            field_dict["calculationAddress"] = calculation_address
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if text is not UNSET:
            field_dict["text"] = text
        if cardholder is not UNSET:
            field_dict["cardholder"] = cardholder
        if acquirer_agent_name is not UNSET:
            field_dict["acquirerAgentName"] = acquirer_agent_name
        if cashless_type is not UNSET:
            field_dict["cashlessType"] = cashless_type
        if qr_pay_transaction is not UNSET:
            field_dict["qrPayTransaction"] = qr_pay_transaction
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if resp_code is not UNSET:
            field_dict["respCode"] = resp_code
        if id is not UNSET:
            field_dict["id"] = id
        if acquirer_bank_name is not UNSET:
            field_dict["acquirerBankName"] = acquirer_bank_name
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if slip_number is not UNSET:
            field_dict["slipNumber"] = slip_number
        if approval_code is not UNSET:
            field_dict["approvalCode"] = approval_code
        if terminal_id is not UNSET:
            field_dict["terminalId"] = terminal_id
        if spasibo is not UNSET:
            field_dict["spasibo"] = spasibo
        if mask_pan is not UNSET:
            field_dict["maskPan"] = mask_pan
        if aid is not UNSET:
            field_dict["aid"] = aid
        if tvr is not UNSET:
            field_dict["tvr"] = tvr
        if apn is not UNSET:
            field_dict["apn"] = apn
        if iin is not UNSET:
            field_dict["iin"] = iin
        if sign_needed is not UNSET:
            field_dict["signNeeded"] = sign_needed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_qr_pay_transaction import NebularApiModelsCommonApiQrPayTransaction
        from ..models.nebular_api_models_common_api_spasibo import NebularApiModelsCommonApiSpasibo
        from ..models.nebular_api_models_lk_service_get_receipt_cashier import (
            NebularApiModelsLkServiceGetReceiptCashier,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_cashier(data: object) -> Union["NebularApiModelsLkServiceGetReceiptCashier", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cashier_type_1 = NebularApiModelsLkServiceGetReceiptCashier.from_dict(data)

                return cashier_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceGetReceiptCashier", None, Unset], data)

        cashier = _parse_cashier(d.pop("cashier", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_cashier_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cashier_id_type_0 = UUID(data)

                return cashier_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cashier_id = _parse_cashier_id(d.pop("cashierId", UNSET))

        amount = d.pop("amount", UNSET)

        def _parse_tsi(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tsi = _parse_tsi(d.pop("tsi", UNSET))

        def _parse_rrn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rrn = _parse_rrn(d.pop("rrn", UNSET))

        def _parse_expiration_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_customer_contact(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer_contact = _parse_customer_contact(d.pop("customerContact", UNSET))

        def _parse_calculation_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        calculation_address = _parse_calculation_address(d.pop("calculationAddress", UNSET))

        def _parse_error_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_cardholder(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cardholder = _parse_cardholder(d.pop("cardholder", UNSET))

        def _parse_acquirer_agent_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acquirer_agent_name = _parse_acquirer_agent_name(d.pop("acquirerAgentName", UNSET))

        def _parse_cashless_type(data: object) -> Union[NebularApiEnumsCashlessPaymentsEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                cashless_type_type_1 = NebularApiEnumsCashlessPaymentsEnum(data)

                return cashless_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsCashlessPaymentsEnum, None, Unset], data)

        cashless_type = _parse_cashless_type(d.pop("cashlessType", UNSET))

        def _parse_qr_pay_transaction(data: object) -> Union["NebularApiModelsCommonApiQrPayTransaction", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qr_pay_transaction_type_1 = NebularApiModelsCommonApiQrPayTransaction.from_dict(data)

                return qr_pay_transaction_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiQrPayTransaction", None, Unset], data)

        qr_pay_transaction = _parse_qr_pay_transaction(d.pop("qrPayTransaction", UNSET))

        def _parse_merchant_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        merchant_id = _parse_merchant_id(d.pop("merchantId", UNSET))

        def _parse_currency(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_resp_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resp_code = _parse_resp_code(d.pop("respCode", UNSET))

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

        def _parse_acquirer_bank_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acquirer_bank_name = _parse_acquirer_bank_name(d.pop("acquirerBankName", UNSET))

        def _parse_transaction_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transaction_id = _parse_transaction_id(d.pop("transactionId", UNSET))

        def _parse_slip_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slip_number = _parse_slip_number(d.pop("slipNumber", UNSET))

        def _parse_approval_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approval_code = _parse_approval_code(d.pop("approvalCode", UNSET))

        def _parse_terminal_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terminal_id = _parse_terminal_id(d.pop("terminalId", UNSET))

        def _parse_spasibo(data: object) -> Union["NebularApiModelsCommonApiSpasibo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spasibo_type_1 = NebularApiModelsCommonApiSpasibo.from_dict(data)

                return spasibo_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiSpasibo", None, Unset], data)

        spasibo = _parse_spasibo(d.pop("spasibo", UNSET))

        def _parse_mask_pan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mask_pan = _parse_mask_pan(d.pop("maskPan", UNSET))

        def _parse_aid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aid = _parse_aid(d.pop("aid", UNSET))

        def _parse_tvr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tvr = _parse_tvr(d.pop("tvr", UNSET))

        def _parse_apn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        apn = _parse_apn(d.pop("apn", UNSET))

        def _parse_iin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        iin = _parse_iin(d.pop("iin", UNSET))

        def _parse_sign_needed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sign_needed = _parse_sign_needed(d.pop("signNeeded", UNSET))

        nebular_api_models_lk_service_lk_slip = cls(
            type_=type_,
            cashier=cashier,
            date=date,
            cashier_id=cashier_id,
            amount=amount,
            tsi=tsi,
            rrn=rrn,
            expiration_date=expiration_date,
            company_name=company_name,
            customer_contact=customer_contact,
            calculation_address=calculation_address,
            error_code=error_code,
            error_message=error_message,
            text=text,
            cardholder=cardholder,
            acquirer_agent_name=acquirer_agent_name,
            cashless_type=cashless_type,
            qr_pay_transaction=qr_pay_transaction,
            merchant_id=merchant_id,
            currency=currency,
            resp_code=resp_code,
            id=id,
            acquirer_bank_name=acquirer_bank_name,
            transaction_id=transaction_id,
            slip_number=slip_number,
            approval_code=approval_code,
            terminal_id=terminal_id,
            spasibo=spasibo,
            mask_pan=mask_pan,
            aid=aid,
            tvr=tvr,
            apn=apn,
            iin=iin,
            sign_needed=sign_needed,
        )

        return nebular_api_models_lk_service_lk_slip
