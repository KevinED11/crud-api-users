from uuid import UUID


from pydantic import BaseModel, EmailStr


class UpdateFieldUser(BaseModel):
    name: str
    username: str = None
    age: int = None
    email: EmailStr
    password: str




