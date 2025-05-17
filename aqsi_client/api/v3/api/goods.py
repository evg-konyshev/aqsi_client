from httpx import Response

from client import AqsiClient, RequestMethods

from api.v3.schemas.request.goods import GoodCreateRequestSchema


class Goods:

    def __init__(self, client: AqsiClient):
        self._client = client

    def create(
        self,
        schema: GoodCreateRequestSchema
    ) -> Response:
        response = self._client.request(
            method=RequestMethods.POST,
            url="/goods/create",
            json=schema.model_dump(),
        )
        return response

