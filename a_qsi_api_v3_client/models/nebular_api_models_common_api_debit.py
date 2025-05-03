from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_cheque import NebularApiModelsCommonApiCheque


T = TypeVar("T", bound="NebularApiModelsCommonApiDebit")


@_attrs_define
class NebularApiModelsCommonApiDebit:
    """<div class="apidocs-russian">Информация о списании бонусов c карты</div>
    <div class="apidocs-english">Information on writing off bonuses from the card</div>

        Attributes:
            hash_ (Union[None, Unset, str]): <div class="apidocs-russian">Хэш считанной карты</div>
                <div class="apidocs-english">Read card hash</div>
            pan4 (Union[None, Unset, str]): <div class="apidocs-russian">PAN4 считанной карты</div>
                <div class="apidocs-english">PAN4 read card</div>
            slip (Union[None, Unset, str]): <div class="apidocs-russian">Слип СПАСИБО</div>
                <div class="apidocs-english">SPASIBO slip</div>
            discount (Union[None, Unset, list['NebularApiModelsCommonApiCheque']]): <div class="apidocs-russian">Скидка
                распределенная по позициям</div>
                <div class="apidocs-english">Discount distributed by items</div>
            cheque (Union[None, Unset, list['NebularApiModelsCommonApiCheque']]): <div class="apidocs-russian">Список
                позиций</div>
                <div class="apidocs-english">Positions list</div>
            currency (Union[None, Unset, str]): <div class="apidocs-russian">Код валюты согласно ISO 4217</div>
                <div class="apidocs-english">Currency code according to ISO 4217</div>
            partner_id (Union[None, Unset, str]): <div class="apidocs-russian">Код партнера СПАСИБО</div>
                <div class="apidocs-english">SPASIBO partner code</div>
            terminal_id (Union[None, Unset, str]): <div class="apidocs-russian">ID терминала</div>
                <div class="apidocs-english">Terminal id</div>
            amount_to_pay (Union[Unset, int]): <div class="apidocs-russian">Сумма к оплате с учетом вычтеных бонусов в
                мининимальных единицах</div>
                <div class="apidocs-english">Amount to be paid, taking into account deducted bonuses, in minimum units</div>
            date_and_time (Union[None, Unset, str]): <div class="apidocs-russian">Дата и время транзакции в исходном
                формате</div>
                <div class="apidocs-english">Date and time of the transaction in original format</div>
            total_amount (Union[Unset, int]): <div class="apidocs-russian">Сумма до вычета бонусов</div>
                <div class="apidocs-english">Amount before deducting bonuses</div>
            id_transaction (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор транзакции</div>
                <div class="apidocs-english">Transaction id</div>
            terminal_location (Union[None, Unset, str]): <div class="apidocs-russian">Локация терминала</div>
                <div class="apidocs-english">Terminal location</div>
            bonuses (Union[Unset, int]): <div class="apidocs-russian">Количество списанных бонусов в мин. единицах</div>
                <div class="apidocs-english">The number of debited bonuses in minimum units</div>
    """

    hash_: Union[None, Unset, str] = UNSET
    pan4: Union[None, Unset, str] = UNSET
    slip: Union[None, Unset, str] = UNSET
    discount: Union[None, Unset, list["NebularApiModelsCommonApiCheque"]] = UNSET
    cheque: Union[None, Unset, list["NebularApiModelsCommonApiCheque"]] = UNSET
    currency: Union[None, Unset, str] = UNSET
    partner_id: Union[None, Unset, str] = UNSET
    terminal_id: Union[None, Unset, str] = UNSET
    amount_to_pay: Union[Unset, int] = UNSET
    date_and_time: Union[None, Unset, str] = UNSET
    total_amount: Union[Unset, int] = UNSET
    id_transaction: Union[None, Unset, str] = UNSET
    terminal_location: Union[None, Unset, str] = UNSET
    bonuses: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        hash_: Union[None, Unset, str]
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        pan4: Union[None, Unset, str]
        if isinstance(self.pan4, Unset):
            pan4 = UNSET
        else:
            pan4 = self.pan4

        slip: Union[None, Unset, str]
        if isinstance(self.slip, Unset):
            slip = UNSET
        else:
            slip = self.slip

        discount: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.discount, Unset):
            discount = UNSET
        elif isinstance(self.discount, list):
            discount = []
            for discount_type_0_item_data in self.discount:
                discount_type_0_item = discount_type_0_item_data.to_dict()
                discount.append(discount_type_0_item)

        else:
            discount = self.discount

        cheque: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.cheque, Unset):
            cheque = UNSET
        elif isinstance(self.cheque, list):
            cheque = []
            for cheque_type_0_item_data in self.cheque:
                cheque_type_0_item = cheque_type_0_item_data.to_dict()
                cheque.append(cheque_type_0_item)

        else:
            cheque = self.cheque

        currency: Union[None, Unset, str]
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        partner_id: Union[None, Unset, str]
        if isinstance(self.partner_id, Unset):
            partner_id = UNSET
        else:
            partner_id = self.partner_id

        terminal_id: Union[None, Unset, str]
        if isinstance(self.terminal_id, Unset):
            terminal_id = UNSET
        else:
            terminal_id = self.terminal_id

        amount_to_pay = self.amount_to_pay

        date_and_time: Union[None, Unset, str]
        if isinstance(self.date_and_time, Unset):
            date_and_time = UNSET
        else:
            date_and_time = self.date_and_time

        total_amount = self.total_amount

        id_transaction: Union[None, Unset, str]
        if isinstance(self.id_transaction, Unset):
            id_transaction = UNSET
        else:
            id_transaction = self.id_transaction

        terminal_location: Union[None, Unset, str]
        if isinstance(self.terminal_location, Unset):
            terminal_location = UNSET
        else:
            terminal_location = self.terminal_location

        bonuses = self.bonuses

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if pan4 is not UNSET:
            field_dict["pan4"] = pan4
        if slip is not UNSET:
            field_dict["slip"] = slip
        if discount is not UNSET:
            field_dict["discount"] = discount
        if cheque is not UNSET:
            field_dict["cheque"] = cheque
        if currency is not UNSET:
            field_dict["currency"] = currency
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if terminal_id is not UNSET:
            field_dict["terminalId"] = terminal_id
        if amount_to_pay is not UNSET:
            field_dict["amountToPay"] = amount_to_pay
        if date_and_time is not UNSET:
            field_dict["dateAndTime"] = date_and_time
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if id_transaction is not UNSET:
            field_dict["idTransaction"] = id_transaction
        if terminal_location is not UNSET:
            field_dict["terminalLocation"] = terminal_location
        if bonuses is not UNSET:
            field_dict["bonuses"] = bonuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_cheque import NebularApiModelsCommonApiCheque

        d = dict(src_dict)

        def _parse_hash_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        def _parse_pan4(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pan4 = _parse_pan4(d.pop("pan4", UNSET))

        def _parse_slip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slip = _parse_slip(d.pop("slip", UNSET))

        def _parse_discount(data: object) -> Union[None, Unset, list["NebularApiModelsCommonApiCheque"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                discount_type_0 = []
                _discount_type_0 = data
                for discount_type_0_item_data in _discount_type_0:
                    discount_type_0_item = NebularApiModelsCommonApiCheque.from_dict(discount_type_0_item_data)

                    discount_type_0.append(discount_type_0_item)

                return discount_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsCommonApiCheque"]], data)

        discount = _parse_discount(d.pop("discount", UNSET))

        def _parse_cheque(data: object) -> Union[None, Unset, list["NebularApiModelsCommonApiCheque"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cheque_type_0 = []
                _cheque_type_0 = data
                for cheque_type_0_item_data in _cheque_type_0:
                    cheque_type_0_item = NebularApiModelsCommonApiCheque.from_dict(cheque_type_0_item_data)

                    cheque_type_0.append(cheque_type_0_item)

                return cheque_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsCommonApiCheque"]], data)

        cheque = _parse_cheque(d.pop("cheque", UNSET))

        def _parse_currency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_partner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        partner_id = _parse_partner_id(d.pop("partnerId", UNSET))

        def _parse_terminal_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terminal_id = _parse_terminal_id(d.pop("terminalId", UNSET))

        amount_to_pay = d.pop("amountToPay", UNSET)

        def _parse_date_and_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_and_time = _parse_date_and_time(d.pop("dateAndTime", UNSET))

        total_amount = d.pop("totalAmount", UNSET)

        def _parse_id_transaction(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id_transaction = _parse_id_transaction(d.pop("idTransaction", UNSET))

        def _parse_terminal_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terminal_location = _parse_terminal_location(d.pop("terminalLocation", UNSET))

        bonuses = d.pop("bonuses", UNSET)

        nebular_api_models_common_api_debit = cls(
            hash_=hash_,
            pan4=pan4,
            slip=slip,
            discount=discount,
            cheque=cheque,
            currency=currency,
            partner_id=partner_id,
            terminal_id=terminal_id,
            amount_to_pay=amount_to_pay,
            date_and_time=date_and_time,
            total_amount=total_amount,
            id_transaction=id_transaction,
            terminal_location=terminal_location,
            bonuses=bonuses,
        )

        return nebular_api_models_common_api_debit
