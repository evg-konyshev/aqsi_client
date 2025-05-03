from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nebular_api_controllers_v3_documents_app_list_documents_response_v3 import (
    NebularApiControllersV3DocumentsAppListDocumentsResponseV3,
)
from ...models.nebular_api_models_lk_service_v3_documents_v3_documents_sorted_v3 import (
    NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3,
)
from ...models.nebular_api_models_lk_service_v3_error_model_v3 import NebularApiModelsLkServiceV3ErrorModelV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_status: Union[Unset, str] = UNSET,
    filtered_number: Union[Unset, int] = UNSET,
    filtered_date_time_from: Union[Unset, str] = UNSET,
    filtered_date_time_to: Union[Unset, str] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["page"] = page

    params["filtered.status"] = filtered_status

    params["filtered.number"] = filtered_number

    params["filtered.dateTimeFrom"] = filtered_date_time_from

    params["filtered.dateTimeTo"] = filtered_date_time_to

    json_sorted_: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(sorted_, Unset):
        json_sorted_ = []
        for sorted_item_data in sorted_:
            sorted_item = sorted_item_data.to_dict()
            json_sorted_.append(sorted_item)

    params["sorted"] = json_sorted_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/documents/inventory",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    if response.status_code == 200:
        response_200 = NebularApiControllersV3DocumentsAppListDocumentsResponseV3.from_dict(response.json())

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
) -> Response[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
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
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_status: Union[Unset, str] = UNSET,
    filtered_number: Union[Unset, int] = UNSET,
    filtered_date_time_from: Union[Unset, str] = UNSET,
    filtered_date_time_to: Union[Unset, str] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка документов по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read documents list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_status (Union[Unset, str]):
        filtered_number (Union[Unset, int]):
        filtered_date_time_from (Union[Unset, str]):
        filtered_date_time_to (Union[Unset, str]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        filtered_status=filtered_status,
        filtered_number=filtered_number,
        filtered_date_time_from=filtered_date_time_from,
        filtered_date_time_to=filtered_date_time_to,
        sorted_=sorted_,
        x_client_key=x_client_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_status: Union[Unset, str] = UNSET,
    filtered_number: Union[Unset, int] = UNSET,
    filtered_date_time_from: Union[Unset, str] = UNSET,
    filtered_date_time_to: Union[Unset, str] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка документов по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read documents list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_status (Union[Unset, str]):
        filtered_number (Union[Unset, int]):
        filtered_date_time_from (Union[Unset, str]):
        filtered_date_time_to (Union[Unset, str]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page=page,
        filtered_status=filtered_status,
        filtered_number=filtered_number,
        filtered_date_time_from=filtered_date_time_from,
        filtered_date_time_to=filtered_date_time_to,
        sorted_=sorted_,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_status: Union[Unset, str] = UNSET,
    filtered_number: Union[Unset, int] = UNSET,
    filtered_date_time_from: Union[Unset, str] = UNSET,
    filtered_date_time_to: Union[Unset, str] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка документов по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read documents list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_status (Union[Unset, str]):
        filtered_number (Union[Unset, int]):
        filtered_date_time_from (Union[Unset, str]):
        filtered_date_time_to (Union[Unset, str]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        filtered_status=filtered_status,
        filtered_number=filtered_number,
        filtered_date_time_from=filtered_date_time_from,
        filtered_date_time_to=filtered_date_time_to,
        sorted_=sorted_,
        x_client_key=x_client_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_status: Union[Unset, str] = UNSET,
    filtered_number: Union[Unset, int] = UNSET,
    filtered_date_time_from: Union[Unset, str] = UNSET,
    filtered_date_time_to: Union[Unset, str] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка документов по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read documents list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_status (Union[Unset, str]):
        filtered_number (Union[Unset, int]):
        filtered_date_time_from (Union[Unset, str]):
        filtered_date_time_to (Union[Unset, str]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DocumentsV3DocumentsSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiControllersV3DocumentsAppListDocumentsResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page=page,
            filtered_status=filtered_status,
            filtered_number=filtered_number,
            filtered_date_time_from=filtered_date_time_from,
            filtered_date_time_to=filtered_date_time_to,
            sorted_=sorted_,
            x_client_key=x_client_key,
        )
    ).parsed
