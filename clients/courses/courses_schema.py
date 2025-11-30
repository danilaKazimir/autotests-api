from pydantic import BaseModel, Field

from clients.files.files_schema import FileSchema
from clients.user.user_schema import UserSchema


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class GetCoursesQuerySchema(BaseModel):
    user_id: int = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="priviewFileId")
    created_by_user_id: str = Field(alias="createByUserId")


class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
