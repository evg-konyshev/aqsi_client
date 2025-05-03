from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_credit import NebularApiModelsCommonApiCredit
    from ..models.nebular_api_models_common_api_debit import NebularApiModelsCommonApiDebit


T = TypeVar("T", bound="NebularApiModelsCommonApiSpasibo")


@_attrs_define
class NebularApiModelsCommonApiSpasibo:
    """<div class="apidocs-russian">"Спасибо" транзакции по платежу</div>
    <div class="apidocs-english">"Spasibo" transactions for a payment</div>

        Attributes:
            credit (Union['NebularApiModelsCommonApiCredit', None, Unset]): <div class="apidocs-russian">Информация о
                зачислении бонусов на карту</div>
                <div class="apidocs-english">Information on crediting bonuses</div>
            debit (Union['NebularApiModelsCommonApiDebit', None, Unset]): <div class="apidocs-russian">Информация о списании
                бонусов c карты</div>
                <div class="apidocs-english">Information on writing off bonuses from the card</div>
    """

    credit: Union["NebularApiModelsCommonApiCredit", None, Unset] = UNSET
    debit: Union["NebularApiModelsCommonApiDebit", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_credit import NebularApiModelsCommonApiCredit
        from ..models.nebular_api_models_common_api_debit import NebularApiModelsCommonApiDebit

        credit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.credit, Unset):
            credit = UNSET
        elif isinstance(self.credit, NebularApiModelsCommonApiCredit):
            credit = self.credit.to_dict()
        else:
            credit = self.credit

        debit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.debit, Unset):
            debit = UNSET
        elif isinstance(self.debit, NebularApiModelsCommonApiDebit):
            debit = self.debit.to_dict()
        else:
            debit = self.debit

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if credit is not UNSET:
            field_dict["credit"] = credit
        if debit is not UNSET:
            field_dict["debit"] = debit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_credit import NebularApiModelsCommonApiCredit
        from ..models.nebular_api_models_common_api_debit import NebularApiModelsCommonApiDebit

        d = dict(src_dict)

        def _parse_credit(data: object) -> Union["NebularApiModelsCommonApiCredit", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credit_type_1 = NebularApiModelsCommonApiCredit.from_dict(data)

                return credit_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCredit", None, Unset], data)

        credit = _parse_credit(d.pop("credit", UNSET))

        def _parse_debit(data: object) -> Union["NebularApiModelsCommonApiDebit", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debit_type_1 = NebularApiModelsCommonApiDebit.from_dict(data)

                return debit_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiDebit", None, Unset], data)

        debit = _parse_debit(d.pop("debit", UNSET))

        nebular_api_models_common_api_spasibo = cls(
            credit=credit,
            debit=debit,
        )

        return nebular_api_models_common_api_spasibo
