from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_money import NebularApiModelsCommonApiMoney
    from ..models.nebular_api_models_common_api_taxes import NebularApiModelsCommonApiTaxes


T = TypeVar("T", bound="NebularApiModelsCommonApiСOunters")


@_attrs_define
class NebularApiModelsCommonApiСOunters:
    """
    Attributes:
        taxes (Union['NebularApiModelsCommonApiTaxes', None, Unset]): <div class="apidocs-russian">Суммы по типам
            налогов</div>
            <div class="apidocs-english">Taxes sum</div>
        money (Union['NebularApiModelsCommonApiMoney', None, Unset]): <div class="apidocs-russian">Суммы по типам
            оплаты</div>
            <div class="apidocs-english">Money sum</div>
    """

    taxes: Union["NebularApiModelsCommonApiTaxes", None, Unset] = UNSET
    money: Union["NebularApiModelsCommonApiMoney", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_money import NebularApiModelsCommonApiMoney
        from ..models.nebular_api_models_common_api_taxes import NebularApiModelsCommonApiTaxes

        taxes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.taxes, Unset):
            taxes = UNSET
        elif isinstance(self.taxes, NebularApiModelsCommonApiTaxes):
            taxes = self.taxes.to_dict()
        else:
            taxes = self.taxes

        money: Union[None, Unset, dict[str, Any]]
        if isinstance(self.money, Unset):
            money = UNSET
        elif isinstance(self.money, NebularApiModelsCommonApiMoney):
            money = self.money.to_dict()
        else:
            money = self.money

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if money is not UNSET:
            field_dict["money"] = money

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_money import NebularApiModelsCommonApiMoney
        from ..models.nebular_api_models_common_api_taxes import NebularApiModelsCommonApiTaxes

        d = dict(src_dict)

        def _parse_taxes(data: object) -> Union["NebularApiModelsCommonApiTaxes", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                taxes_type_1 = NebularApiModelsCommonApiTaxes.from_dict(data)

                return taxes_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiTaxes", None, Unset], data)

        taxes = _parse_taxes(d.pop("taxes", UNSET))

        def _parse_money(data: object) -> Union["NebularApiModelsCommonApiMoney", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                money_type_1 = NebularApiModelsCommonApiMoney.from_dict(data)

                return money_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiMoney", None, Unset], data)

        money = _parse_money(d.pop("money", UNSET))

        nebular_api_models_common_api_с_ounters = cls(
            taxes=taxes,
            money=money,
        )

        return nebular_api_models_common_api_с_ounters
