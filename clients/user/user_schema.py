from pydantic import BaseModel, Field, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str | None = None
    last_name: str | None = Field(default=None, alias="lastName")
    first_name: str | None = Field(default=None, alias="firstName")
    middle_name: str | None = Field(default=None, alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    user: UserSchema
