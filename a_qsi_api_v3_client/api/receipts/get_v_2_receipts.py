import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_receipt_type_enum import NebularApiModelsLkServiceReceiptTypeEnum
from ...models.nebular_api_models_lk_service_receipts_v2_receipts_response_v2 import (
    NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2,
)
from ...models.nebular_api_models_lk_service_sorting import NebularApiModelsLkServiceSorting
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filtered_operation: Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_order: Union[Unset, str] = UNSET,
    filtered_client: Union[Unset, UUID] = UNSET,
    filtered_shops: Union[Unset, list[int]] = UNSET,
    filtered_fd: Union[Unset, str] = UNSET,
    filtered_fp: Union[Unset, str] = UNSET,
    filtered_product_name: Union[Unset, str] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_begin_date: datetime.datetime,
    filtered_end_date: Union[Unset, datetime.datetime] = UNSET,
    filtered_devices: Union[Unset, list[int]] = UNSET,
    filtered_cashiers: Union[Unset, list[UUID]] = UNSET,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    params: dict[str, Any] = {}

    json_filtered_operation: Union[Unset, int] = UNSET
    if not isinstance(filtered_operation, Unset):
        json_filtered_operation = filtered_operation.value

    params["filtered.operation"] = json_filtered_operation

    params["filtered.search"] = filtered_search

    params["filtered.order"] = filtered_order

    json_filtered_client: Union[Unset, str] = UNSET
    if not isinstance(filtered_client, Unset):
        json_filtered_client = str(filtered_client)
    params["filtered.client"] = json_filtered_client

    json_filtered_shops: Union[Unset, list[int]] = UNSET
    if not isinstance(filtered_shops, Unset):
        json_filtered_shops = filtered_shops

    params["filtered.shops"] = json_filtered_shops

    params["filtered.fd"] = filtered_fd

    params["filtered.fp"] = filtered_fp

    params["filtered.productName"] = filtered_product_name

    params["filtered.beginAmount"] = filtered_begin_amount

    params["filtered.endAmount"] = filtered_end_amount

    json_filtered_begin_date = filtered_begin_date.isoformat()
    params["filtered.beginDate"] = json_filtered_begin_date

    json_filtered_end_date: Union[Unset, str] = UNSET
    if not isinstance(filtered_end_date, Unset):
        json_filtered_end_date = filtered_end_date.isoformat()
    params["filtered.endDate"] = json_filtered_end_date

    json_filtered_devices: Union[Unset, list[int]] = UNSET
    if not isinstance(filtered_devices, Unset):
        json_filtered_devices = filtered_devices

    params["filtered.devices"] = json_filtered_devices

    json_filtered_cashiers: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_cashiers, Unset):
        json_filtered_cashiers = []
        for filtered_cashiers_item_data in filtered_cashiers:
            filtered_cashiers_item = str(filtered_cashiers_item_data)
            json_filtered_cashiers.append(filtered_cashiers_item)

    params["filtered.cashiers"] = json_filtered_cashiers

    params["pageSize"] = page_size

    params["page"] = page

    json_sorted_: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(sorted_, Unset):
        json_sorted_ = []
        for sorted_item_data in sorted_:
            sorted_item = sorted_item_data.to_dict()
            json_sorted_.append(sorted_item)

    params["sorted"] = json_sorted_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/Receipts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2.from_dict(response.json())

        return response_200
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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filtered_operation: Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_order: Union[Unset, str] = UNSET,
    filtered_client: Union[Unset, UUID] = UNSET,
    filtered_shops: Union[Unset, list[int]] = UNSET,
    filtered_fd: Union[Unset, str] = UNSET,
    filtered_fp: Union[Unset, str] = UNSET,
    filtered_product_name: Union[Unset, str] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_begin_date: datetime.datetime,
    filtered_end_date: Union[Unset, datetime.datetime] = UNSET,
    filtered_devices: Union[Unset, list[int]] = UNSET,
    filtered_cashiers: Union[Unset, list[UUID]] = UNSET,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка чеков</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-english\">Get
    receipts list</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        filtered_operation (Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum]):
        filtered_search (Union[Unset, str]):
        filtered_order (Union[Unset, str]):
        filtered_client (Union[Unset, UUID]):
        filtered_shops (Union[Unset, list[int]]):
        filtered_fd (Union[Unset, str]):
        filtered_fp (Union[Unset, str]):
        filtered_product_name (Union[Unset, str]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_begin_date (datetime.datetime):
        filtered_end_date (Union[Unset, datetime.datetime]):
        filtered_devices (Union[Unset, list[int]]):
        filtered_cashiers (Union[Unset, list[UUID]]):
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]
    """

    kwargs = _get_kwargs(
        filtered_operation=filtered_operation,
        filtered_search=filtered_search,
        filtered_order=filtered_order,
        filtered_client=filtered_client,
        filtered_shops=filtered_shops,
        filtered_fd=filtered_fd,
        filtered_fp=filtered_fp,
        filtered_product_name=filtered_product_name,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_begin_date=filtered_begin_date,
        filtered_end_date=filtered_end_date,
        filtered_devices=filtered_devices,
        filtered_cashiers=filtered_cashiers,
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filtered_operation: Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_order: Union[Unset, str] = UNSET,
    filtered_client: Union[Unset, UUID] = UNSET,
    filtered_shops: Union[Unset, list[int]] = UNSET,
    filtered_fd: Union[Unset, str] = UNSET,
    filtered_fp: Union[Unset, str] = UNSET,
    filtered_product_name: Union[Unset, str] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_begin_date: datetime.datetime,
    filtered_end_date: Union[Unset, datetime.datetime] = UNSET,
    filtered_devices: Union[Unset, list[int]] = UNSET,
    filtered_cashiers: Union[Unset, list[UUID]] = UNSET,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка чеков</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-english\">Get
    receipts list</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        filtered_operation (Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum]):
        filtered_search (Union[Unset, str]):
        filtered_order (Union[Unset, str]):
        filtered_client (Union[Unset, UUID]):
        filtered_shops (Union[Unset, list[int]]):
        filtered_fd (Union[Unset, str]):
        filtered_fp (Union[Unset, str]):
        filtered_product_name (Union[Unset, str]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_begin_date (datetime.datetime):
        filtered_end_date (Union[Unset, datetime.datetime]):
        filtered_devices (Union[Unset, list[int]]):
        filtered_cashiers (Union[Unset, list[UUID]]):
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]
    """

    return sync_detailed(
        client=client,
        filtered_operation=filtered_operation,
        filtered_search=filtered_search,
        filtered_order=filtered_order,
        filtered_client=filtered_client,
        filtered_shops=filtered_shops,
        filtered_fd=filtered_fd,
        filtered_fp=filtered_fp,
        filtered_product_name=filtered_product_name,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_begin_date=filtered_begin_date,
        filtered_end_date=filtered_end_date,
        filtered_devices=filtered_devices,
        filtered_cashiers=filtered_cashiers,
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filtered_operation: Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_order: Union[Unset, str] = UNSET,
    filtered_client: Union[Unset, UUID] = UNSET,
    filtered_shops: Union[Unset, list[int]] = UNSET,
    filtered_fd: Union[Unset, str] = UNSET,
    filtered_fp: Union[Unset, str] = UNSET,
    filtered_product_name: Union[Unset, str] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_begin_date: datetime.datetime,
    filtered_end_date: Union[Unset, datetime.datetime] = UNSET,
    filtered_devices: Union[Unset, list[int]] = UNSET,
    filtered_cashiers: Union[Unset, list[UUID]] = UNSET,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка чеков</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-english\">Get
    receipts list</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        filtered_operation (Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum]):
        filtered_search (Union[Unset, str]):
        filtered_order (Union[Unset, str]):
        filtered_client (Union[Unset, UUID]):
        filtered_shops (Union[Unset, list[int]]):
        filtered_fd (Union[Unset, str]):
        filtered_fp (Union[Unset, str]):
        filtered_product_name (Union[Unset, str]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_begin_date (datetime.datetime):
        filtered_end_date (Union[Unset, datetime.datetime]):
        filtered_devices (Union[Unset, list[int]]):
        filtered_cashiers (Union[Unset, list[UUID]]):
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]
    """

    kwargs = _get_kwargs(
        filtered_operation=filtered_operation,
        filtered_search=filtered_search,
        filtered_order=filtered_order,
        filtered_client=filtered_client,
        filtered_shops=filtered_shops,
        filtered_fd=filtered_fd,
        filtered_fp=filtered_fp,
        filtered_product_name=filtered_product_name,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_begin_date=filtered_begin_date,
        filtered_end_date=filtered_end_date,
        filtered_devices=filtered_devices,
        filtered_cashiers=filtered_cashiers,
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filtered_operation: Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_order: Union[Unset, str] = UNSET,
    filtered_client: Union[Unset, UUID] = UNSET,
    filtered_shops: Union[Unset, list[int]] = UNSET,
    filtered_fd: Union[Unset, str] = UNSET,
    filtered_fp: Union[Unset, str] = UNSET,
    filtered_product_name: Union[Unset, str] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_begin_date: datetime.datetime,
    filtered_end_date: Union[Unset, datetime.datetime] = UNSET,
    filtered_devices: Union[Unset, list[int]] = UNSET,
    filtered_cashiers: Union[Unset, list[UUID]] = UNSET,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка чеков</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-english\">Get
    receipts list</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        filtered_operation (Union[Unset, NebularApiModelsLkServiceReceiptTypeEnum]):
        filtered_search (Union[Unset, str]):
        filtered_order (Union[Unset, str]):
        filtered_client (Union[Unset, UUID]):
        filtered_shops (Union[Unset, list[int]]):
        filtered_fd (Union[Unset, str]):
        filtered_fp (Union[Unset, str]):
        filtered_product_name (Union[Unset, str]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_begin_date (datetime.datetime):
        filtered_end_date (Union[Unset, datetime.datetime]):
        filtered_devices (Union[Unset, list[int]]):
        filtered_cashiers (Union[Unset, list[UUID]]):
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceReceiptsV2ReceiptsResponseV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            filtered_operation=filtered_operation,
            filtered_search=filtered_search,
            filtered_order=filtered_order,
            filtered_client=filtered_client,
            filtered_shops=filtered_shops,
            filtered_fd=filtered_fd,
            filtered_fp=filtered_fp,
            filtered_product_name=filtered_product_name,
            filtered_begin_amount=filtered_begin_amount,
            filtered_end_amount=filtered_end_amount,
            filtered_begin_date=filtered_begin_date,
            filtered_end_date=filtered_end_date,
            filtered_devices=filtered_devices,
            filtered_cashiers=filtered_cashiers,
            page_size=page_size,
            page=page,
            sorted_=sorted_,
            x_client_key=x_client_key,
        )
    ).parsed
