from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_lk_service_bind_device_to_account_model import (
    NebularApiModelsLkServiceBindDeviceToAccountModel,
)
from ...models.nebular_api_models_lk_service_binding_response import NebularApiModelsLkServiceBindingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/Devices/BindDeviceToAccount",
    }

    if isinstance(body, NebularApiModelsLkServiceBindDeviceToAccountModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServiceBindDeviceToAccountModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServiceBindDeviceToAccountModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, str]]:
    if response.status_code == 400:
        response_400 = cast(str, response.json())
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
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, str]]:
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
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, str]]:
    r"""GetBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceBindingResponse, str]]
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
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, str]]:
    r"""GetBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceBindingResponse, str]
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
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsLkServiceBindingResponse, str]]:
    r"""GetBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceBindingResponse, str]]
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
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
        NebularApiModelsLkServiceBindDeviceToAccountModel,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsLkServiceBindingResponse, str]]:
    r"""GetBindingToken

     <div class=\"apidocs-russian\"><span>Получение токена привязки устройства к учётной записи
    ЛК</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get binding token of the device to your
    personal computer account</div>

    Args:
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):
        body (NebularApiModelsLkServiceBindDeviceToAccountModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceBindingResponse, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
