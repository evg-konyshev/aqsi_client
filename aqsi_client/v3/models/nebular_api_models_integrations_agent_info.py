from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from aqsi_client.types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsIntegrationsAgentInfo")


@_attrs_define
class NebularApiModelsIntegrationsAgentInfo:
    """<div class="apidocs-russian apidocs-ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
    <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
    <div class="apidocs-russian">Данные агента, 1223 (На текущий момент длина сериализованных данных тэга не должна
    превышать 243 байта)</div>
    <div class="apidocs-english">Agent Data, 1223 (Currently, the length of serialized tag data should not exceed 243
    bytes)</div>

        Attributes:
            payment_transfer_operator_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-
                ffd-availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Телефон оператора перевода, 1075</div>
                <div class="apidocs-english tag-value">Payment transfer operator phone numbers , 1075</div>
            payment_agent_operation (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Операция платежного агента, 1044</div>
                <div class="apidocs-english tag-value">Payment agent operation, 1044</div>
            payment_agent_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Телефон платежного агента, 1073</div>
                <div class="apidocs-english tag-value">Payment agent phone numbers</div>
            payment_operator_phone_numbers (Union[None, Unset, list[str]]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Телефон оператора по приему платежей, 1074</div>
                <div class="apidocs-english tag-value">Payment operator phone numbers, 1074</div>
            payment_operator_name (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Наименование оператора перевода, 1026</div>
                <div class="apidocs-english tag-value">Payment operator name, 1026</div>
            payment_operator_address (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">Адрес оператора перевода, 1005</div>
                <div class="apidocs-english tag-value">Payment operator address, 1005</div>
            payment_operator_inn (Union[None, Unset, str]): <div class="apidocs-russian apidocs-ffd-
                availability">Соответствует: ФФД 1.05, ФФД 1.2</div>
                <div class="apidocs-english apidocs-ffd-availability">Available in: FFD 1.05, FFD 1.2</div>
                <div class="apidocs-russian tag-value">ИНН оператора перевода, 1016</div>
                <div class="apidocs-english tag-value">Payment operator TIN, 1016</div>
    """

    payment_transfer_operator_phone_numbers: Union[None, Unset, list[str]] = UNSET
    payment_agent_operation: Union[None, Unset, str] = UNSET
    payment_agent_phone_numbers: Union[None, Unset, list[str]] = UNSET
    payment_operator_phone_numbers: Union[None, Unset, list[str]] = UNSET
    payment_operator_name: Union[None, Unset, str] = UNSET
    payment_operator_address: Union[None, Unset, str] = UNSET
    payment_operator_inn: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        payment_transfer_operator_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_transfer_operator_phone_numbers, Unset):
            payment_transfer_operator_phone_numbers = UNSET
        elif isinstance(self.payment_transfer_operator_phone_numbers, list):
            payment_transfer_operator_phone_numbers = self.payment_transfer_operator_phone_numbers

        else:
            payment_transfer_operator_phone_numbers = self.payment_transfer_operator_phone_numbers

        payment_agent_operation: Union[None, Unset, str]
        if isinstance(self.payment_agent_operation, Unset):
            payment_agent_operation = UNSET
        else:
            payment_agent_operation = self.payment_agent_operation

        payment_agent_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_agent_phone_numbers, Unset):
            payment_agent_phone_numbers = UNSET
        elif isinstance(self.payment_agent_phone_numbers, list):
            payment_agent_phone_numbers = self.payment_agent_phone_numbers

        else:
            payment_agent_phone_numbers = self.payment_agent_phone_numbers

        payment_operator_phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.payment_operator_phone_numbers, Unset):
            payment_operator_phone_numbers = UNSET
        elif isinstance(self.payment_operator_phone_numbers, list):
            payment_operator_phone_numbers = self.payment_operator_phone_numbers

        else:
            payment_operator_phone_numbers = self.payment_operator_phone_numbers

        payment_operator_name: Union[None, Unset, str]
        if isinstance(self.payment_operator_name, Unset):
            payment_operator_name = UNSET
        else:
            payment_operator_name = self.payment_operator_name

        payment_operator_address: Union[None, Unset, str]
        if isinstance(self.payment_operator_address, Unset):
            payment_operator_address = UNSET
        else:
            payment_operator_address = self.payment_operator_address

        payment_operator_inn: Union[None, Unset, str]
        if isinstance(self.payment_operator_inn, Unset):
            payment_operator_inn = UNSET
        else:
            payment_operator_inn = self.payment_operator_inn

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if payment_transfer_operator_phone_numbers is not UNSET:
            field_dict["paymentTransferOperatorPhoneNumbers"] = payment_transfer_operator_phone_numbers
        if payment_agent_operation is not UNSET:
            field_dict["paymentAgentOperation"] = payment_agent_operation
        if payment_agent_phone_numbers is not UNSET:
            field_dict["paymentAgentPhoneNumbers"] = payment_agent_phone_numbers
        if payment_operator_phone_numbers is not UNSET:
            field_dict["paymentOperatorPhoneNumbers"] = payment_operator_phone_numbers
        if payment_operator_name is not UNSET:
            field_dict["paymentOperatorName"] = payment_operator_name
        if payment_operator_address is not UNSET:
            field_dict["paymentOperatorAddress"] = payment_operator_address
        if payment_operator_inn is not UNSET:
            field_dict["paymentOperatorINN"] = payment_operator_inn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_payment_transfer_operator_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_transfer_operator_phone_numbers_type_0 = cast(list[str], data)

                return payment_transfer_operator_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_transfer_operator_phone_numbers = _parse_payment_transfer_operator_phone_numbers(
            d.pop("paymentTransferOperatorPhoneNumbers", UNSET)
        )

        def _parse_payment_agent_operation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_agent_operation = _parse_payment_agent_operation(d.pop("paymentAgentOperation", UNSET))

        def _parse_payment_agent_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_agent_phone_numbers_type_0 = cast(list[str], data)

                return payment_agent_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_agent_phone_numbers = _parse_payment_agent_phone_numbers(d.pop("paymentAgentPhoneNumbers", UNSET))

        def _parse_payment_operator_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_operator_phone_numbers_type_0 = cast(list[str], data)

                return payment_operator_phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        payment_operator_phone_numbers = _parse_payment_operator_phone_numbers(
            d.pop("paymentOperatorPhoneNumbers", UNSET)
        )

        def _parse_payment_operator_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_name = _parse_payment_operator_name(d.pop("paymentOperatorName", UNSET))

        def _parse_payment_operator_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_address = _parse_payment_operator_address(d.pop("paymentOperatorAddress", UNSET))

        def _parse_payment_operator_inn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_operator_inn = _parse_payment_operator_inn(d.pop("paymentOperatorINN", UNSET))

        nebular_api_models_integrations_agent_info = cls(
            payment_transfer_operator_phone_numbers=payment_transfer_operator_phone_numbers,
            payment_agent_operation=payment_agent_operation,
            payment_agent_phone_numbers=payment_agent_phone_numbers,
            payment_operator_phone_numbers=payment_operator_phone_numbers,
            payment_operator_name=payment_operator_name,
            payment_operator_address=payment_operator_address,
            payment_operator_inn=payment_operator_inn,
        )

        return nebular_api_models_integrations_agent_info
