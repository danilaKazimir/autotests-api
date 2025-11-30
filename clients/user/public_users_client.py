from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.user.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUserClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response: Response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())
