from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient


class LoginRequestedDict(TypedDict):
    username: str
    password: str


class RefreshRequestedDict(TypedDict):
    refreshToken: str


class AuthenticationClient(ApiClient):
    def login_api(self, request: LoginRequestedDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestedDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)
