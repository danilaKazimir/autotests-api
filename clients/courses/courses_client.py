from typing import TypedDict
from httpx import Response

from clients.api_client import ApiClient


class GetCoursesQueryDict(TypedDict):
    userId: int


class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    priviewFileId: str
    createByUserId: str


class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(ApiClient):
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        return self.get("/api/v1/courses", params=query)  # type: ignore

    def get_course_api(self, course_id: int) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)

    def update_course_api(
        self, course_id: int, request: UpdateCourseRequestDict
    ) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: int) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")
