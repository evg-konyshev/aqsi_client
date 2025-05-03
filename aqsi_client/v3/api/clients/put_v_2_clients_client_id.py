from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_client import NebularApiModelsLkServiceClient
from ...models.nebular_api_models_lk_service_id_response_v2 import NebularApiModelsLkServiceIdResponseV2
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    client_id: str,
    *,
    body: Union[
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v2/Clients/{client_id}",
    }

    if isinstance(body, NebularApiModelsLkServiceClient):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, NebularApiModelsLkServiceClient):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NebularApiModelsLkServiceClient):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceIdResponseV2.from_dict(response.json())

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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление клиента для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update external system client</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        client_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        body=body,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление клиента для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update external system client</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        client_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
        body=body,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление клиента для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update external system client</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        client_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        body=body,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
        NebularApiModelsLkServiceClient,
    ],
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]]:
    r"""Update

     <div class=\"apidocs-russian\"><span>Обновление клиента для внешней системы</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Update external system client</div><br/><div class=\"apidocs-russian version-
    annotation\">В методах версии 2 (V2) идентификаторы уникальны в разрезе аккаунта (используются
    идентификаторы внешней системы заказчика), в отличие от методов версии 1 (V1), где использовались
    идентификаторы уникальные в разрезе всей системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        client_id (str):
        x_client_key (Union[Unset, str]):
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.
        body (NebularApiModelsLkServiceClient):  Example: {'group': {'id':
            '00000000-0000-0000-0000-000000000000'}, 'fio': 'Иванов Иван', 'gender': 1, 'inn':
            '123124125126', 'birthDate': '1970-01-01T00:00:00.0000000+00:00', 'mainPhone':
            '88005553535', 'additionalPhone': None, 'email': 'ivanov@example.com', 'comment':
            'Оставляет чаевые', 'passport': '4608999777', 'docType': None, 'nationality': None,
            'address': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceIdResponseV2]
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
