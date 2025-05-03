from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_models_common_api_error_model import NebularApiModelsCommonApiErrorModel
from ...models.nebular_api_models_common_api_guid_model import NebularApiModelsCommonApiGuidModel
from ...models.post_v2_shops_prices_body import PostV2ShopsPricesBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV2ShopsPricesBody,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/ShopsPrices",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    if response.status_code == 200:
        response_200 = NebularApiModelsCommonApiGuidModel.from_dict(response.text)

        return response_200
    if response.status_code == 400:
        response_400 = NebularApiModelsCommonApiErrorModel.from_dict(response.text)

        return response_400
    if response.status_code == 500:
        response_500 = NebularApiModelsCommonApiErrorModel.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostV2ShopsPricesBody,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Set Prices

     <div class=\"apidocs-russian\"><span>Отправка GZip архива товаров,в ответе возвращается время
    постановки сообщения в очередь на шину данных Архивированный файл должен содеражть Json, состоящий
    из полей: payload - PostSetShopPrices[] (Массив структур, соответствующих модели сущности) nonAtomic
    - bool Признак необходимости обрабатывать элементы массива `payload` по отдельности. При
    возникновении ошибки для одной из записей(например, товар не найден в бд), операция не завершалась с
    ошибкой, а эта ошибка добавлялась в массив ошибок, а все сущности, для которых ошибок не возникло,
    успешно обновились.(Значение по умолчанию `false`.)</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Sending goods GZIP archive.  Response returns data bus message queuing timestamp. The
    archived file must be a Json, containing fields: payload - PostSetShopPrices [] (An array of
    structures corresponding to the entity model) nonAtomic - bool (Indicates whether to process payload
    array elements separately. If an error occures for one of the records (for example, the product has
    not been found in database), the operation would not complete with an error, this error would be
    added to the errors array, all other entities would be updated properly  (The default value is
    `false`.)</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div> Sample json:

                   POST /ShopsPrices
                   {
                     \"payload\": [
                            {
                             \"id\": \"YOUR_SHOP_ID_V2\",
                             \"goods\": [
                                 {
                                     \"id\": \"YOUR_GOOD_V2_ID\",
                                     \"price\": 111,
                                     \"maxDiscountPercent\": 9
                                 },
                                 {
                                     \"id\": \"RGFFE2354\",
                                     \"price\": 222,
                                     \"maxDiscountPercent\": 14
                                 }
                             ]
                         },
                         {
                         \"goods\": [
                             {
                                     \"id\": \"SOME_GOOD_V2_ID\",
                                     \"price\": 99.99,
                                     \"maxDiscountPercent\": 0
                             },
                             {
                                     \"id\": \"ANOTHER_GOOD_V2_ID\",
                                     \"maxDiscountPercent\": 12,
                                     \"price\": 88
                             }
                             ]
                         }
                     ],
                     \"nonAtomic\": false
                   }

    Args:
        x_client_key (Union[Unset, str]):
        body (PostV2ShopsPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]
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
    body: PostV2ShopsPricesBody,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Set Prices

     <div class=\"apidocs-russian\"><span>Отправка GZip архива товаров,в ответе возвращается время
    постановки сообщения в очередь на шину данных Архивированный файл должен содеражть Json, состоящий
    из полей: payload - PostSetShopPrices[] (Массив структур, соответствующих модели сущности) nonAtomic
    - bool Признак необходимости обрабатывать элементы массива `payload` по отдельности. При
    возникновении ошибки для одной из записей(например, товар не найден в бд), операция не завершалась с
    ошибкой, а эта ошибка добавлялась в массив ошибок, а все сущности, для которых ошибок не возникло,
    успешно обновились.(Значение по умолчанию `false`.)</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Sending goods GZIP archive.  Response returns data bus message queuing timestamp. The
    archived file must be a Json, containing fields: payload - PostSetShopPrices [] (An array of
    structures corresponding to the entity model) nonAtomic - bool (Indicates whether to process payload
    array elements separately. If an error occures for one of the records (for example, the product has
    not been found in database), the operation would not complete with an error, this error would be
    added to the errors array, all other entities would be updated properly  (The default value is
    `false`.)</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div> Sample json:

                   POST /ShopsPrices
                   {
                     \"payload\": [
                            {
                             \"id\": \"YOUR_SHOP_ID_V2\",
                             \"goods\": [
                                 {
                                     \"id\": \"YOUR_GOOD_V2_ID\",
                                     \"price\": 111,
                                     \"maxDiscountPercent\": 9
                                 },
                                 {
                                     \"id\": \"RGFFE2354\",
                                     \"price\": 222,
                                     \"maxDiscountPercent\": 14
                                 }
                             ]
                         },
                         {
                         \"goods\": [
                             {
                                     \"id\": \"SOME_GOOD_V2_ID\",
                                     \"price\": 99.99,
                                     \"maxDiscountPercent\": 0
                             },
                             {
                                     \"id\": \"ANOTHER_GOOD_V2_ID\",
                                     \"maxDiscountPercent\": 12,
                                     \"price\": 88
                             }
                             ]
                         }
                     ],
                     \"nonAtomic\": false
                   }

    Args:
        x_client_key (Union[Unset, str]):
        body (PostV2ShopsPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostV2ShopsPricesBody,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Set Prices

     <div class=\"apidocs-russian\"><span>Отправка GZip архива товаров,в ответе возвращается время
    постановки сообщения в очередь на шину данных Архивированный файл должен содеражть Json, состоящий
    из полей: payload - PostSetShopPrices[] (Массив структур, соответствующих модели сущности) nonAtomic
    - bool Признак необходимости обрабатывать элементы массива `payload` по отдельности. При
    возникновении ошибки для одной из записей(например, товар не найден в бд), операция не завершалась с
    ошибкой, а эта ошибка добавлялась в массив ошибок, а все сущности, для которых ошибок не возникло,
    успешно обновились.(Значение по умолчанию `false`.)</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Sending goods GZIP archive.  Response returns data bus message queuing timestamp. The
    archived file must be a Json, containing fields: payload - PostSetShopPrices [] (An array of
    structures corresponding to the entity model) nonAtomic - bool (Indicates whether to process payload
    array elements separately. If an error occures for one of the records (for example, the product has
    not been found in database), the operation would not complete with an error, this error would be
    added to the errors array, all other entities would be updated properly  (The default value is
    `false`.)</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div> Sample json:

                   POST /ShopsPrices
                   {
                     \"payload\": [
                            {
                             \"id\": \"YOUR_SHOP_ID_V2\",
                             \"goods\": [
                                 {
                                     \"id\": \"YOUR_GOOD_V2_ID\",
                                     \"price\": 111,
                                     \"maxDiscountPercent\": 9
                                 },
                                 {
                                     \"id\": \"RGFFE2354\",
                                     \"price\": 222,
                                     \"maxDiscountPercent\": 14
                                 }
                             ]
                         },
                         {
                         \"goods\": [
                             {
                                     \"id\": \"SOME_GOOD_V2_ID\",
                                     \"price\": 99.99,
                                     \"maxDiscountPercent\": 0
                             },
                             {
                                     \"id\": \"ANOTHER_GOOD_V2_ID\",
                                     \"maxDiscountPercent\": 12,
                                     \"price\": 88
                             }
                             ]
                         }
                     ],
                     \"nonAtomic\": false
                   }

    Args:
        x_client_key (Union[Unset, str]):
        body (PostV2ShopsPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]
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
    body: PostV2ShopsPricesBody,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]]:
    r"""Set Prices

     <div class=\"apidocs-russian\"><span>Отправка GZip архива товаров,в ответе возвращается время
    постановки сообщения в очередь на шину данных Архивированный файл должен содеражть Json, состоящий
    из полей: payload - PostSetShopPrices[] (Массив структур, соответствующих модели сущности) nonAtomic
    - bool Признак необходимости обрабатывать элементы массива `payload` по отдельности. При
    возникновении ошибки для одной из записей(например, товар не найден в бд), операция не завершалась с
    ошибкой, а эта ошибка добавлялась в массив ошибок, а все сущности, для которых ошибок не возникло,
    успешно обновились.(Значение по умолчанию `false`.)</span><br><div class=\"required-
    annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-weight:
    normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Sending goods GZIP archive.  Response returns data bus message queuing timestamp. The
    archived file must be a Json, containing fields: payload - PostSetShopPrices [] (An array of
    structures corresponding to the entity model) nonAtomic - bool (Indicates whether to process payload
    array elements separately. If an error occures for one of the records (for example, the product has
    not been found in database), the operation would not complete with an error, this error would be
    added to the errors array, all other entities would be updated properly  (The default value is
    `false`.)</div><br/><div class=\"apidocs-russian version-annotation\">В методах версии 2 (V2)
    идентификаторы уникальны в разрезе аккаунта (используются идентификаторы внешней системы заказчика),
    в отличие от методов версии 1 (V1), где использовались идентификаторы уникальные в разрезе всей
    системы.</div>
                <div class=\"apidocs-english version-annotation\">Each model identifier is unique in
    scope of user account in V2 methods (user external system ids). Whereas globally unique system
    identifiers were used in V1 methods (our system ids).</div> Sample json:

                   POST /ShopsPrices
                   {
                     \"payload\": [
                            {
                             \"id\": \"YOUR_SHOP_ID_V2\",
                             \"goods\": [
                                 {
                                     \"id\": \"YOUR_GOOD_V2_ID\",
                                     \"price\": 111,
                                     \"maxDiscountPercent\": 9
                                 },
                                 {
                                     \"id\": \"RGFFE2354\",
                                     \"price\": 222,
                                     \"maxDiscountPercent\": 14
                                 }
                             ]
                         },
                         {
                         \"goods\": [
                             {
                                     \"id\": \"SOME_GOOD_V2_ID\",
                                     \"price\": 99.99,
                                     \"maxDiscountPercent\": 0
                             },
                             {
                                     \"id\": \"ANOTHER_GOOD_V2_ID\",
                                     \"maxDiscountPercent\": 12,
                                     \"price\": 88
                             }
                             ]
                         }
                     ],
                     \"nonAtomic\": false
                   }

    Args:
        x_client_key (Union[Unset, str]):
        body (PostV2ShopsPricesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsCommonApiErrorModel, NebularApiModelsCommonApiGuidModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_client_key=x_client_key,
        )
    ).parsed
