from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    guid: UUID,
    *,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/ListGoods/{guid}/status",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Bulk Upsert Status

     <div class=\"apidocs-russian\"><span>Получение статуса загрузки пачки сообщений для товаров по
    идентификатору</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get goods batch message  status by
    identifier</div>

    Args:
        guid (UUID):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        guid=guid,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Bulk Upsert Status

     <div class=\"apidocs-russian\"><span>Получение статуса загрузки пачки сообщений для товаров по
    идентификатору</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get goods batch message  status by
    identifier</div>

    Args:
        guid (UUID):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        guid=guid,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
