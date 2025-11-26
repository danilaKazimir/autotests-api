from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient


class UpdateRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(ApiClient):
    def get_get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateRequestDict) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")
