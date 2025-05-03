from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_goods_rows_2_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e_system_string_system_private_core_lib_version_6000_cultureneutral_public_key_token_7_cec_85d7_bea_7798e import (
    NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: Union[Unset, int] = 0,
    group_id: Union[Unset, str] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["group_id"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/Goods/list",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E.from_dict(
            response.json()
        )

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
) -> Response[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_number: Union[Unset, int] = 0,
    group_id: Union[Unset, str] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товаров из личного кабинета в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting external system account-wide list of
    goods</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_number (Union[Unset, int]):  Default: 0.
        group_id (Union[Unset, str]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        group_id=group_id,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_number: Union[Unset, int] = 0,
    group_id: Union[Unset, str] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товаров из личного кабинета в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting external system account-wide list of
    goods</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_number (Union[Unset, int]):  Default: 0.
        group_id (Union[Unset, str]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E]
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        group_id=group_id,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_number: Union[Unset, int] = 0,
    group_id: Union[Unset, str] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товаров из личного кабинета в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting external system account-wide list of
    goods</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_number (Union[Unset, int]):  Default: 0.
        group_id (Union[Unset, str]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E]]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        group_id=group_id,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_number: Union[Unset, int] = 0,
    group_id: Union[Unset, str] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        NebularApiModelsCommonApiErrorModel,
        NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E,
    ]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товаров из личного кабинета в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Getting external system account-wide list of
    goods</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        page_number (Union[Unset, int]):  Default: 0.
        group_id (Union[Unset, str]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsLkServiceGoodsRows2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798ESystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7Cec85D7Bea7798E]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_number=page_number,
            group_id=group_id,
            x_client_key=x_client_key,
        )
    ).parsed
