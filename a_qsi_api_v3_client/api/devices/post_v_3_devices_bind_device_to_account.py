from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_lk_service_binding_response import NebularApiModelsLkServiceBindingResponse
from ...models.nebular_api_models_lk_service_v3_devices_v3_bind_device_to_account_model_v3 import (
    NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
)
from ...models.nebular_api_models_lk_service_v3_error_model_v3 import NebularApiModelsLkServiceV3ErrorModelV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/Devices/BindDeviceToAccount",
    }

    if isinstance(body, NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
    if response.status_code == 400:
        response_400 = NebularApiModelsLkServiceV3ErrorModelV3.from_dict(response.json())

        return response_400
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceBindingResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
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
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""CreateBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]
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
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""CreateBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]
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
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""CreateBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]
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
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
        NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""CreateBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):
        body (NebularApiModelsLkServiceV3DevicesV3BindDeviceToAccountModelV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceBindingResponse, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
