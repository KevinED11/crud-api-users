from fastapi import APIRouter, HTTPException, Query
from starlette.status import HTTP_404_NOT_FOUND

from models.create_user import User
from routes.create_user import user_list
from models.user_read import UserRead

filter_user = APIRouter(tags=["Users"])


@filter_user.get("/users/filtered", response_model=list[UserRead])
async def filter_user_by_params(name: str = Query(default=None, max_length=20),
                                username: str = Query(default=None, max_length=20)):
    users: list[User] = [user for user in user_list
                         if (name is None or name == user.name) and
                         (username is None or username == user.username)
                         ]

    if not users:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    return users
