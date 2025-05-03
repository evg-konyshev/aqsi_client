import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_common_api_order_dto_extended_content import (
        NebularApiModelsCommonApiOrderDtoExtendedContent,
    )
    from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
    from ..models.nebular_api_models_receipt_models_receipt_v3 import NebularApiModelsReceiptModelsReceiptV3


T = TypeVar("T", bound="NebularApiDtosGetOrderStatusWithReceiptsContent")


@_attrs_define
class NebularApiDtosGetOrderStatusWithReceiptsContent:
    """
    Attributes:
        content (NebularApiModelsCommonApiOrderDtoExtendedContent): <div class="apidocs-russian">Содержимое
            документа</div>
            <div class="apidocs-english">Content</div>
        receipts (Union[None, Unset, list['NebularApiModelsReceiptModelsReceiptV3']]): <div class="apidocs-
            russian">Массив чеков</div>
            <div class="apidocs-english">List of receipts</div>
        number (Union[None, Unset, str]): <div class="apidocs-russian">Номер заказа с учетом префиксов</div>
            <div class="apidocs-english">Order number with prefix</div>
        external_system (Union[None, Unset, str]): <div class="apidocs-russian">Название внешней системы</div>
            <div class="apidocs-english">External system name</div>
        date_time (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Дата/Время из внешней системы</div>
            <div class="apidocs-english">Extenal system date/time</div>
        uid (Union[None, Unset, str]): <div class="apidocs-russian">Идентификатор заказа</div>
            <div class="apidocs-english">Order identifier</div>
        device (Union[None, Unset, int]): <div class="apidocs-russian">Привязанность к устройству</div>
            <div class="apidocs-english">Device binding</div>
        cashier (Union[None, UUID, Unset]): <div class="apidocs-russian">Привязанность к кассиру</div>
            <div class="apidocs-english">Cashier binding</div>
        shop (Union[None, Unset, int]): <div class="apidocs-russian">Привязанность к магазину</div>
            <div class="apidocs-english">Shop binding</div>
        status (Union[None, Unset, str]): <div class="apidocs-russian">Статус заказа 'Оплачен', 'Част. оплачен',
            'Отложен', 'Черновик', ' Отменен '</div>
            <div class="apidocs-english">Order status' Paid ',' Part. Paid ',' Postponed ',' Draft ', ' Canceled '</div>
        created_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Время создания заказа</div>
            <div class="apidocs-english">Order creation time</div>
        updated_at (Union[Unset, datetime.datetime]): <div class="apidocs-russian">Время обновления заказа</div>
            <div class="apidocs-english">Order update time</div>
        deleted_at (Union[None, Unset, datetime.datetime]): <div class="apidocs-russian">Время удаления заказа</div>
            <div class="apidocs-english">Order delete time</div>
        client_id (Union[None, UUID, Unset]): <div class="apidocs-russian">Идентификатор клиента (Если заполнен
            идентификатор клиента, то поля customerContact, customer и customerINN игнорируются)</div>
            <div class="apidocs-english">Client identifier (customerContact, customer and customerINN fields will be ignored
            if clientId field is not empty)</div>
        delivery_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес доставки заказа</div>
            <div class="apidocs-english">Delivery address</div>
        pick_address (Union[None, Unset, str]): <div class="apidocs-russian">Адрес забора заказа</div>
            <div class="apidocs-english">Order pickup address</div>
        comment (Union[None, Unset, str]): <div class="apidocs-russian">Комментарий к заказу</div>
            <div class="apidocs-english">Order comment</div>
        custom_properties (Union[None, Unset, list['NebularApiModelsLkServiceCustomProperty']]): <div class="apidocs-
            russian">Дополнительные параметры</div>
            <div class="apidocs-english">Extra options</div>
        cancellation_reason (Union[None, Unset, str]): <div class="apidocs-russian">Причина отмены заказа</div>
            <div class="apidocs-english">Order's cancellation reason</div>
        is_editable_by_device (Union[Unset, bool]): <div class="apidocs-russian">Возможность редактировать заказ на
            кассе</div>
            <div class="apidocs-english">Ability to edit the order on a POS device</div>
        ignore_item_code_check (Union[Unset, bool]): <div class="apidocs-russian">Игнорировать проверку КМ в кассе
            ОД</div>
            <div class="apidocs-english">Ignore the check of CM on a device of OD</div>
    """

    content: "NebularApiModelsCommonApiOrderDtoExtendedContent"
    receipts: Union[None, Unset, list["NebularApiModelsReceiptModelsReceiptV3"]] = UNSET
    number: Union[None, Unset, str] = UNSET
    external_system: Union[None, Unset, str] = UNSET
    date_time: Union[Unset, datetime.datetime] = UNSET
    uid: Union[None, Unset, str] = UNSET
    device: Union[None, Unset, int] = UNSET
    cashier: Union[None, UUID, Unset] = UNSET
    shop: Union[None, Unset, int] = UNSET
    status: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    client_id: Union[None, UUID, Unset] = UNSET
    delivery_address: Union[None, Unset, str] = UNSET
    pick_address: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    custom_properties: Union[None, Unset, list["NebularApiModelsLkServiceCustomProperty"]] = UNSET
    cancellation_reason: Union[None, Unset, str] = UNSET
    is_editable_by_device: Union[Unset, bool] = UNSET
    ignore_item_code_check: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        content = self.content.to_dict()

        receipts: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.receipts, Unset):
            receipts = UNSET
        elif isinstance(self.receipts, list):
            receipts = []
            for receipts_type_0_item_data in self.receipts:
                receipts_type_0_item = receipts_type_0_item_data.to_dict()
                receipts.append(receipts_type_0_item)

        else:
            receipts = self.receipts

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        external_system: Union[None, Unset, str]
        if isinstance(self.external_system, Unset):
            external_system = UNSET
        else:
            external_system = self.external_system

        date_time: Union[Unset, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        uid: Union[None, Unset, str]
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        device: Union[None, Unset, int]
        if isinstance(self.device, Unset):
            device = UNSET
        else:
            device = self.device

        cashier: Union[None, Unset, str]
        if isinstance(self.cashier, Unset):
            cashier = UNSET
        elif isinstance(self.cashier, UUID):
            cashier = str(self.cashier)
        else:
            cashier = self.cashier

        shop: Union[None, Unset, int]
        if isinstance(self.shop, Unset):
            shop = UNSET
        else:
            shop = self.shop

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

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

        is_editable_by_device = self.is_editable_by_device

        ignore_item_code_check = self.ignore_item_code_check

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "content": content,
            }
        )
        if receipts is not UNSET:
            field_dict["receipts"] = receipts
        if number is not UNSET:
            field_dict["number"] = number
        if external_system is not UNSET:
            field_dict["externalSystem"] = external_system
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if uid is not UNSET:
            field_dict["uid"] = uid
        if device is not UNSET:
            field_dict["device"] = device
        if cashier is not UNSET:
            field_dict["cashier"] = cashier
        if shop is not UNSET:
            field_dict["shop"] = shop
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if pick_address is not UNSET:
            field_dict["pickAddress"] = pick_address
        if comment is not UNSET:
            field_dict["comment"] = comment
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason
        if is_editable_by_device is not UNSET:
            field_dict["isEditableByDevice"] = is_editable_by_device
        if ignore_item_code_check is not UNSET:
            field_dict["ignoreItemCodeCheck"] = ignore_item_code_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_common_api_order_dto_extended_content import (
            NebularApiModelsCommonApiOrderDtoExtendedContent,
        )
        from ..models.nebular_api_models_lk_service_custom_property import NebularApiModelsLkServiceCustomProperty
        from ..models.nebular_api_models_receipt_models_receipt_v3 import NebularApiModelsReceiptModelsReceiptV3

        d = dict(src_dict)
        content = NebularApiModelsCommonApiOrderDtoExtendedContent.from_dict(d.pop("content"))

        def _parse_receipts(data: object) -> Union[None, Unset, list["NebularApiModelsReceiptModelsReceiptV3"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receipts_type_0 = []
                _receipts_type_0 = data
                for receipts_type_0_item_data in _receipts_type_0:
                    receipts_type_0_item = NebularApiModelsReceiptModelsReceiptV3.from_dict(receipts_type_0_item_data)

                    receipts_type_0.append(receipts_type_0_item)

                return receipts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsReceiptModelsReceiptV3"]], data)

        receipts = _parse_receipts(d.pop("receipts", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_external_system(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_system = _parse_external_system(d.pop("externalSystem", UNSET))

        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, datetime.datetime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        def _parse_uid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uid = _parse_uid(d.pop("uid", UNSET))

        def _parse_device(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

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

        def _parse_shop(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shop = _parse_shop(d.pop("shop", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

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

        is_editable_by_device = d.pop("isEditableByDevice", UNSET)

        ignore_item_code_check = d.pop("ignoreItemCodeCheck", UNSET)

        nebular_api_dtos_get_order_status_with_receipts_content = cls(
            content=content,
            receipts=receipts,
            number=number,
            external_system=external_system,
            date_time=date_time,
            uid=uid,
            device=device,
            cashier=cashier,
            shop=shop,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            client_id=client_id,
            delivery_address=delivery_address,
            pick_address=pick_address,
            comment=comment,
            custom_properties=custom_properties,
            cancellation_reason=cancellation_reason,
            is_editable_by_device=is_editable_by_device,
            ignore_item_code_check=ignore_item_code_check,
        )

        return nebular_api_dtos_get_order_status_with_receipts_content
