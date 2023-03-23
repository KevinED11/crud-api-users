from uuid import UUID


from pydantic import BaseModel, EmailStr, validator
from fastapi import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


class BaseUser(BaseModel):
    id: UUID = None
    name: str
    username: str
    age: int
    email: EmailStr
    password: str

    @validator("age")
    def validate_age(cls, age):
        if age >= 18:
            return age
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="place 18 or more")
