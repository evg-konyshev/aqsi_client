from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_post_cashier import NebularApiModelsLkServicePostCashier
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    cashier_id: str,
    *,
    body: Union[
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v2/Cashiers/{cashier_id}",
    }

    if isinstance(body, NebularApiModelsLkServicePostCashier):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServicePostCashier):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServicePostCashier):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cashier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление кассира для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update cashier for an external system</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        cashier_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NebularApiModelsCommonApiErrorModel]]
    """

    kwargs = _get_kwargs(
        cashier_id=cashier_id,
        body=body,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cashier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление кассира для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update cashier for an external system</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        cashier_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NebularApiModelsCommonApiErrorModel]
    """

    return sync_detailed(
        cashier_id=cashier_id,
        client=client,
        body=body,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    cashier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление кассира для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update cashier for an external system</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        cashier_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NebularApiModelsCommonApiErrorModel]]
    """

    kwargs = _get_kwargs(
        cashier_id=cashier_id,
        body=body,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cashier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
        NebularApiModelsLkServicePostCashier,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NebularApiModelsCommonApiErrorModel]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление кассира для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update cashier for an external system</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        cashier_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.
        body (NebularApiModelsLkServicePostCashier): Модель отправки данных для создания/изменения
            кассира Example: {'name': 'Vasya', 'inn': '000000000000', 'position': 'Cashier', 'pin':
            '0000', 'code': '34', 'devices': [4, 47], 'img': None, 'externalId': '1k23o3kk', 'shops':
            None, 'customProperties': [{'key': 'StaffId', 'value': 'YYY'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NebularApiModelsCommonApiErrorModel]
    """

    return (
        await asyncio_detailed(
            cashier_id=cashier_id,
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
