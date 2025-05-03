from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.nebular_api_enums_agent_type_enum import NebularApiEnumsAgentTypeEnum
from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
    from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo


T = TypeVar("T", bound="NebularApiModelsLkServiceReceiptProperties")


@_attrs_define
class NebularApiModelsLkServiceReceiptProperties:
    """<div class="apidocs-russian">Параметры по умолчанию для позиции</div>
    <div class="apidocs-english">Default position parameters</div>

        Attributes:
            supplier_info (Union['NebularApiModelsIntegrationsSupplierInfo', None, Unset]): <div class="apidocs-
                russian">Данные поставщика, 1224</div>
                <div class="apidocs-english">Supplier info, 1224</div>
            supplier_inn (Union[None, Unset, str]): <div class="apidocs-russian">ИНН поставщика, 1226</div>
                <div class="apidocs-english">Supplier TIN, 1226</div>
            agent_type (Union[NebularApiEnumsAgentTypeEnum, None, Unset]): <div class="apidocs-russian">Признак агента по
                предмету расчета, 1222</div>
                <div class="apidocs-english">Agent type for the subject of calculation, 1222</div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 0 (1)</div><div style="margin:
                0 0.25em;">-</div><div class="apidocs-russian">Банковский платежный агент</div><div class="apidocs-
                english">Payment bank agent</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 1 (2)</div><div style="margin:
                0 0.25em;">-</div><div class="apidocs-russian">Банковский платежный субагент</div><div class="apidocs-
                english">Payment bank sub agent</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 2 (4)</div><div style="margin:
                0 0.25em;">-</div><div class="apidocs-russian">Платежный агент</div><div class="apidocs-english">Paying
                agent</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 3 (8)</div><div style="margin:
                0 0.25em;">-</div><div class="apidocs-russian">Платежный субагент</div><div class="apidocs-english">Paying sub
                agent</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 4 (16)</div><div
                style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Поверенный</div><div class="apidocs-
                english">Attorney</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 5 (32)</div><div
                style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Комиссионер</div><div class="apidocs-
                english">Comissioner</div></div>
                <div style="display: flex;margin-top: 4px;"><div style="white-space: nowrap;">��� 6 (64)</div><div
                style="margin: 0 0.25em;">-</div><div class="apidocs-russian">Иной агент</div><div class="apidocs-english">Other
                agetn</div></div>
            agent_info (Union['NebularApiModelsIntegrationsAgentInfo', None, Unset]): <div class="apidocs-russian">Данные
                агента, 1223 </div>
                <div class="apidocs-english">Agetn info, 1223  </div>
            additional_attribute (Union[None, Unset, str]): <div class="apidocs-russian">Дополнительный реквизит предмета
                расчета, 1191</div>
                <div class="apidocs-english">Additional attribute of the subject of calculation, 1191</div>
            manufacturer_country_code (Union[None, Unset, str]): <div class="apidocs-russian">Код страны происхождения
                товара, 1230</div>
                <div class="apidocs-english">country of origin of the product code, 1230</div>
            customs_declaration_number (Union[None, Unset, str]): <div class="apidocs-russian">Номер таможенной декларации,
                1231</div>
                <div class="apidocs-english">Customs declaration number, 1231</div>
            excise (Union[None, Unset, float]): <div class="apidocs-russian">Акциз, 1229</div>
                <div class="apidocs-english">Excise, 1229</div>
    """

    supplier_info: Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset] = UNSET
    supplier_inn: Union[None, Unset, str] = UNSET
    agent_type: Union[NebularApiEnumsAgentTypeEnum, None, Unset] = UNSET
    agent_info: Union["NebularApiModelsIntegrationsAgentInfo", None, Unset] = UNSET
    additional_attribute: Union[None, Unset, str] = UNSET
    manufacturer_country_code: Union[None, Unset, str] = UNSET
    customs_declaration_number: Union[None, Unset, str] = UNSET
    excise: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo

        supplier_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.supplier_info, Unset):
            supplier_info = UNSET
        elif isinstance(self.supplier_info, NebularApiModelsIntegrationsSupplierInfo):
            supplier_info = self.supplier_info.to_dict()
        else:
            supplier_info = self.supplier_info

        supplier_inn: Union[None, Unset, str]
        if isinstance(self.supplier_inn, Unset):
            supplier_inn = UNSET
        else:
            supplier_inn = self.supplier_inn

        agent_type: Union[None, Unset, int]
        if isinstance(self.agent_type, Unset):
            agent_type = UNSET
        elif isinstance(self.agent_type, NebularApiEnumsAgentTypeEnum):
            agent_type = self.agent_type.value
        else:
            agent_type = self.agent_type

        agent_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.agent_info, Unset):
            agent_info = UNSET
        elif isinstance(self.agent_info, NebularApiModelsIntegrationsAgentInfo):
            agent_info = self.agent_info.to_dict()
        else:
            agent_info = self.agent_info

        additional_attribute: Union[None, Unset, str]
        if isinstance(self.additional_attribute, Unset):
            additional_attribute = UNSET
        else:
            additional_attribute = self.additional_attribute

        manufacturer_country_code: Union[None, Unset, str]
        if isinstance(self.manufacturer_country_code, Unset):
            manufacturer_country_code = UNSET
        else:
            manufacturer_country_code = self.manufacturer_country_code

        customs_declaration_number: Union[None, Unset, str]
        if isinstance(self.customs_declaration_number, Unset):
            customs_declaration_number = UNSET
        else:
            customs_declaration_number = self.customs_declaration_number

        excise: Union[None, Unset, float]
        if isinstance(self.excise, Unset):
            excise = UNSET
        else:
            excise = self.excise

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if supplier_inn is not UNSET:
            field_dict["supplierINN"] = supplier_inn
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type
        if agent_info is not UNSET:
            field_dict["agentInfo"] = agent_info
        if additional_attribute is not UNSET:
            field_dict["additionalAttribute"] = additional_attribute
        if manufacturer_country_code is not UNSET:
            field_dict["manufacturerCountryCode"] = manufacturer_country_code
        if customs_declaration_number is not UNSET:
            field_dict["customsDeclarationNumber"] = customs_declaration_number
        if excise is not UNSET:
            field_dict["excise"] = excise

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_integrations_agent_info import NebularApiModelsIntegrationsAgentInfo
        from ..models.nebular_api_models_integrations_supplier_info import NebularApiModelsIntegrationsSupplierInfo

        d = dict(src_dict)

        def _parse_supplier_info(data: object) -> Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                supplier_info_type_1 = NebularApiModelsIntegrationsSupplierInfo.from_dict(data)

                return supplier_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsSupplierInfo", None, Unset], data)

        supplier_info = _parse_supplier_info(d.pop("supplierInfo", UNSET))

        def _parse_supplier_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_inn = _parse_supplier_inn(d.pop("supplierINN", UNSET))

        def _parse_agent_type(data: object) -> Union[NebularApiEnumsAgentTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                agent_type_type_1 = NebularApiEnumsAgentTypeEnum(data)

                return agent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NebularApiEnumsAgentTypeEnum, None, Unset], data)

        agent_type = _parse_agent_type(d.pop("agentType", UNSET))

        def _parse_agent_info(data: object) -> Union["NebularApiModelsIntegrationsAgentInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_info_type_1 = NebularApiModelsIntegrationsAgentInfo.from_dict(data)

                return agent_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsIntegrationsAgentInfo", None, Unset], data)

        agent_info = _parse_agent_info(d.pop("agentInfo", UNSET))

        def _parse_additional_attribute(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_attribute = _parse_additional_attribute(d.pop("additionalAttribute", UNSET))

        def _parse_manufacturer_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer_country_code = _parse_manufacturer_country_code(d.pop("manufacturerCountryCode", UNSET))

        def _parse_customs_declaration_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customs_declaration_number = _parse_customs_declaration_number(d.pop("customsDeclarationNumber", UNSET))

        def _parse_excise(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        excise = _parse_excise(d.pop("excise", UNSET))

        nebular_api_models_lk_service_receipt_properties = cls(
            supplier_info=supplier_info,
            supplier_inn=supplier_inn,
            agent_type=agent_type,
            agent_info=agent_info,
            additional_attribute=additional_attribute,
            manufacturer_country_code=manufacturer_country_code,
            customs_declaration_number=customs_declaration_number,
            excise=excise,
        )

        return nebular_api_models_lk_service_receipt_properties
