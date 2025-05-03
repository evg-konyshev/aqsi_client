from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsCommonApiCashModeSums")


@_attrs_define
class NebularApiModelsCommonApiCashModeSums:
    """
    Attributes:
        sell (Union[Unset, float]): <div class="apidocs-russian">Сумма в режиме приход</div>
            <div class="apidocs-english">Receipt mode sum</div>
        sell_return (Union[Unset, float]): <div class="apidocs-russian">Сумма в режиме возврат прихода</div>
            <div class="apidocs-english">Return receipt mode sum</div>
        buy (Union[Unset, float]): <div class="apidocs-russian">Сумма в режиме расход</div>
            <div class="apidocs-english">Expense mode sum</div>
        buy_return (Union[Unset, float]): <div class="apidocs-russian">Сумма в режиме возврат расхода</div>
            <div class="apidocs-english">Return expense mode sum</div>
    """

    sell: Union[Unset, float] = UNSET
    sell_return: Union[Unset, float] = UNSET
    buy: Union[Unset, float] = UNSET
    buy_return: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        sell = self.sell

        sell_return = self.sell_return

        buy = self.buy

        buy_return = self.buy_return

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if sell is not UNSET:
            field_dict["sell"] = sell
        if sell_return is not UNSET:
            field_dict["sellReturn"] = sell_return
        if buy is not UNSET:
            field_dict["buy"] = buy
        if buy_return is not UNSET:
            field_dict["buyReturn"] = buy_return

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sell = d.pop("sell", UNSET)

        sell_return = d.pop("sellReturn", UNSET)

        buy = d.pop("buy", UNSET)

        buy_return = d.pop("buyReturn", UNSET)

        nebular_api_models_common_api_cash_mode_sums = cls(
            sell=sell,
            sell_return=sell_return,
            buy=buy,
            buy_return=buy_return,
        )

        return nebular_api_models_common_api_cash_mode_sums
