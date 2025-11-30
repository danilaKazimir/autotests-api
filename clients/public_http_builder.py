from httpx import Client


def get_public_http_client() -> Client:
    return Client(timeout=100, base_url="http://localhost:8000")


def def_public_users_client() -> Client:
    return Client(timeout=100, base_url="http://localhost:8000")
