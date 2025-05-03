from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_common_api_guid_model import NebularApiModelsCommonApiGuidModel
from ...models.nebular_api_models_lk_service_orders_v2_post_order_v2 import NebularApiModelsLkServiceOrdersV2PostOrderV2
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/Orders/simple",
    }

    if isinstance(body, NebularApiModelsLkServiceOrdersV2PostOrderV2):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServiceOrdersV2PostOrderV2):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServiceOrdersV2PostOrderV2):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    if response.status_code == 201:
        response_201 = NebularApiModelsCommonApiGuidModel.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = NebularApiModelsCommonApiErrorModel.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = NebularApiModelsCommonApiErrorModel.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Create

     <div class=\"apidocs-russian\"><span>Создание и обновление отложенного заказа.</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Create new or update existing pending order.</div><br/><div class=\"apidocs-russian
    version-annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта
    (используются идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где
    использовались идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Create

     <div class=\"apidocs-russian\"><span>Создание и обновление отложенного заказа.</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Create new or update existing pending order.</div><br/><div class=\"apidocs-russian
    version-annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта
    (используются идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где
    использовались идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Create

     <div class=\"apidocs-russian\"><span>Создание и обновление отложенного заказа.</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Create new or update existing pending order.</div><br/><div class=\"apidocs-russian
    version-annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта
    (используются идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где
    использовались идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
        NebularApiModelsLkServiceOrdersV2PostOrderV2,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Create

     <div class=\"apidocs-russian\"><span>Создание и обновление отложенного заказа.</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Create new or update existing pending order.</div><br/><div class=\"apidocs-russian
    version-annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта
    (используются идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где
    использовались идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.
        body (NebularApiModelsLkServiceOrdersV2PostOrderV2):  Example: {'id': 'stringId',
            'number': 'OderNumber', 'dateTime': '2019-08-14T12:15:43.0000000+00:00', 'device': None,
            'shop': None, 'cashier': None, 'clientId': None, 'comment': None, 'deliveryAddress': None,
            'pickAddress': None, 'status': None, 'cancellationReason': None, 'content':
            {'discountMoney': '0', 'discountPercent': '0', 'type': 3, 'positions': [{'sku': '', 'id':
            None, 'discountMoney': 0, 'positionId': '00000000-0000-0000-0000-000000000000',
            'markingType': None, 'nomenclatureCode': None, 'itemCode': None, 'soldAmount': 0,
            'barcodes': None, 'addingType': 0, 'addedAt': '2025-04-29T20:13:37.6005649+00:00',
            'editable': True, 'quantity': 1, 'price': 10, 'tax': 6, 'text': 'Договор страхования
            №ARS15/123474', 'paymentMethodType': 4, 'paymentSubjectType': 4, 'agentInfo': None,
            'unitOfMeasurement': 'Piece', 'unitCode': 0, 'additionalAttribute': None,
            'manufacturerCountryCode': None, 'customsDeclarationNumber': None, 'supplierINN': None,
            'supplierInfo': None, 'excise': None, 'agentType': None, 'customProperties': None,
            'industryAttribute': None, 'noReturn': 0, 'discountPercent': '0', 'maxDiscountPercent':
            '0', 'minPrice': '0', 'isWeight': 0}], 'checkClose': {'payments': [{'acquiringData': None,
            'processedAt': None, 'index': None, 'parentIndex': None, 'type': 1, 'amount': 10}],
            'taxationSystem': 0}, 'customerContact': 'Иванов Иван', 'paymentAgentOperation': None,
            'paymentOperatorName': None, 'paymentOperatorAddress': None, 'paymentOperatorINN': None,
            'agentType': None, 'paymentTransferOperatorPhoneNumbers': None,
            'paymentAgentPhoneNumbers': None, 'paymentOperatorPhoneNumbers': None,
            'supplierPhoneNumbers': None, 'additionalUserAttribute': None, 'automatNumber': None,
            'settlementAddress': None, 'settlementPlace': None, 'additionalAttribute': None,
            'customer': 'Иванов Иван', 'customerINN': None, 'customerInfo': {'birthDate':
            '1980-01-01', 'nationality': 'Национальность', 'docType': 21, 'passport': '00-00-000000',
            'address': 'город, улица, дом'}, 'industryAttribute': None, 'electronicCheck': None},
            'isEditableByDevice': False, 'ignoreItemCodeCheck': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
