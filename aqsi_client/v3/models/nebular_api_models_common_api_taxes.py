from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums


T = TypeVar("T", bound="NebularApiModelsCommonApiTaxes")


@_attrs_define
class NebularApiModelsCommonApiTaxes:
    """
    Attributes:
        vat20 (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">НДС 20%</div>
            <div class="apidocs-english">Vat 20%</div>
        vat10 (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">НДС 10%</div>
            <div class="apidocs-english">Vat 10%</div>
        vat0 (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">НДС 0%</div>
            <div class="apidocs-english">Vat 0%</div>
        without_vat (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">без
            НДС</div>
            <div class="apidocs-english">Without vat</div>
        vat120 (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">НДС
            20/120%</div>
            <div class="apidocs-english">Vat 20/120%</div>
        vat110 (Union['NebularApiModelsCommonApiCashModeSums', None, Unset]): <div class="apidocs-russian">НДС
            10/110%</div>
            <div class="apidocs-english">Vat 10/110%</div>
    """

    vat20: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    vat10: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    vat0: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    without_vat: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    vat120: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET
    vat110: Union["NebularApiModelsCommonApiCashModeSums", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums

        vat20: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vat20, Unset):
            vat20 = UNSET
        elif isinstance(self.vat20, NebularApiModelsCommonApiCashModeSums):
            vat20 = self.vat20.to_dict()
        else:
            vat20 = self.vat20

        vat10: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vat10, Unset):
            vat10 = UNSET
        elif isinstance(self.vat10, NebularApiModelsCommonApiCashModeSums):
            vat10 = self.vat10.to_dict()
        else:
            vat10 = self.vat10

        vat0: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vat0, Unset):
            vat0 = UNSET
        elif isinstance(self.vat0, NebularApiModelsCommonApiCashModeSums):
            vat0 = self.vat0.to_dict()
        else:
            vat0 = self.vat0

        without_vat: Union[None, Unset, dict[str, Any]]
        if isinstance(self.without_vat, Unset):
            without_vat = UNSET
        elif isinstance(self.without_vat, NebularApiModelsCommonApiCashModeSums):
            without_vat = self.without_vat.to_dict()
        else:
            without_vat = self.without_vat

        vat120: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vat120, Unset):
            vat120 = UNSET
        elif isinstance(self.vat120, NebularApiModelsCommonApiCashModeSums):
            vat120 = self.vat120.to_dict()
        else:
            vat120 = self.vat120

        vat110: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vat110, Unset):
            vat110 = UNSET
        elif isinstance(self.vat110, NebularApiModelsCommonApiCashModeSums):
            vat110 = self.vat110.to_dict()
        else:
            vat110 = self.vat110

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if vat20 is not UNSET:
            field_dict["vat20"] = vat20
        if vat10 is not UNSET:
            field_dict["vat10"] = vat10
        if vat0 is not UNSET:
            field_dict["vat0"] = vat0
        if without_vat is not UNSET:
            field_dict["withoutVat"] = without_vat
        if vat120 is not UNSET:
            field_dict["vat120"] = vat120
        if vat110 is not UNSET:
            field_dict["vat110"] = vat110

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_cash_mode_sums import NebularApiModelsCommonApiCashModeSums

        d = dict(src_dict)

        def _parse_vat20(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat20_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return vat20_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        vat20 = _parse_vat20(d.pop("vat20", UNSET))

        def _parse_vat10(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat10_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return vat10_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        vat10 = _parse_vat10(d.pop("vat10", UNSET))

        def _parse_vat0(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat0_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return vat0_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        vat0 = _parse_vat0(d.pop("vat0", UNSET))

        def _parse_without_vat(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                without_vat_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return without_vat_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        without_vat = _parse_without_vat(d.pop("withoutVat", UNSET))

        def _parse_vat120(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat120_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return vat120_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        vat120 = _parse_vat120(d.pop("vat120", UNSET))

        def _parse_vat110(data: object) -> Union["NebularApiModelsCommonApiCashModeSums", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat110_type_1 = NebularApiModelsCommonApiCashModeSums.from_dict(data)

                return vat110_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiCashModeSums", None, Unset], data)

        vat110 = _parse_vat110(d.pop("vat110", UNSET))

        nebular_api_models_common_api_taxes = cls(
            vat20=vat20,
            vat10=vat10,
            vat0=vat0,
            without_vat=without_vat,
            vat120=vat120,
            vat110=vat110,
        )

        return nebular_api_models_common_api_taxes
