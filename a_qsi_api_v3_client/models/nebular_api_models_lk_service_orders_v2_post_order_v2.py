import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_order_dto_content import NebularApiModelsCommonApiOrderDtoContent


T = TypeVar("T", bound="NebularApiModelsLkServiceOrdersV2PostOrderV2")


@_attrs_define
class NebularApiModelsLkServiceOrdersV2PostOrderV2:
    """
    Example:
        {'id': 'stringId', 'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None, 'pickAddress': None,
            'status': None, 'cancellationReason': None, 'content': {'discountMoney': '0', 'discountPercent': '0', 'type': 3,
            'positions': [{'sku': '', 'id': None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0, 'barcodes': None,
            'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00', 'editable': True, 'quantity': 1, 'price': 10,
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
            None, 'settlementPlace': None, 'additionalAttribute': None, 'customer': 'Иванов Иван', 'customerINN': None,
            'customerInfo': {'birthDate': '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport':
            '00-00-000000', 'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}

    Attributes:
        id (str): <div class="apidocs-russian">Идентификатор заказа</div>
            <div class="apidocs-english">Order identifier</div>
        number (str): <div class="apidocs-russian">Номер заказа</div>
            <div class="apidocs-english">Order number</div>
        date_time (datetime.datetime): <div class="apidocs-russian">Время создания заказа</div>
            <div class="apidocs-english">Order creation time</div>
        device (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор устройства (обязателен, если не
            указаны shop и cashier, и при этом заказ не в статусе "Черновик").
                        Для заказов со статусом "Черновик"  поле необязательно.</div>
            <div class="apidocs-english">Device identifier (is required if shop and cashier values are not presented and
            status is not "Черновик" (Draft))
                        For orders with the "Черновик" (Draft) status, the field is optional.</div>
        shop (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор магазина (обязателен, если не указаны
            device и cashier, и при этом заказ не в статусе "Черновик")
                        Для заказов со статусом "Черновик"  поле необязательно.</div>
            <div class="apidocs-english">Shop identifier (is required if device and cashier values are not presented and
            status is not "Черновик" (Draft))
                        For orders with the "Черновик" (Draft) status, the field is optional.</div>
        cashier (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор кассира (обязателен, если не
            указаны shop и device, и при этом заказ не в статусе "Черновик")
                        Для заказов со статусом "Черновик"  поле необязательно.</div>
            <div class="apidocs-english">Cashier identifier (is required if shop and device values are not presented and
            status is not "Черновик" (Draft))
                        For orders with the "Черновик" (Draft) status, the field is optional.</div>
        client_id (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор клиента</div>
            <div class="apidocs-english">Customer identifier</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий к заказу</div>
            <div class="apidocs-english">Order comment</div>
        delivery_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес доставки заказа</div>
            <div class="apidocs-english">Delivery address</div>
        pick_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес забора заказа</div>
            <div class="apidocs-english">Order pickup address</div>
        status (Union[None, Unset, str]): <div class="apidocs-russian">Статус заказа, можно использовать для отмены
            заказа. По умолчанию: "Отложен". Допустимые значения: "Отложен", "Отменен", "Черновик", "Возвращен", "Частично
            возвращен".
                        При статусе заказа "Черновик" поля device, cashier, shop необязательны.</div>
            <div class="apidocs-english">Order status, can be utilized to cancel the order. Default: "Отложен"(Deferred).
            Possible values: "Отложен" (Deferred), "Отменен" (Canceled),
                        "Черновик" (Draft), "Возвращен" (Returned), "Частично возвращен" (Partial returned). If the status
            is draft, the cashier, shop and device fields are optional</div>
        cancellation_reason (Union[None, Unset, str]): <div class="apidocs-russian">Причина отмены заказа (заполняется,
            если указан статус заказа "Отменен")</div>
            <div class="apidocs-english">Order cancellation reason (fill in if status value is "Отменен"(Canceled))</div>
        content (Union['NebularApiModelsCommonApiOrderDtoContent', None, Unset]): <div class="apidocs-
            russian">Содержимое заказа</div>
            <div class="apidocs-english">Order content</div>
        is_editable_by_device (Union[Unset, bool]): <div class="apidocs-russian">Возможность редактировать заказ на
            кассе. По умолчанию: true</div>
            <div class="apidocs-english">Ability to change order on POS-device. Default: true</div>
        ignore_item_code_check (Union[Unset, bool]): <div class="apidocs-russian">Игнорировать проверку КМ в кассе
            ОД</div>
            <div class="apidocs-english">Ignore the check of CM on a device of OD</div>
    """

    id: str
    number: str
    date_time: datetime.datetime
    device: Union[None, Unset, str] = UNSET
    shop: Union[None, Unset, str] = UNSET
    cashier: Union[None, Unset, str] = UNSET
    client_id: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    delivery_address: Union[None, Unset, str] = UNSET
    pick_address: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    cancellation_reason: Union[None, Unset, str] = UNSET
    content: Union["NebularApiModelsCommonApiOrderDtoContent", None, Unset] = UNSET
    is_editable_by_device: Union[Unset, bool] = UNSET
    ignore_item_code_check: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.nebular_api_models_common_api_order_dto_content import NebularApiModelsCommonApiOrderDtoContent

        id = self.id

        number = self.number

        date_time = self.date_time.isoformat()

        device: Union[None, Unset, str]
        if isinstance(self.device, Unset):
            device = UNSET
        else:
            device = self.device

        shop: Union[None, Unset, str]
        if isinstance(self.shop, Unset):
            shop = UNSET
        else:
            shop = self.shop

        cashier: Union[None, Unset, str]
        if isinstance(self.cashier, Unset):
            cashier = UNSET
        else:
            cashier = self.cashier

        client_id: Union[None, Unset, str]
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

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

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        cancellation_reason: Union[None, Unset, str]
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        content: Union[None, Unset, dict[str, Any]]
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, NebularApiModelsCommonApiOrderDtoContent):
            content = self.content.to_dict()
        else:
            content = self.content

        is_editable_by_device = self.is_editable_by_device

        ignore_item_code_check = self.ignore_item_code_check

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "number": number,
                "dateTime": date_time,
            }
        )
        if device is not UNSET:
            field_dict["device"] = device
        if shop is not UNSET:
            field_dict["shop"] = shop
        if cashier is not UNSET:
            field_dict["cashier"] = cashier
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if pick_address is not UNSET:
            field_dict["pickAddress"] = pick_address
        if status is not UNSET:
            field_dict["status"] = status
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason
        if content is not UNSET:
            field_dict["content"] = content
        if is_editable_by_device is not UNSET:
            field_dict["isEditableByDevice"] = is_editable_by_device
        if ignore_item_code_check is not UNSET:
            field_dict["ignoreItemCodeCheck"] = ignore_item_code_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_order_dto_content import NebularApiModelsCommonApiOrderDtoContent

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        date_time = isoparse(d.pop("dateTime"))

        def _parse_device(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_shop(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop = _parse_shop(d.pop("shop", UNSET))

        def _parse_cashier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cashier = _parse_cashier(d.pop("cashier", UNSET))

        def _parse_client_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

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

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_cancellation_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellationReason", UNSET))

        def _parse_content(data: object) -> Union["NebularApiModelsCommonApiOrderDtoContent", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = NebularApiModelsCommonApiOrderDtoContent.from_dict(data)

                return content_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NebularApiModelsCommonApiOrderDtoContent", None, Unset], data)

        content = _parse_content(d.pop("content", UNSET))

        is_editable_by_device = d.pop("isEditableByDevice", UNSET)

        ignore_item_code_check = d.pop("ignoreItemCodeCheck", UNSET)

        nebular_api_models_lk_service_orders_v2_post_order_v2 = cls(
            id=id,
            number=number,
            date_time=date_time,
            device=device,
            shop=shop,
            cashier=cashier,
            client_id=client_id,
            comment=comment,
            delivery_address=delivery_address,
            pick_address=pick_address,
            status=status,
            cancellation_reason=cancellation_reason,
            content=content,
            is_editable_by_device=is_editable_by_device,
            ignore_item_code_check=ignore_item_code_check,
        )

        return nebular_api_models_lk_service_orders_v2_post_order_v2
