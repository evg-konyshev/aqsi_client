from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiReconciliations")


@_attrs_define
class NebularApiModelsCommonApiReconciliations:
    """
    Attributes:
        slip (Union[None, Unset, str]): <div class="apidocs-russian">Текст слипа сверки итогов</div>
            <div class="apidocs-english">Slip text</div>
        error_code (Union[Unset, int]): <div class="apidocs-russian">Код ошибки сверки итогов</div>
            <div class="apidocs-english">Error code</div>
        error_message (Union[None, Unset, str]): <div class="apidocs-russian">Сообщение об ошибке при сверке
            итогов</div>
            <div class="apidocs-english">Error message</div>
        response_code (Union[None, Unset, str]): <div class="apidocs-russian">Код ответа</div>
            <div class="apidocs-english">Response code</div>
        approval_number (Union[None, Unset, str]): <div class="apidocs-russian">Код авторизации</div>
            <div class="apidocs-english">Approval code</div>
        rrn (Union[None, Unset, str]): <div class="apidocs-russian">Retrieval Reference Number</div>
            <div class="apidocs-english">Retrieval Reference Number</div>
        original_amount (Union[None, Unset, str]): <div class="apidocs-russian">Итоговая сумма, подсчитанная на
            терминале</div>
            <div class="apidocs-english">Terminal total sum</div>
        amount (Union[None, Unset, str]): <div class="apidocs-russian">Итоговая сумма, переданная сервером
            авторизации</div>
            <div class="apidocs-english">Total sum</div>
        date_time (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время проведения сверки итогов</div>
            <div class="apidocs-english">Date and time of reconciliation</div>
        tid (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор (номер) терминала</div>
            <div class="apidocs-english">Terminal ID</div>
        mid (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор владельца терминала</div>
            <div class="apidocs-english">Merchant ID</div>
        currency (Union[Unset, int]): <div class="apidocs-russian">Код валюты</div>
            <div class="apidocs-english">Currency code</div>
        from_ (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время первой транзакции в сверке</div>
            <div class="apidocs-english">Date and time of the first transaction in the reconciliation</div>
        to (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время последней транзакции в сверке</div>
            <div class="apidocs-english">Date and time of the last transaction in the reconciliation</div>
        num (Union[Unset, int]): <div class="apidocs-russian">Количество транзакций в сверке</div>
            <div class="apidocs-english">Count of transaction in the reconciliation</div>
        batch_upload (Union[None, Unset, str]): <div class="apidocs-russian">В случае если суммы при сверке не совпали,
            требуется загрузка транзакций</div>
            <div class="apidocs-english">Batch upload</div>
        art_response_code (Union[None, Unset, str]): <div class="apidocs-russian">Код ответа на запрос, завершающий
            загрузку транзакций</div>
            <div class="apidocs-english">Response code to the request that completes the download of transactions</div>
        cov_response_code (Union[None, Unset, str]): <div class="apidocs-russian">Код возврата операции очистки
            журнала</div>
            <div class="apidocs-english">The return code of the log cleanup operation</div>
        cov_rrn (Union[None, Unset, str]): <div class="apidocs-russian">RRN операции очистки журнала</div>
            <div class="apidocs-english">RRN log cleanup operations</div>
        settlement_result (Union[None, Unset, str]): <div class="apidocs-russian">Результат операции сверки итогов</div>
            <div class="apidocs-english">Result of reconciliation operation</div>
    """

    slip: Union[None, Unset, str] = UNSET
    error_code: Union[Unset, int] = UNSET
    error_message: Union[None, Unset, str] = UNSET
    response_code: Union[None, Unset, str] = UNSET
    approval_number: Union[None, Unset, str] = UNSET
    rrn: Union[None, Unset, str] = UNSET
    original_amount: Union[None, Unset, str] = UNSET
    amount: Union[None, Unset, str] = UNSET
    date_time: Union[None, Unset, str] = UNSET
    tid: Union[None, Unset, str] = UNSET
    mid: Union[None, Unset, str] = UNSET
    currency: Union[Unset, int] = UNSET
    from_: Union[None, Unset, str] = UNSET
    to: Union[None, Unset, str] = UNSET
    num: Union[Unset, int] = UNSET
    batch_upload: Union[None, Unset, str] = UNSET
    art_response_code: Union[None, Unset, str] = UNSET
    cov_response_code: Union[None, Unset, str] = UNSET
    cov_rrn: Union[None, Unset, str] = UNSET
    settlement_result: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        slip: Union[None, Unset, str]
        if isinstance(self.slip, Unset):
            slip = UNSET
        else:
            slip = self.slip

        error_code = self.error_code

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        response_code: Union[None, Unset, str]
        if isinstance(self.response_code, Unset):
            response_code = UNSET
        else:
            response_code = self.response_code

        approval_number: Union[None, Unset, str]
        if isinstance(self.approval_number, Unset):
            approval_number = UNSET
        else:
            approval_number = self.approval_number

        rrn: Union[None, Unset, str]
        if isinstance(self.rrn, Unset):
            rrn = UNSET
        else:
            rrn = self.rrn

        original_amount: Union[None, Unset, str]
        if isinstance(self.original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = self.original_amount

        amount: Union[None, Unset, str]
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        date_time: Union[None, Unset, str]
        if isinstance(self.date_time, Unset):
            date_time = UNSET
        else:
            date_time = self.date_time

        tid: Union[None, Unset, str]
        if isinstance(self.tid, Unset):
            tid = UNSET
        else:
            tid = self.tid

        mid: Union[None, Unset, str]
        if isinstance(self.mid, Unset):
            mid = UNSET
        else:
            mid = self.mid

        currency = self.currency

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        num = self.num

        batch_upload: Union[None, Unset, str]
        if isinstance(self.batch_upload, Unset):
            batch_upload = UNSET
        else:
            batch_upload = self.batch_upload

        art_response_code: Union[None, Unset, str]
        if isinstance(self.art_response_code, Unset):
            art_response_code = UNSET
        else:
            art_response_code = self.art_response_code

        cov_response_code: Union[None, Unset, str]
        if isinstance(self.cov_response_code, Unset):
            cov_response_code = UNSET
        else:
            cov_response_code = self.cov_response_code

        cov_rrn: Union[None, Unset, str]
        if isinstance(self.cov_rrn, Unset):
            cov_rrn = UNSET
        else:
            cov_rrn = self.cov_rrn

        settlement_result: Union[None, Unset, str]
        if isinstance(self.settlement_result, Unset):
            settlement_result = UNSET
        else:
            settlement_result = self.settlement_result

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if slip is not UNSET:
            field_dict["slip"] = slip
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if response_code is not UNSET:
            field_dict["responseCode"] = response_code
        if approval_number is not UNSET:
            field_dict["approvalNumber"] = approval_number
        if rrn is not UNSET:
            field_dict["rrn"] = rrn
        if original_amount is not UNSET:
            field_dict["originalAmount"] = original_amount
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if tid is not UNSET:
            field_dict["tid"] = tid
        if mid is not UNSET:
            field_dict["mid"] = mid
        if currency is not UNSET:
            field_dict["currency"] = currency
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if num is not UNSET:
            field_dict["num"] = num
        if batch_upload is not UNSET:
            field_dict["batchUpload"] = batch_upload
        if art_response_code is not UNSET:
            field_dict["artResponseCode"] = art_response_code
        if cov_response_code is not UNSET:
            field_dict["covResponseCode"] = cov_response_code
        if cov_rrn is not UNSET:
            field_dict["covRrn"] = cov_rrn
        if settlement_result is not UNSET:
            field_dict["settlementResult"] = settlement_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_slip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slip = _parse_slip(d.pop("slip", UNSET))

        error_code = d.pop("errorCode", UNSET)

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_response_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        response_code = _parse_response_code(d.pop("responseCode", UNSET))

        def _parse_approval_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approval_number = _parse_approval_number(d.pop("approvalNumber", UNSET))

        def _parse_rrn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rrn = _parse_rrn(d.pop("rrn", UNSET))

        def _parse_original_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_amount = _parse_original_amount(d.pop("originalAmount", UNSET))

        def _parse_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_date_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_time = _parse_date_time(d.pop("dateTime", UNSET))

        def _parse_tid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tid = _parse_tid(d.pop("tid", UNSET))

        def _parse_mid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mid = _parse_mid(d.pop("mid", UNSET))

        currency = d.pop("currency", UNSET)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        num = d.pop("num", UNSET)

        def _parse_batch_upload(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        batch_upload = _parse_batch_upload(d.pop("batchUpload", UNSET))

        def _parse_art_response_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        art_response_code = _parse_art_response_code(d.pop("artResponseCode", UNSET))

        def _parse_cov_response_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cov_response_code = _parse_cov_response_code(d.pop("covResponseCode", UNSET))

        def _parse_cov_rrn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cov_rrn = _parse_cov_rrn(d.pop("covRrn", UNSET))

        def _parse_settlement_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        settlement_result = _parse_settlement_result(d.pop("settlementResult", UNSET))

        nebular_api_models_common_api_reconciliations = cls(
            slip=slip,
            error_code=error_code,
            error_message=error_message,
            response_code=response_code,
            approval_number=approval_number,
            rrn=rrn,
            original_amount=original_amount,
            amount=amount,
            date_time=date_time,
            tid=tid,
            mid=mid,
            currency=currency,
            from_=from_,
            to=to,
            num=num,
            batch_upload=batch_upload,
            art_response_code=art_response_code,
            cov_response_code=cov_response_code,
            cov_rrn=cov_rrn,
            settlement_result=settlement_result,
        )

        return nebular_api_models_common_api_reconciliations
