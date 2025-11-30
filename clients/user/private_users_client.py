from httpx import Response

from clients.api_client import ApiClient
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)
from clients.user.user_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(ApiClient):
    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(
        self, user_id: str, request: UpdateUserRequestSchema
    ) -> Response:
        return self.patch(
            f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True)
        )

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self) -> GetUserResponseSchema:
        response: Response = self.get_user_me_api()
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))
