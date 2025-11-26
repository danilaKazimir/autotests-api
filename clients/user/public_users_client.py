from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/public/users", json=request)
