from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_device_list import NebularApiModelsLkServiceDeviceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/Devices",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceDeviceList.from_dict(response.json())

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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение всех устройств в пределах внешней
    системы</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get all external system devices</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]
    """

    kwargs = _get_kwargs(
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение всех устройств в пределах внешней
    системы</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get all external system devices</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]
    """

    return sync_detailed(
        client=client,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение всех устройств в пределах внешней
    системы</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get all external system devices</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]
    """

    kwargs = _get_kwargs(
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение всех устройств в пределах внешней
    системы</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get all external system devices</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceDeviceList]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_client_key=x_client_key,
        )
    ).parsed
