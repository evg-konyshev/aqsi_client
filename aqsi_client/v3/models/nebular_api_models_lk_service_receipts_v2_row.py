import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.nebular_api_enums_fiscalization_status_enum import NebularApiEnumsFiscalizationStatusEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_cashiers_v2_get_cashier_response_v2 import (
        NebularApiModelsLkServiceCashiersV2GetCashierResponseV2,
    )
    from ..models.nebular_api_models_lk_service_receipts_v2_client_info import (
        NebularApiModelsLkServiceReceiptsV2ClientInfo,
    )
    from ..models.nebular_api_models_lk_service_receipts_v2_loyalty_content import (
        NebularApiModelsLkServiceReceiptsV2LoyaltyContent,
    )
    from ..models.nebular_api_models_receipt_models_receipt_content_v3 import (
        NebularApiModelsReceiptModelsReceiptContentV3,
    )


T = TypeVar("T", bound="NebularApiModelsLkServiceReceiptsV2Row")


@_attrs_define
class NebularApiModelsLkServiceReceiptsV2Row:
    """
    Attributes:
        id (UUID): <div class="apidocs-russian">Номер чека</div>
            <div class="apidocs-english">Receipt number</div>
        content (NebularApiModelsReceiptModelsReceiptContentV3): <div class="apidocs-russian">Содержимое чека версии
            3</div>
            <div class="apidocs-english">Receipt content</div>
        amount (float): <div class="apidocs-russian">Сумма чека</div>
            <div class="apidocs-english">Receipt amount</div>
        operation_mode (int): <div class="apidocs-russian">Операционный режим, в котором был пробит чек. Битовая маска,
            по умолчанию 0.</div>
            <div class="apidocs-english">The operating mode in which the check was processed. Bitmask, default 0.</div>
        cashier (Union['NebularApiModelsLkServiceCashiersV2GetCashierResponseV2', None, Unset]): <div class="apidocs-
            russian">Модель кассира для отображения в чеке</div>
            <div class="apidocs-english">Cashier model for presentation in receipt</div> Example: {'id': '1k23o3kk', 'name':
            'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'lastLoginTime': None, 'code': '34', 'img': None,
            'customProperties': [{'key': 'StaffId', 'value': 'YYY'}], 'pin': '0000', 'devices': None}.
        calculation_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес установки ККТ для проведения
            расчетов</div>
            <div class="apidocs-english">Cash register installation address</div>
        calculation_place (Union[None, Unset, str]): <div class="apidocs-russian">Место проведения расчетов</div>
            <div class="apidocs-english">Calculation place</div>
        cashier_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор кассира</div>
            <div class="apidocs-english">Cashier identifier</div>
        change (Union[Unset, float]): <div class="apidocs-russian">Сдача</div>
            <div class="apidocs-english">Change</div>
        device_rn (Union[None, Unset, str]): <div class="apidocs-russian">Регистрационный номер устройства</div>
            <div class="apidocs-english">Device registration number</div>
        device_sn (Union[None, Unset, str]): <div class="apidocs-russian">Серийник устройства</div>
            <div class="apidocs-english">Device serial number</div>
        aqsi_serial_number (Union[None, Unset, str]): <div class="apidocs-russian">Серийник устройства aQsi</div>
            <div class="apidocs-english">aQsi device serial number</div>
        fns_website (Union[None, Unset, str]): <div class="apidocs-russian">Сайт ФНС</div>
            <div class="apidocs-english">The Federal Tax Service website</div>
        fp (Union[None, Unset, str]): <div class="apidocs-russian">Фискальный признак</div>
            <div class="apidocs-english">Fiscal property</div>
        fs_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер ФН</div>
            <div class="apidocs-english">Fiscal storage number</div>
        ofd_inn (Union[None, Unset, str]): <div class="apidocs-russian">ИНН ОФД</div>
            <div class="apidocs-english">Fiscal data operator TIN</div>
        ofd_name (Union[None, Unset, str]): <div class="apidocs-russian">Имя ОФД</div>
            <div class="apidocs-english">Fiscal data operator name</div>
        ofd_website (Union[None, Unset, str]): <div class="apidocs-russian">Сайт ОФД</div>
            <div class="apidocs-english">Fiscal data operator site</div>
        operation_number (Union[None, Unset, int]): <div class="apidocs-russian">Сквозной номер документа</div>
            <div class="apidocs-english">Global operation number</div>
        order_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор заказа, для которого пробит
            чек</div>
            <div class="apidocs-english">ID of the order for which the check has been processed</div>
        processed_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Время обработки кассой</div>
            <div class="apidocs-english">Cashbox processing time</div>
        fiscalized_at (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Время фискализации в
            ОД</div>
            <div class="apidocs-english">OrangeData fiscalized date</div>
        shift_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер смены кассира</div>
            <div class="apidocs-english">Cashier shift number</div>
        loyalty_content (Union['NebularApiModelsLkServiceReceiptsV2LoyaltyContent', None, Unset]): <div class="apidocs-
            russian">Дополнительные поля агрегации для лояльности</div>
            <div class="apidocs-english">Additional aggregation fields for loyalty</div>
        client_info (Union['NebularApiModelsLkServiceReceiptsV2ClientInfo', None, Unset]): <div class="apidocs-
            russian">Информация о клиенте</div>
            <div class="apidocs-english">Client info</div>
        return_check_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор чека, для которого
            выполняется возврат</div>
            <div class="apidocs-english">Receipt identifier for which the refund</div>
        document_index (Union[None, Unset, int]): <div class="apidocs-russian">Номер чека за смену</div>
            <div class="apidocs-english">Shift receipt number</div>
        document_number (Union[None, Unset, int]): <div class="apidocs-russian">Номер фискального документа</div>
            <div class="apidocs-english">Fiscal document number</div>
        company_inn (Union[None, Unset, str]): <div class="apidocs-russian">ИНН торговой точки по фискализации</div>
            <div class="apidocs-english">TIN of a fiscalization outlet</div>
        company_name (Union[None, Unset, str]): <div class="apidocs-russian">Название организации</div>
            <div class="apidocs-english">Company name</div>
        fiscalization_status (Union[NebularApiEnumsFiscalizationStatusEnum, None, Unset]): <div class="apidocs-
            russian">Статус фискализации чека</div>
            <div class="apidocs-english">Fiscalization status</div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">0</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">В очереди</div><div class="apidocs-english">Queue</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">1</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Отправлен</div><div class="apidocs-english">Sent</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">2</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Фискализирован</div><div class="apidocs-
            english">Fiscalized</div></div>
            <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">3</div><div style="margin: 0
            0.25em;">-</div><div class="apidocs-russian">Ошибка</div><div class="apidocs-english">Error</div></div>
        fiscalization_error (Union[None, Unset, str]): <div class="apidocs-russian">Описание ошибки для статуса
            фискализации</div>
            <div class="apidocs-english">Error description for fiscalization status</div>
        automaton_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор автомата</div>
            <div class="apidocs-english">Automat identifier</div>
        shift_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор смены</div>
            <div class="apidocs-english">Shift identifier</div>
        is_non_fiscal (Union[Unset, bool]): <div class="apidocs-russian">Признак, указывающий на то, что данный чек был
            пробит из нефискального режима</div>
            <div class="apidocs-english">A sign indicating that this check was processed out of non-fiscal mode</div>
    """

    id: UUID
    content: "NebularApiModelsReceiptModelsReceiptContentV3"
    amount: float
    operation_mode: int
    cashier: Union["NebularApiModelsLkServiceCashiersV2GetCashierResponseV2", None, Unset] = UNSET
    calculation_address: Union[None, Unset, str] = UNSET
    calculation_place: Union[None, Unset, str] = UNSET
    cashier_id: Union[None, Unset, str] = UNSET
    change: Union[Unset, float] = UNSET
    device_rn: Union[None, Unset, str] = UNSET
    device_sn: Union[None, Unset, str] = UNSET
    aqsi_serial_number: Union[None, Unset, str] = UNSET
    fns_website: Union[None, Unset, str] = UNSET
    fp: Union[None, Unset, str] = UNSET
    fs_number: Union[None, Unset, str] = UNSET
    ofd_inn: Union[None, Unset, str] = UNSET
    ofd_name: Union[None, Unset, str] = UNSET
    ofd_website: Union[None, Unset, str] = UNSET
    operation_number: Union[None, Unset, int] = UNSET
    order_id: Union[None, Unset, str] = UNSET
    processed_at: Union[Unset, datetime.datetime] = UNSET
    fiscalized_at: Union[None, Unset, datetime.datetime] = UNSET
    shift_number: Union[None, Unset, str] = UNSET
    loyalty_content: Union["NebularApiModelsLkServiceReceiptsV2LoyaltyContent", None, Unset] = UNSET
    client_info: Union["NebularApiModelsLkServiceReceiptsV2ClientInfo", None, Unset] = UNSET
    return_check_id: Union[None, UUID, Unset] = UNSET
    document_index: Union[None, Unset, int] = UNSET
    document_number: Union[None, Unset, int] = UNSET
    company_inn: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    fiscalization_status: Union[NebularApiEnumsFiscalizationStatusEnum, None, Unset] = UNSET
    fiscalization_error: Union[None, Unset, str] = UNSET
    automaton_id: Union[None, UUID, Unset] = UNSET
    shift_id: Union[None, UUID, Unset] = UNSET
    is_non_fiscal: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_lk_service_cashiers_v2_get_cashier_response_v2 import (
            NebularApiModelsLkServiceCashiersV2GetCashierResponseV2,
        )
        from ..models.nebular_api_models_lk_service_receipts_v2_client_info import (
            NebularApiModelsLkServiceReceiptsV2ClientInfo,
        )
        from ..models.nebular_api_models_lk_service_receipts_v2_loyalty_content import (
            NebularApiModelsLkServiceReceiptsV2LoyaltyContent,
        )

        id = str(self.id)

        content = self.content.to_dict()

        amount = self.amount

        operation_mode = self.operation_mode

        cashier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cashier, Unset):
            cashier = UNSET
        elif isinstance(self.cashier, NebularApiModelsLkServiceCashiersV2GetCashierResponseV2):
            cashier = self.cashier.to_dict()
        else:
            cashier = self.cashier

        calculation_address: Union[None, Unset, str]
        if isinstance(self.calculation_address, Unset):
            calculation_address = UNSET
        else:
            calculation_address = self.calculation_address

        calculation_place: Union[None, Unset, str]
        if isinstance(self.calculation_place, Unset):
            calculation_place = UNSET
        else:
            calculation_place = self.calculation_place

        cashier_id: Union[None, Unset, str]
        if isinstance(self.cashier_id, Unset):
            cashier_id = UNSET
        else:
            cashier_id = self.cashier_id

        change = self.change

        device_rn: Union[None, Unset, str]
        if isinstance(self.device_rn, Unset):
            device_rn = UNSET
        else:
            device_rn = self.device_rn

        device_sn: Union[None, Unset, str]
        if isinstance(self.device_sn, Unset):
            device_sn = UNSET
        else:
            device_sn = self.device_sn

        aqsi_serial_number: Union[None, Unset, str]
        if isinstance(self.aqsi_serial_number, Unset):
            aqsi_serial_number = UNSET
        else:
            aqsi_serial_number = self.aqsi_serial_number

        fns_website: Union[None, Unset, str]
        if isinstance(self.fns_website, Unset):
            fns_website = UNSET
        else:
            fns_website = self.fns_website

        fp: Union[None, Unset, str]
        if isinstance(self.fp, Unset):
            fp = UNSET
        else:
            fp = self.fp

        fs_number: Union[None, Unset, str]
        if isinstance(self.fs_number, Unset):
            fs_number = UNSET
        else:
            fs_number = self.fs_number

        ofd_inn: Union[None, Unset, str]
        if isinstance(self.ofd_inn, Unset):
            ofd_inn = UNSET
        else:
            ofd_inn = self.ofd_inn

        ofd_name: Union[None, Unset, str]
        if isinstance(self.ofd_name, Unset):
            ofd_name = UNSET
        else:
            ofd_name = self.ofd_name

        ofd_website: Union[None, Unset, str]
        if isinstance(self.ofd_website, Unset):
            ofd_website = UNSET
        else:
            ofd_website = self.ofd_website

        operation_number: Union[None, Unset, int]
        if isinstance(self.operation_number, Unset):
            operation_number = UNSET
        else:
            operation_number = self.operation_number

        order_id: Union[None, Unset, str]
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        fiscalized_at: Union[None, Unset, str]
        if isinstance(self.fiscalized_at, Unset):
            fiscalized_at = UNSET
        elif isinstance(self.fiscalized_at, datetime.datetime):
            fiscalized_at = self.fiscalized_at.isoformat()
        else:
            fiscalized_at = self.fiscalized_at

        shift_number: Union[None, Unset, str]
        if isinstance(self.shift_number, Unset):
            shift_number = UNSET
        else:
            shift_number = self.shift_number

        loyalty_content: Union[None, Unset, dict[str, Any]]
        if isinstance(self.loyalty_content, Unset):
            loyalty_content = UNSET
        elif isinstance(self.loyalty_content, NebularApiModelsLkServiceReceiptsV2LoyaltyContent):
            loyalty_content = self.loyalty_content.to_dict()
        else:
            loyalty_content = self.loyalty_content

        client_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.client_info, Unset):
            client_info = UNSET
        elif isinstance(self.client_info, NebularApiModelsLkServiceReceiptsV2ClientInfo):
            client_info = self.client_info.to_dict()
        else:
            client_info = self.client_info

        return_check_id: Union[None, Unset, str]
        if isinstance(self.return_check_id, Unset):
            return_check_id = UNSET
        elif isinstance(self.return_check_id, UUID):
            return_check_id = str(self.return_check_id)
        else:
            return_check_id = self.return_check_id

        document_index: Union[None, Unset, int]
        if isinstance(self.document_index, Unset):
            document_index = UNSET
        else:
            document_index = self.document_index

        document_number: Union[None, Unset, int]
        if isinstance(self.document_number, Unset):
            document_number = UNSET
        else:
            document_number = self.document_number

        company_inn: Union[None, Unset, str]
        if isinstance(self.company_inn, Unset):
            company_inn = UNSET
        else:
            company_inn = self.company_inn

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        fiscalization_status: Union[None, Unset, int]
        if isinstance(self.fiscalization_status, Unset):
            fiscalization_status = UNSET
        elif isinstance(self.fiscalization_status, NebularApiEnumsFiscalizationStatusEnum):
            fiscalization_status = self.fiscalization_status.value
        else:
            fiscalization_status = self.fiscalization_status

        fiscalization_error: Union[None, Unset, str]
        if isinstance(self.fiscalization_error, Unset):
            fiscalization_error = UNSET
        else:
            fiscalization_error = self.fiscalization_error

        automaton_id: Union[None, Unset, str]
        if isinstance(self.automaton_id, Unset):
            automaton_id = UNSET
        elif isinstance(self.automaton_id, UUID):
            automaton_id = str(self.automaton_id)
        else:
            automaton_id = self.automaton_id

        shift_id: Union[None, Unset, str]
        if isinstance(self.shift_id, Unset):
            shift_id = UNSET
        elif isinstance(self.shift_id, UUID):
            shift_id = str(self.shift_id)
        else:
            shift_id = self.shift_id

        is_non_fiscal = self.is_non_fiscal

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "content": content,
                "amount": amount,
                "operationMode": operation_mode,
            }
        )
        if cashier is not UNSET:
            field_dict["cashier"] = cashier
        if calculation_address is not UNSET:
            field_dict["calculationAddress"] = calculation_address
        if calculation_place is not UNSET:
            field_dict["calculationPlace"] = calculation_place
        if cashier_id is not UNSET:
            field_dict["cashierId"] = cashier_id
        if change is not UNSET:
            field_dict["change"] = change
        if device_rn is not UNSET:
            field_dict["deviceRN"] = device_rn
        if device_sn is not UNSET:
            field_dict["deviceSN"] = device_sn
        if aqsi_serial_number is not UNSET:
            field_dict["aqsiSerialNumber"] = aqsi_serial_number
        if fns_website is not UNSET:
            field_dict["fnsWebsite"] = fns_website
        if fp is not UNSET:
            field_dict["fp"] = fp
        if fs_number is not UNSET:
            field_dict["fsNumber"] = fs_number
        if ofd_inn is not UNSET:
            field_dict["ofdInn"] = ofd_inn
        if ofd_name is not UNSET:
            field_dict["ofdName"] = ofd_name
        if ofd_website is not UNSET:
            field_dict["ofdWebsite"] = ofd_website
        if operation_number is not UNSET:
            field_dict["operationNumber"] = operation_number
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if fiscalized_at is not UNSET:
            field_dict["fiscalizedAt"] = fiscalized_at
        if shift_number is not UNSET:
            field_dict["shiftNumber"] = shift_number
        if loyalty_content is not UNSET:
            field_dict["loyaltyContent"] = loyalty_content
        if client_info is not UNSET:
            field_dict["clientInfo"] = client_info
        if return_check_id is not UNSET:
            field_dict["returnCheckId"] = return_check_id
        if document_index is not UNSET:
            field_dict["documentIndex"] = document_index
        if document_number is not UNSET:
            field_dict["documentNumber"] = document_number
        if company_inn is not UNSET:
            field_dict["companyINN"] = company_inn
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if fiscalization_status is not UNSET:
            field_dict["fiscalizationStatus"] = fiscalization_status
        if fiscalization_error is not UNSET:
            field_dict["fiscalizationError"] = fiscalization_error
        if automaton_id is not UNSET:
            field_dict["automatonId"] = automaton_id
        if shift_id is not UNSET:
            field_dict["shiftId"] = shift_id
        if is_non_fiscal is not UNSET:
            field_dict["isNonFiscal"] = is_non_fiscal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_cashiers_v2_get_cashier_response_v2 import (
            NebularApiModelsLkServiceCashiersV2GetCashierResponseV2,
        )
        from ..models.nebular_api_models_lk_service_receipts_v2_client_info import (
            NebularApiModelsLkServiceReceiptsV2ClientInfo,
        )
        from ..models.nebular_api_models_lk_service_receipts_v2_loyalty_content import (
            NebularApiModelsLkServiceReceiptsV2LoyaltyContent,
        )
        from ..models.nebular_api_models_receipt_models_receipt_content_v3 import (
            NebularApiModelsReceiptModelsReceiptContentV3,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        content = NebularApiModelsReceiptModelsReceiptContentV3.from_dict(d.pop("content"))

        amount = d.pop("amount")

        operation_mode = d.pop("operationMode")

        def _parse_cashier(
            data: object,
        ) -> Union["NebularApiModelsLkServiceCashiersV2GetCashierResponseV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cashier_type_1 = NebularApiModelsLkServiceCashiersV2GetCashierResponseV2.from_dict(data)

                return cashier_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceCashiersV2GetCashierResponseV2", None, Unset], data)

        cashier = _parse_cashier(d.pop("cashier", UNSET))

        def _parse_calculation_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        calculation_address = _parse_calculation_address(d.pop("calculationAddress", UNSET))

        def _parse_calculation_place(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        calculation_place = _parse_calculation_place(d.pop("calculationPlace", UNSET))

        def _parse_cashier_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cashier_id = _parse_cashier_id(d.pop("cashierId", UNSET))

        change = d.pop("change", UNSET)

        def _parse_device_rn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_rn = _parse_device_rn(d.pop("deviceRN", UNSET))

        def _parse_device_sn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_sn = _parse_device_sn(d.pop("deviceSN", UNSET))

        def _parse_aqsi_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aqsi_serial_number = _parse_aqsi_serial_number(d.pop("aqsiSerialNumber", UNSET))

        def _parse_fns_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fns_website = _parse_fns_website(d.pop("fnsWebsite", UNSET))

        def _parse_fp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fp = _parse_fp(d.pop("fp", UNSET))

        def _parse_fs_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fs_number = _parse_fs_number(d.pop("fsNumber", UNSET))

        def _parse_ofd_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ofd_inn = _parse_ofd_inn(d.pop("ofdInn", UNSET))

        def _parse_ofd_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ofd_name = _parse_ofd_name(d.pop("ofdName", UNSET))

        def _parse_ofd_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ofd_website = _parse_ofd_website(d.pop("ofdWebsite", UNSET))

        def _parse_operation_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        operation_number = _parse_operation_number(d.pop("operationNumber", UNSET))

        def _parse_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_id = _parse_order_id(d.pop("orderId", UNSET))

        _processed_at = d.pop("processedAt", UNSET)
        processed_at: Union[Unset, datetime.datetime]
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        def _parse_fiscalized_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fiscalized_at_type_0 = isoparse(data)

                return fiscalized_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        fiscalized_at = _parse_fiscalized_at(d.pop("fiscalizedAt", UNSET))

        def _parse_shift_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shift_number = _parse_shift_number(d.pop("shiftNumber", UNSET))

        def _parse_loyalty_content(
            data: object,
        ) -> Union["NebularApiModelsLkServiceReceiptsV2LoyaltyContent", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loyalty_content_type_1 = NebularApiModelsLkServiceReceiptsV2LoyaltyContent.from_dict(data)

                return loyalty_content_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceReceiptsV2LoyaltyContent", None, Unset], data)

        loyalty_content = _parse_loyalty_content(d.pop("loyaltyContent", UNSET))

        def _parse_client_info(data: object) -> Union["NebularApiModelsLkServiceReceiptsV2ClientInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_info_type_1 = NebularApiModelsLkServiceReceiptsV2ClientInfo.from_dict(data)

                return client_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsLkServiceReceiptsV2ClientInfo", None, Unset], data)

        client_info = _parse_client_info(d.pop("clientInfo", UNSET))

        def _parse_return_check_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                return_check_id_type_0 = UUID(data)

                return return_check_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        return_check_id = _parse_return_check_id(d.pop("returnCheckId", UNSET))

        def _parse_document_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_index = _parse_document_index(d.pop("documentIndex", UNSET))

        def _parse_document_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_number = _parse_document_number(d.pop("documentNumber", UNSET))

        def _parse_company_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_inn = _parse_company_inn(d.pop("companyINN", UNSET))

        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_fiscalization_status(data: object) -> Union[NebularApiEnumsFiscalizationStatusEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                fiscalization_status_type_1 = NebularApiEnumsFiscalizationStatusEnum(data)

                return fiscalization_status_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsFiscalizationStatusEnum, None, Unset], data)

        fiscalization_status = _parse_fiscalization_status(d.pop("fiscalizationStatus", UNSET))

        def _parse_fiscalization_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fiscalization_error = _parse_fiscalization_error(d.pop("fiscalizationError", UNSET))

        def _parse_automaton_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                automaton_id_type_0 = UUID(data)

                return automaton_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        automaton_id = _parse_automaton_id(d.pop("automatonId", UNSET))

        def _parse_shift_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shift_id_type_0 = UUID(data)

                return shift_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        shift_id = _parse_shift_id(d.pop("shiftId", UNSET))

        is_non_fiscal = d.pop("isNonFiscal", UNSET)

        nebular_api_models_lk_service_receipts_v2_row = cls(
            id=id,
            content=content,
            amount=amount,
            operation_mode=operation_mode,
            cashier=cashier,
            calculation_address=calculation_address,
            calculation_place=calculation_place,
            cashier_id=cashier_id,
            change=change,
            device_rn=device_rn,
            device_sn=device_sn,
            aqsi_serial_number=aqsi_serial_number,
            fns_website=fns_website,
            fp=fp,
            fs_number=fs_number,
            ofd_inn=ofd_inn,
            ofd_name=ofd_name,
            ofd_website=ofd_website,
            operation_number=operation_number,
            order_id=order_id,
            processed_at=processed_at,
            fiscalized_at=fiscalized_at,
            shift_number=shift_number,
            loyalty_content=loyalty_content,
            client_info=client_info,
            return_check_id=return_check_id,
            document_index=document_index,
            document_number=document_number,
            company_inn=company_inn,
            company_name=company_name,
            fiscalization_status=fiscalization_status,
            fiscalization_error=fiscalization_error,
            automaton_id=automaton_id,
            shift_id=shift_id,
            is_non_fiscal=is_non_fiscal,
        )

        return nebular_api_models_lk_service_receipts_v2_row
