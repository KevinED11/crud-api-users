from uuid import uuid4

from fastapi import APIRouter, Body, Response
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY

from models.create_user import User

create_user = APIRouter(tags=["Users"])

user_list: list[User] = []


@create_user.post("/users", response_model=None,
                  status_code=HTTP_201_CREATED,
                  responses={
                      HTTP_201_CREATED: {"description": "User created successfully"},
                      HTTP_422_UNPROCESSABLE_ENTITY: {"description": "Invalid field"}
                  }
                  )
async def create(user_request: User = Body(
    example=
    {"name": "kevin",
     "username": "kevind",
     "age": 25,
     "email": "kevin@hotmail.com",
     "password": "kevin123"
     }

)):
    user_request.id = uuid4()

    __new_user = User(**user_request.dict())

    user_list.append(__new_user)

    return Response(status_code=HTTP_201_CREATED,
                    content="User created successfully")
