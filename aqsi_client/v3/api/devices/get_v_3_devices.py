from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from aqsi_client import errors
from aqsi_client.client import AuthenticatedClient, Client
from ...models.nebular_api_models_lk_service_v3_devices_v3_devices_sorted_v3 import (
    NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3,
)
from ...models.nebular_api_models_lk_service_v3_devices_v3_list_devices_response_v3 import (
    NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3,
)
from ...models.nebular_api_models_lk_service_v3_error_model_v3 import NebularApiModelsLkServiceV3ErrorModelV3
from aqsi_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_activation_date_from: Union[Unset, str] = UNSET,
    filtered_activation_date_to: Union[Unset, str] = UNSET,
    filtered_shop_ids: Union[Unset, list[str]] = UNSET,
    filtered_shop_external_ids: Union[Unset, list[str]] = UNSET,
    filtered_imei: Union[Unset, str] = UNSET,
    filtered_serial_number: Union[Unset, str] = UNSET,
    filtered_model: Union[Unset, list[str]] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_client_key, Unset):
        headers["x-client-key"] = x_client_key

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["page"] = page

    params["filtered.activationDateFrom"] = filtered_activation_date_from

    params["filtered.activationDateTo"] = filtered_activation_date_to

    json_filtered_shop_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_shop_ids, Unset):
        json_filtered_shop_ids = filtered_shop_ids

    params["filtered.shopIds"] = json_filtered_shop_ids

    json_filtered_shop_external_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_shop_external_ids, Unset):
        json_filtered_shop_external_ids = filtered_shop_external_ids

    params["filtered.shopExternalIds"] = json_filtered_shop_external_ids

    params["filtered.imei"] = filtered_imei

    params["filtered.serialNumber"] = filtered_serial_number

    json_filtered_model: Union[Unset, list[str]] = UNSET
    if not isinstance(filtered_model, Unset):
        json_filtered_model = filtered_model

    params["filtered.model"] = json_filtered_model

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
        "url": "/v3/Devices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    if response.status_code == 200:
        response_200 = NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3.from_dict(response.json())

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
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
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
    filtered_activation_date_from: Union[Unset, str] = UNSET,
    filtered_activation_date_to: Union[Unset, str] = UNSET,
    filtered_shop_ids: Union[Unset, list[str]] = UNSET,
    filtered_shop_external_ids: Union[Unset, list[str]] = UNSET,
    filtered_imei: Union[Unset, str] = UNSET,
    filtered_serial_number: Union[Unset, str] = UNSET,
    filtered_model: Union[Unset, list[str]] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка устройств по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read device list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_activation_date_from (Union[Unset, str]):
        filtered_activation_date_to (Union[Unset, str]):
        filtered_shop_ids (Union[Unset, list[str]]):
        filtered_shop_external_ids (Union[Unset, list[str]]):
        filtered_imei (Union[Unset, str]):
        filtered_serial_number (Union[Unset, str]):
        filtered_model (Union[Unset, list[str]]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        filtered_activation_date_from=filtered_activation_date_from,
        filtered_activation_date_to=filtered_activation_date_to,
        filtered_shop_ids=filtered_shop_ids,
        filtered_shop_external_ids=filtered_shop_external_ids,
        filtered_imei=filtered_imei,
        filtered_serial_number=filtered_serial_number,
        filtered_model=filtered_model,
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
    filtered_activation_date_from: Union[Unset, str] = UNSET,
    filtered_activation_date_to: Union[Unset, str] = UNSET,
    filtered_shop_ids: Union[Unset, list[str]] = UNSET,
    filtered_shop_external_ids: Union[Unset, list[str]] = UNSET,
    filtered_imei: Union[Unset, str] = UNSET,
    filtered_serial_number: Union[Unset, str] = UNSET,
    filtered_model: Union[Unset, list[str]] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка устройств по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read device list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_activation_date_from (Union[Unset, str]):
        filtered_activation_date_to (Union[Unset, str]):
        filtered_shop_ids (Union[Unset, list[str]]):
        filtered_shop_external_ids (Union[Unset, list[str]]):
        filtered_imei (Union[Unset, str]):
        filtered_serial_number (Union[Unset, str]):
        filtered_model (Union[Unset, list[str]]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page=page,
        filtered_activation_date_from=filtered_activation_date_from,
        filtered_activation_date_to=filtered_activation_date_to,
        filtered_shop_ids=filtered_shop_ids,
        filtered_shop_external_ids=filtered_shop_external_ids,
        filtered_imei=filtered_imei,
        filtered_serial_number=filtered_serial_number,
        filtered_model=filtered_model,
        sorted_=sorted_,
        x_client_key=x_client_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    page: Union[Unset, int] = 1,
    filtered_activation_date_from: Union[Unset, str] = UNSET,
    filtered_activation_date_to: Union[Unset, str] = UNSET,
    filtered_shop_ids: Union[Unset, list[str]] = UNSET,
    filtered_shop_external_ids: Union[Unset, list[str]] = UNSET,
    filtered_imei: Union[Unset, str] = UNSET,
    filtered_serial_number: Union[Unset, str] = UNSET,
    filtered_model: Union[Unset, list[str]] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка устройств по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read device list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_activation_date_from (Union[Unset, str]):
        filtered_activation_date_to (Union[Unset, str]):
        filtered_shop_ids (Union[Unset, list[str]]):
        filtered_shop_external_ids (Union[Unset, list[str]]):
        filtered_imei (Union[Unset, str]):
        filtered_serial_number (Union[Unset, str]):
        filtered_model (Union[Unset, list[str]]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page=page,
        filtered_activation_date_from=filtered_activation_date_from,
        filtered_activation_date_to=filtered_activation_date_to,
        filtered_shop_ids=filtered_shop_ids,
        filtered_shop_external_ids=filtered_shop_external_ids,
        filtered_imei=filtered_imei,
        filtered_serial_number=filtered_serial_number,
        filtered_model=filtered_model,
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
    filtered_activation_date_from: Union[Unset, str] = UNSET,
    filtered_activation_date_to: Union[Unset, str] = UNSET,
    filtered_shop_ids: Union[Unset, list[str]] = UNSET,
    filtered_shop_external_ids: Union[Unset, list[str]] = UNSET,
    filtered_imei: Union[Unset, str] = UNSET,
    filtered_serial_number: Union[Unset, str] = UNSET,
    filtered_model: Union[Unset, list[str]] = UNSET,
    sorted_: Union[Unset, list["NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3"]] = UNSET,
    x_client_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
]:
    r"""Index

     <div class=\"apidocs-russian\"><span>Получение списка устройств по фильтру</span><br><div
    class=\"required-annotation\">Поля в модели запроса, отмеченные <span style=\"color: red; font-
    weight: normal;\">required</span> - обязательны к заполнению</div></div><div class=\"apidocs-
    english\">Read device list by filter</div>

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        page (Union[Unset, int]):  Default: 1.
        filtered_activation_date_from (Union[Unset, str]):
        filtered_activation_date_to (Union[Unset, str]):
        filtered_shop_ids (Union[Unset, list[str]]):
        filtered_shop_external_ids (Union[Unset, list[str]]):
        filtered_imei (Union[Unset, str]):
        filtered_serial_number (Union[Unset, str]):
        filtered_model (Union[Unset, list[str]]):
        sorted_ (Union[Unset, list['NebularApiModelsLkServiceV3DevicesV3DevicesSortedV3']]):
        x_client_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NebularApiModelsLkServiceV3DevicesV3ListDevicesResponseV3, NebularApiModelsLkServiceV3ErrorModelV3]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page=page,
            filtered_activation_date_from=filtered_activation_date_from,
            filtered_activation_date_to=filtered_activation_date_to,
            filtered_shop_ids=filtered_shop_ids,
            filtered_shop_external_ids=filtered_shop_external_ids,
            filtered_imei=filtered_imei,
            filtered_serial_number=filtered_serial_number,
            filtered_model=filtered_model,
            sorted_=sorted_,
            x_client_key=x_client_key,
        )
    ).parsed
