from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import LoginRequestedDict, LoginResponseDict, get_authentication_client  # type: ignore


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authentication_client = get_authentication_client()

    login_request: LoginRequestedDict = LoginRequestedDict(
        username=user.get("email"), password=user.get("password")
    )
    login_response: LoginResponseDict = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="https://localhost:8000",
        headers={
            "Authorization": f"Bearer {login_response.get('token').get('accessToken')}"
        },
    )
