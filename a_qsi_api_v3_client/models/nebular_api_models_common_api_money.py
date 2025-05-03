from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums


T = TypeVar("T", bound="NebularApiModelsCommonApiMoney")


@_attrs_define
class NebularApiModelsCommonApiMoney:
    """
    Attributes:
        cash (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">Наличные</div>
            <div class="apidocs-english">Cash</div>
        card (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">Карта</div>
            <div class="apidocs-english">Card</div>
        advance (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">Аванс</div>
            <div class="apidocs-english">Advance</div>
        credit (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">Кредит</div>
            <div class="apidocs-english">Credit</div>
        consideration (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-
            russian">БСО</div>
            <div class="apidocs-english">Consideration</div>
    """

    cash: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    card: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    advance: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    credit: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    consideration: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums

        cash: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cash, Unset):
            cash = UNSET
        elif isinstance(self.cash, NebularApiModelsCommonApiCashModeSums):
            cash = self.cash.to_dict()
        else:
            cash = self.cash

        card: Union[None, Unset, dict[str, Any]]
        if isinstance(self.card, Unset):
            card = UNSET
        elif isinstance(self.card, NebularApiModelsCommonApiCashModeSums):
            card = self.card.to_dict()
        else:
            card = self.card

        advance: Union[None, Unset, dict[str, Any]]
        if isinstance(self.advance, Unset):
            advance = UNSET
        elif isinstance(self.advance, NebularApiModelsCommonApiCashModeSums):
            advance = self.advance.to_dict()
        else:
            advance = self.advance

        credit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.credit, Unset):
            credit = UNSET
        elif isinstance(self.credit, NebularApiModelsCommonApiCashModeSums):
            credit = self.credit.to_dict()
        else:
            credit = self.credit

        consideration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.consideration, Unset):
            consideration = UNSET
        elif isinstance(self.consideration, NebularApiModelsCommonApiCashModeSums):
            consideration = self.consideration.to_dict()
        else:
            consideration = self.consideration

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if cash is not UNSET:
            field_dict["cash"] = cash
        if card is not UNSET:
            field_dict["card"] = card
        if advance is not UNSET:
            field_dict["advance"] = advance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if consideration is not UNSET:
            field_dict["consideration"] = consideration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums

        d = dict(src_dict)

        def _parse_cash(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cash_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return cash_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        cash = _parse_cash(d.pop("cash", UNSET))

        def _parse_card(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                card_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return card_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        card = _parse_card(d.pop("card", UNSET))

        def _parse_advance(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                advance_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return advance_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        advance = _parse_advance(d.pop("advance", UNSET))

        def _parse_credit(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credit_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return credit_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        credit = _parse_credit(d.pop("credit", UNSET))

        def _parse_consideration(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consideration_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return consideration_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        consideration = _parse_consideration(d.pop("consideration", UNSET))

        nebular_api_models_common_api_money = cls(
            cash=cash,
            card=card,
            advance=advance,
            credit=credit,
            consideration=consideration,
        )

        return nebular_api_models_common_api_money
