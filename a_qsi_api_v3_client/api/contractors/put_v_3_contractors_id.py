from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_lk_service_v3_contractors_v3_update_contractor_request_v3 import (
    NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
)
from ...models.nebular_api_models_lk_service_v3_error_model_v3 import NebularApiModelsLkServiceV3ErrorModelV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v3/Contractors/{id}",
    }

    if isinstance(body, NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = NebularApiModelsLkServiceV3ErrorModelV3.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = NebularApiModelsLkServiceV3ErrorModelV3.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление контрагента</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update contractor</div>

    Args:
        id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление контрагента</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update contractor</div>

    Args:
        id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление контрагента</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update contractor</div>

    Args:
        id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
        NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление контрагента</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update contractor</div>

    Args:
        id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):
        body (NebularApiModelsLkServiceV3ContractorsV3UpdateContractorRequestV3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
