from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient
from clients.files.files_client import File
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class Course(TypedDict):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: ...


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


class CreateCourseResponseDict(TypedDict):
    course: Course


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

    def create_course(
        self, request: CreateCourseRequestDict
    ) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
