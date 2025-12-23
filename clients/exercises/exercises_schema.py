from pydantic import BaseModel, Field

from utils.fakers import fake


class GetExercisesQuerySchema(BaseModel):
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4())
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score())
    min_score: int = Field(alias="minScore", default_factory=fake.min_score())
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer())
    description: str = Field(default_factory=fake.text())
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time())


class UpdateExerciseRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score())
    min_score: int = Field(alias="minScore", default_factory=fake.min_score())
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer())
    description: str = Field(default_factory=fake.text())
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time())
