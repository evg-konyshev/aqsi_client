from enum import Enum
from typing import Any

from httpx import Client, Response


class RequestMethods(str, Enum):
    GET = "GET"
    POST = "POST"


class AqsiClient:

    token_prefix: str = "Bearer "

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        follow_redirects: bool = True,
    ) -> None:
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"{self.token_prefix}{token}"}
        self._client = Client(
            base_url=self.base_url,
            headers=self.headers,
            follow_redirects=follow_redirects,
        )

    def request(
        self,
        url: str,
        method: RequestMethods,
        params: dict[str, Any] | None = None,
        json: dict[str, Any]  | None = None,
        expected_status: int | None = None,
    ) -> Response:
        response = self._client.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=json,
        )
        if expected_status:
            response.raise_for_status()
        return response