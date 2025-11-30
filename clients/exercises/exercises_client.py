from httpx import Response

from clients.api_client import ApiClient
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
)


class ExercisesClient(ApiClient):
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get(f"/api/v1/exercises", params=query.model_dump(by_alias=True))  # type: ignore

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
