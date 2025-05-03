from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_dtos_get_order_status_with_receipts_content import (
    NebularApiDtosGetOrderStatusWithReceiptsContent,
)
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/Orders/simple/{order_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    if response.status_code == 200:
        response_200 = NebularApiDtosGetOrderStatusWithReceiptsContent.from_dict(response.json())

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
) -> Response[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    r"""Read

     <div class=\"apidocs-russian\"><span>Получение данных об отложенном заказе, принимает в качестве
    параметра на вход внешний id</span><br><div class=\"required-annotation\">Поля в модели запроса,
    отмеченные <span style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting pending order info. Accepts external id
    as input parameters</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2
    (V2) идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы
    заказчика), в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в
    разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        order_id (str):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    r"""Read

     <div class=\"apidocs-russian\"><span>Получение данных об отложенном заказе, принимает в качестве
    параметра на вход внешний id</span><br><div class=\"required-annotation\">Поля в модели запроса,
    отмеченные <span style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting pending order info. Accepts external id
    as input parameters</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2
    (V2) идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы
    заказчика), в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в
    разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        order_id (str):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    r"""Read

     <div class=\"apidocs-russian\"><span>Получение данных об отложенном заказе, принимает в качестве
    параметра на вход внешний id</span><br><div class=\"required-annotation\">Поля в модели запроса,
    отмеченные <span style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting pending order info. Accepts external id
    as input parameters</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2
    (V2) идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы
    заказчика), в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в
    разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        order_id (str):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]]:
    r"""Read

     <div class=\"apidocs-russian\"><span>Получение данных об отложенном заказе, принимает в качестве
    параметра на вход внешний id</span><br><div class=\"required-annotation\">Поля в модели запроса,
    отмеченные <span style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting pending order info. Accepts external id
    as input parameters</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2
    (V2) идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы
    заказчика), в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в
    разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        order_id (str):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiDtosGetOrderStatusWithReceiptsContent, NebularApiModelsCommonApiErrorModel]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            x_client_key=x_client_key,
        )
    ).parsed
