from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client  # type: ignore


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestedDict(TypedDict):
    email: str
    password: str


class LoginResponseDict(TypedDict):
    token: Token


class RefreshRequestedDict(TypedDict):
    refreshToken: str


class AuthenticationClient(ApiClient):
    def login_api(self, request: LoginRequestedDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestedDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestedDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())  # type: ignore
