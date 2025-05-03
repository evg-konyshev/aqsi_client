import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from aqsi_client.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_order_dto_content import NebularApiModelsCommonApiOrderDtoContent
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty


T = TypeVar("T", bound="NebularApiDtosCommonOrderDto")


@_attrs_define
class NebularApiDtosCommonOrderDto:
    """
    Example:
        {'id': 'c2e68ee4-1175-4524-a34f-70e287e553f1', 'number': '101ARS15/13475', 'externalSystem': None, 'dateTime':
            '2019-08-14T12:15:43.0000000+00:00', 'cashier': None, 'clientId': None, 'deliveryAddress': None, 'pickAddress':
            None, 'comment': None, 'status': None, 'content': {'discountMoney': '0', 'discountPercent': '0', 'type': 3,
            'positions': [{'sku': '', 'id': None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0, 'barcodes': None,
            'addingType': 0, 'addedAt': '2025-04-29T20:13:37.5961163+00:00', 'editable': True, 'quantity': 1, 'price': 10,
            'tax': 6, 'text': 'Договор страхования №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4,
            'agentInfo': None, 'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None, 'supplierInfo': None,
            'excise': None, 'agentType': None, 'customProperties': None, 'industryAttribute': None, 'noReturn': 0,
            'discountPercent': '0', 'maxDiscountPercent': '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments':
            [{'acquiringData': None, 'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None, 'paymentOperatorName':
            None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None, 'agentType': None,
            'paymentTransferOperatorPhoneNumbers': None, 'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers':
            None, 'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None, 'settlementAddress':
            'Москва, Кремль', 'settlementPlace': 'Жилое помещение', 'additionalAttribute': None, 'customer': 'Иванов Иван',
            'customerINN': None, 'customerInfo': None, 'industryAttribute': None, 'electronicCheck': None},
            'customProperties': None, 'cancellationReason': None, 'isEditableByDevice': True}

    Attributes:
        id (UUID): <div class="apidocs-russian">Идентификатор заказа</div>
            <div class="apidocs-english">Order identifier</div>
        number (str): <div class="apidocs-russian">Номер заказа</div>
            <div class="apidocs-english">Order number</div>
        date_time (datetime.datetime): <div class="apidocs-russian">Время создания заказа</div>
            <div class="apidocs-english">Order creation time</div>
        content (NebularApiModelsCommonApiOrderDtoContent): <div class="apidocs-russian"> Содержимое документа</div>
            <div class="apidocs-english">Document content</div>
        external_system (Union[None, Unset, str]): <div class="apidocs-russian">Название внешней системы</div>
            <div class="apidocs-english">External system name</div>
        cashier (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор кассира, если не указан Id
            устройства или магазина обязательно</div>
            <div class="apidocs-english">Cashier ID, if the device or store ID is not specified</div>
        client_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор клиента (Если заполнен
            идентификатор клиента, то поля customerContact, customer и customerINN игнорируются)</div>
            <div class="apidocs-english">Customer Identifier (customerContact, customer and customerINN fields will be
            ignored if clientId field is not empty)</div>
        delivery_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес доставки заказа</div>
            <div class="apidocs-english">Delivery address</div>
        pick_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес забора заказа</div>
            <div class="apidocs-english">Order pickup address</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий к заказу</div>
            <div class="apidocs-english">Order comment</div>
        status (Union[None, Unset, str]): <div class="apidocs-russian">Статус заказа 'Оплачен', 'Част. оплачен',
            'Отложен', 'Черновик', ' Отменен '</div>
            <div class="apidocs-english">Order status' Paid ',' Part. Paid ',' Postponed ',' Draft ', ' Canceled '</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
        cancellation_reason (Union[None, Unset, str]): <div class="apidocs-russian">Причина отмены заказа</div>
            <div class="apidocs-english">Order's cancellation reason</div>
        is_editable_by_device (Union[None, Unset, bool]): <div class="apidocs-russian">Возможность редактировать заказ
            на кассе  (значение по умолчанию "true")</div>
            <div class="apidocs-english">Ability to edit the order on a POS device (defaults to true)</div>
    """

    id: UUID
    number: str
    date_time: datetime.datetime
    content: "NebularApiModelsCommonApiOrderDtoContent"
    external_system: Union[None, Unset, str] = UNSET
    cashier: Union[None, UUID, Unset] = UNSET
    client_id: Union[None, UUID, Unset] = UNSET
    delivery_address: Union[None, Unset, str] = UNSET
    pick_address: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    cancellation_reason: Union[None, Unset, str] = UNSET
    is_editable_by_device: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        date_time = self.date_time.isoformat()

        content = self.content.to_dict()

        external_system: Union[None, Unset, str]
        if isinstance(self.external_system, Unset):
            external_system = UNSET
        else:
            external_system = self.external_system

        cashier: Union[None, Unset, str]
        if isinstance(self.cashier, Unset):
            cashier = UNSET
        elif isinstance(self.cashier, UUID):
            cashier = str(self.cashier)
        else:
            cashier = self.cashier

        client_id: Union[None, Unset, str]
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        elif isinstance(self.client_id, UUID):
            client_id = str(self.client_id)
        else:
            client_id = self.client_id

        delivery_address: Union[None, Unset, str]
        if isinstance(self.delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = self.delivery_address

        pick_address: Union[None, Unset, str]
        if isinstance(self.pick_address, Unset):
            pick_address = UNSET
        else:
            pick_address = self.pick_address

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        custom_properties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_properties, Unset):
            custom_properties = UNSET
        elif isinstance(self.custom_properties, list):
            custom_properties = []
            for custom_properties_type_0_item_data in self.custom_properties:
                custom_properties_type_0_item = custom_properties_type_0_item_data.to_dict()
                custom_properties.append(custom_properties_type_0_item)

        else:
            custom_properties = self.custom_properties

        cancellation_reason: Union[None, Unset, str]
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        is_editable_by_device: Union[None, Unset, bool]
        if isinstance(self.is_editable_by_device, Unset):
            is_editable_by_device = UNSET
        else:
            is_editable_by_device = self.is_editable_by_device

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "number": number,
                "dateTime": date_time,
                "content": content,
            }
        )
        if external_system is not UNSET:
            field_dict["externalSystem"] = external_system
        if cashier is not UNSET:
            field_dict["cashier"] = cashier
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if pick_address is not UNSET:
            field_dict["pickAddress"] = pick_address
        if comment is not UNSET:
            field_dict["comment"] = comment
        if status is not UNSET:
            field_dict["status"] = status
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason
        if is_editable_by_device is not UNSET:
            field_dict["isEditableByDevice"] = is_editable_by_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_order_dto_content import NebularApiModelsCommonApiOrderDtoContent
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        number = d.pop("number")

        date_time = isoparse(d.pop("dateTime"))

        content = NebularApiModelsCommonApiOrderDtoContent.from_dict(d.pop("content"))

        def _parse_external_system(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_system = _parse_external_system(d.pop("externalSystem", UNSET))

        def _parse_cashier(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cashier_type_0 = UUID(data)

                return cashier_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cashier = _parse_cashier(d.pop("cashier", UNSET))

        def _parse_client_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_id_type_0 = UUID(data)

                return client_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))

        def _parse_delivery_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_address = _parse_delivery_address(d.pop("deliveryAddress", UNSET))

        def _parse_pick_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pick_address = _parse_pick_address(d.pop("pickAddress", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_custom_properties(
            data: object,
        ) -> Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_properties_type_0 = []
                _custom_properties_type_0 = data
                for custom_properties_type_0_item_data in _custom_properties_type_0:
                    custom_properties_type_0_item = NebularApiModelsLkServiceCustomProperty.from_dict(
                        custom_properties_type_0_item_data
                    )

                    custom_properties_type_0.append(custom_properties_type_0_item)

                return custom_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]], data)

        custom_properties = _parse_custom_properties(d.pop("customProperties", UNSET))

        def _parse_cancellation_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellationReason", UNSET))

        def _parse_is_editable_by_device(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_editable_by_device = _parse_is_editable_by_device(d.pop("isEditableByDevice", UNSET))

        nebular_api_dtos_common_order_dto = cls(
            id=id,
            number=number,
            date_time=date_time,
            content=content,
            external_system=external_system,
            cashier=cashier,
            client_id=client_id,
            delivery_address=delivery_address,
            pick_address=pick_address,
            comment=comment,
            status=status,
            custom_properties=custom_properties,
            cancellation_reason=cancellation_reason,
            is_editable_by_device=is_editable_by_device,
        )

        return nebular_api_dtos_common_order_dto
