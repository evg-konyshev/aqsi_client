from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_lk_service_get_goods_category_v2 import NebularApiModelsLkServiceGetGoodsCategoryV2
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
        "url": "/v2/GoodsCategory/list",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NebularApiModelsLkServiceGetGoodsCategoryV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
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
) -> Response[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товарных категорий в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get a list of good's categories by
    account</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, list['NebularApiModelsLkServiceGetGoodsCategoryV2']]]
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
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товарных категорий в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get a list of good's categories by
    account</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, list['NebularApiModelsLkServiceGetGoodsCategoryV2']]
    """

    return sync_detailed(
        client=client,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товарных категорий в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get a list of good's categories by
    account</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, list['NebularApiModelsLkServiceGetGoodsCategoryV2']]]
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
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, list["NebularApiModelsLkServiceGetGoodsCategoryV2"]]]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка товарных категорий в разрезе
    аккаунта</span><br><div class=\"required-annotation\">Поля в модели запроса, отмеченные <span
    style=\"color: red; font-weight: normal;\">required</span> - обязательны к
    заполнению</div></div><div class=\"apidocs-english\">Get a list of good's categories by
    account</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div>

    Args:
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, list['NebularApiModelsLkServiceGetGoodsCategoryV2']]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_client_key=x_client_key,
        )
    ).parsed
