from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_orders_v2_orders_response import (
    NebularApiModelsLkServiceOrdersV2OrdersResponse,
)
from ...models.nebular_api_models_lk_service_sorting import NebularApiModelsLkServiceSorting
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_clients: Union[Unset, list[UUID]] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_date_from: str,
    filtered_date_to: Union[Unset, str] = UNSET,
    filtered_status: Union[Unset, list[str]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["page"] = page

    json_sorted_: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(sorted_, Unset):
        json_sorted_ = []
        for sorted_item_data in sorted_:
            sorted_item = sorted_item_data.to_dict()
            json_sorted_.append(sorted_item)

    params["sorted"] = json_sorted_

    params["filtered.search"] = filtered_search

    json_filtered_clients: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_clients, Unset):
        json_filtered_clients = []
        for filtered_clients_item_data in filtered_clients:
            filtered_clients_item = str(filtered_clients_item_data)
            json_filtered_clients.append(filtered_clients_item)

    params["filtered.clients"] = json_filtered_clients

    params["filtered.beginAmount"] = filtered_begin_amount

    params["filtered.endAmount"] = filtered_end_amount

    params["filtered.dateFrom"] = filtered_date_from

    params["filtered.dateTo"] = filtered_date_to

    json_filtered_status: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_status, Unset):
        json_filtered_status = filtered_status

    params["filtered.status"] = json_filtered_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/Orders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceOrdersV2OrdersResponse.from_dict(response.json())

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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_clients: Union[Unset, list[UUID]] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_date_from: str,
    filtered_date_to: Union[Unset, str] = UNSET,
    filtered_status: Union[Unset, list[str]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка отложенных заказов</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Getting list of pending orders</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        filtered_search (Union[Unset, str]):
        filtered_clients (Union[Unset, list[UUID]]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_date_from (str):
        filtered_date_to (Union[Unset, str]):
        filtered_status (Union[Unset, list[str]]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        filtered_search=filtered_search,
        filtered_clients=filtered_clients,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_date_from=filtered_date_from,
        filtered_date_to=filtered_date_to,
        filtered_status=filtered_status,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_clients: Union[Unset, list[UUID]] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_date_from: str,
    filtered_date_to: Union[Unset, str] = UNSET,
    filtered_status: Union[Unset, list[str]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка отложенных заказов</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Getting list of pending orders</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        filtered_search (Union[Unset, str]):
        filtered_clients (Union[Unset, list[UUID]]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_date_from (str):
        filtered_date_to (Union[Unset, str]):
        filtered_status (Union[Unset, list[str]]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        filtered_search=filtered_search,
        filtered_clients=filtered_clients,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_date_from=filtered_date_from,
        filtered_date_to=filtered_date_to,
        filtered_status=filtered_status,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_clients: Union[Unset, list[UUID]] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_date_from: str,
    filtered_date_to: Union[Unset, str] = UNSET,
    filtered_status: Union[Unset, list[str]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка отложенных заказов</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Getting list of pending orders</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        filtered_search (Union[Unset, str]):
        filtered_clients (Union[Unset, list[UUID]]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_date_from (str):
        filtered_date_to (Union[Unset, str]):
        filtered_status (Union[Unset, list[str]]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        sorted_=sorted_,
        filtered_search=filtered_search,
        filtered_clients=filtered_clients,
        filtered_begin_amount=filtered_begin_amount,
        filtered_end_amount=filtered_end_amount,
        filtered_date_from=filtered_date_from,
        filtered_date_to=filtered_date_to,
        filtered_status=filtered_status,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 0,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceSorting"]] = UNSET,
    filtered_search: Union[Unset, str] = UNSET,
    filtered_clients: Union[Unset, list[UUID]] = UNSET,
    filtered_begin_amount: Union[Unset, str] = UNSET,
    filtered_end_amount: Union[Unset, str] = UNSET,
    filtered_date_from: str,
    filtered_date_to: Union[Unset, str] = UNSET,
    filtered_status: Union[Unset, list[str]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка отложенных заказов</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Getting list of pending orders</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 0.
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceSorting']]):
        filtered_search (Union[Unset, str]):
        filtered_clients (Union[Unset, list[UUID]]):
        filtered_begin_amount (Union[Unset, str]):
        filtered_end_amount (Union[Unset, str]):
        filtered_date_from (str):
        filtered_date_to (Union[Unset, str]):
        filtered_status (Union[Unset, list[str]]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceOrdersV2OrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page=page,
            sorted_=sorted_,
            filtered_search=filtered_search,
            filtered_clients=filtered_clients,
            filtered_begin_amount=filtered_begin_amount,
            filtered_end_amount=filtered_end_amount,
            filtered_date_from=filtered_date_from,
            filtered_date_to=filtered_date_to,
            filtered_status=filtered_status,
            x_client_key=x_client_key,
        )
    ).parsed
