from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client  # type: ignore


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/public/users", json=request)


def get_public_users_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())  # type: ignore
