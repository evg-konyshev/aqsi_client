import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_reconciliations import NebularApiModelsCommonApiReconciliations
    from ..models.nebular_api_models_common_api_с_ounters import NebularApiModelsCommonApiСOunters


T = TypeVar("T", bound="NebularApiModelsLkServiceLkShift")


@_attrs_define
class NebularApiModelsLkServiceLkShift:
    """<div class="apidocs-russian">Смена</div>
    <div class="apidocs-english">Shift</div>

        Attributes:
            id (Union[None, UUID, Unset]): <div class="apidocs-russian">Uuid смены</div>
                <div class="apidocs-english">shift uuid</div>
            number (Union[None, Unset, int]): <div class="apidocs-russian">Номер смены</div>
                <div class="apidocs-english">Shift number</div>
            start_date (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Дата начала смены</div>
                <div class="apidocs-english">Shift start date</div>
            cash_at_start (Union[None, Unset, str]): <div class="apidocs-russian">Сумма на начало смены</div>
                <div class="apidocs-english">Shift start sum</div>
            date_close (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Дата завершения смены</div>
                <div class="apidocs-english">Shift end date</div>
            cash_at_end (Union[None, Unset, str]): <div class="apidocs-russian">Сумма в кассе на конец смены</div>
                <div class="apidocs-english">Shift end sum</div>
            device_sn (Union[None, Unset, str]): <div class="apidocs-russian">Серийный номер кассы</div>
                <div class="apidocs-english">Device serial number</div>
            fs_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер ФН</div>
                <div class="apidocs-english">FS number</div>
            cashier_open (Union[None, UUID, Unset]): <div class="apidocs-russian">Кассир, открывший смену</div>
                <div class="apidocs-english">Open cashier</div>
            cashier_close (Union[None, UUID, Unset]): <div class="apidocs-russian">Кассир, закрывший смену</div>
                <div class="apidocs-english">Close cashier</div>
            device_rn (Union[None, Unset, str]): <div class="apidocs-russian">Регистрационный номер ККТ</div>
                <div class="apidocs-english">Device RN number</div>
            counters (Union['NebularApiModelsCommonApiСOunters', None, Unset]): <div class="apidocs-russian">Счётчики
                кассы</div>
                <div class="apidocs-english">Cash counters</div>
            updated_at (Union[None, Unset, str]): <div class="apidocs-russian">Метка времени обновления</div>
                <div class="apidocs-english">Update date mark</div>
            reconciliations (Union[None, Unset, list['NebularApiModelsCommonApiReconciliations']]): <div class="apidocs-
                russian">Список сверок итогов</div>
                <div class="apidocs-english">List of reconciliations</div>
            external_user_id (Union[None, Unset, str]): <div class="apidocs-russian">Внешний идентификатор
                пользователя</div>
                <div class="apidocs-english">External user id</div>
            position (Union[None, Unset, str]): <div class="apidocs-russian">Должность кассира</div>
                <div class="apidocs-english">Cashier position</div>
    """

    id: Union[None, UUID, Unset] = UNSET
    number: Union[None, Unset, int] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    cash_at_start: Union[None, Unset, str] = UNSET
    date_close: Union[None, Unset, datetime.datetime] = UNSET
    cash_at_end: Union[None, Unset, str] = UNSET
    device_sn: Union[None, Unset, str] = UNSET
    fs_number: Union[None, Unset, str] = UNSET
    cashier_open: Union[None, UUID, Unset] = UNSET
    cashier_close: Union[None, UUID, Unset] = UNSET
    device_rn: Union[None, Unset, str] = UNSET
    counters: Union["NebularApiModelsCommonApiСOunters", None, Unset] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    reconciliations: Union[None, Unset, list["NebularApiModelsCommonApiReconciliations"]] = UNSET
    external_user_id: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_с_ounters import NebularApiModelsCommonApiСOunters

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        cash_at_start: Union[None, Unset, str]
        if isinstance(self.cash_at_start, Unset):
            cash_at_start = UNSET
        else:
            cash_at_start = self.cash_at_start

        date_close: Union[None, Unset, str]
        if isinstance(self.date_close, Unset):
            date_close = UNSET
        elif isinstance(self.date_close, datetime.datetime):
            date_close = self.date_close.isoformat()
        else:
            date_close = self.date_close

        cash_at_end: Union[None, Unset, str]
        if isinstance(self.cash_at_end, Unset):
            cash_at_end = UNSET
        else:
            cash_at_end = self.cash_at_end

        device_sn: Union[None, Unset, str]
        if isinstance(self.device_sn, Unset):
            device_sn = UNSET
        else:
            device_sn = self.device_sn

        fs_number: Union[None, Unset, str]
        if isinstance(self.fs_number, Unset):
            fs_number = UNSET
        else:
            fs_number = self.fs_number

        cashier_open: Union[None, Unset, str]
        if isinstance(self.cashier_open, Unset):
            cashier_open = UNSET
        elif isinstance(self.cashier_open, UUID):
            cashier_open = str(self.cashier_open)
        else:
            cashier_open = self.cashier_open

        cashier_close: Union[None, Unset, str]
        if isinstance(self.cashier_close, Unset):
            cashier_close = UNSET
        elif isinstance(self.cashier_close, UUID):
            cashier_close = str(self.cashier_close)
        else:
            cashier_close = self.cashier_close

        device_rn: Union[None, Unset, str]
        if isinstance(self.device_rn, Unset):
            device_rn = UNSET
        else:
            device_rn = self.device_rn

        counters: Union[None, Unset, dict[str, Any]]
        if isinstance(self.counters, Unset):
            counters = UNSET
        elif isinstance(self.counters, NebularApiModelsCommonApiСOunters):
            counters = self.counters.to_dict()
        else:
            counters = self.counters

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        reconciliations: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.reconciliations, Unset):
            reconciliations = UNSET
        elif isinstance(self.reconciliations, list):
            reconciliations = []
            for reconciliations_type_0_item_data in self.reconciliations:
                reconciliations_type_0_item = reconciliations_type_0_item_data.to_dict()
                reconciliations.append(reconciliations_type_0_item)

        else:
            reconciliations = self.reconciliations

        external_user_id: Union[None, Unset, str]
        if isinstance(self.external_user_id, Unset):
            external_user_id = UNSET
        else:
            external_user_id = self.external_user_id

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if cash_at_start is not UNSET:
            field_dict["cashAtStart"] = cash_at_start
        if date_close is not UNSET:
            field_dict["dateClose"] = date_close
        if cash_at_end is not UNSET:
            field_dict["cashAtEnd"] = cash_at_end
        if device_sn is not UNSET:
            field_dict["deviceSN"] = device_sn
        if fs_number is not UNSET:
            field_dict["fsNumber"] = fs_number
        if cashier_open is not UNSET:
            field_dict["cashierOpen"] = cashier_open
        if cashier_close is not UNSET:
            field_dict["cashierClose"] = cashier_close
        if device_rn is not UNSET:
            field_dict["deviceRN"] = device_rn
        if counters is not UNSET:
            field_dict["counters"] = counters
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if reconciliations is not UNSET:
            field_dict["reconciliations"] = reconciliations
        if external_user_id is not UNSET:
            field_dict["externalUserId"] = external_user_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_reconciliations import NebularApiModelsCommonApiReconciliations
        from ..models.nebular_api_models_common_api_с_ounters import NebularApiModelsCommonApiСOunters

        d = dict(src_dict)

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

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_cash_at_start(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cash_at_start = _parse_cash_at_start(d.pop("cashAtStart", UNSET))

        def _parse_date_close(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_close_type_0 = isoparse(data)

                return date_close_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_close = _parse_date_close(d.pop("dateClose", UNSET))

        def _parse_cash_at_end(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cash_at_end = _parse_cash_at_end(d.pop("cashAtEnd", UNSET))

        def _parse_device_sn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_sn = _parse_device_sn(d.pop("deviceSN", UNSET))

        def _parse_fs_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fs_number = _parse_fs_number(d.pop("fsNumber", UNSET))

        def _parse_cashier_open(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cashier_open_type_0 = UUID(data)

                return cashier_open_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cashier_open = _parse_cashier_open(d.pop("cashierOpen", UNSET))

        def _parse_cashier_close(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cashier_close_type_0 = UUID(data)

                return cashier_close_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cashier_close = _parse_cashier_close(d.pop("cashierClose", UNSET))

        def _parse_device_rn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_rn = _parse_device_rn(d.pop("deviceRN", UNSET))

        def _parse_counters(data: object) -> Union["NebularApiModelsCommonApiСOunters", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counters_type_1 = NebularApiModelsCommonApiСOunters.from_dict(data)

                return counters_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiСOunters", None, Unset], data)

        counters = _parse_counters(d.pop("counters", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_reconciliations(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsCommonApiReconciliations"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reconciliations_type_0 = []
                _reconciliations_type_0 = data
                for reconciliations_type_0_item_data in _reconciliations_type_0:
                    reconciliations_type_0_item = NebularApiModelsCommonApiReconciliations.from_dict(
                        reconciliations_type_0_item_data
                    )

                    reconciliations_type_0.append(reconciliations_type_0_item)

                return reconciliations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsCommonApiReconciliations"]], data)

        reconciliations = _parse_reconciliations(d.pop("reconciliations", UNSET))

        def _parse_external_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_user_id = _parse_external_user_id(d.pop("externalUserId", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position = _parse_position(d.pop("position", UNSET))

        nebular_api_models_lk_service_lk_shift = cls(
            id=id,
            number=number,
            start_date=start_date,
            cash_at_start=cash_at_start,
            date_close=date_close,
            cash_at_end=cash_at_end,
            device_sn=device_sn,
            fs_number=fs_number,
            cashier_open=cashier_open,
            cashier_close=cashier_close,
            device_rn=device_rn,
            counters=counters,
            updated_at=updated_at,
            reconciliations=reconciliations,
            external_user_id=external_user_id,
            position=position,
        )

        return nebular_api_models_lk_service_lk_shift
