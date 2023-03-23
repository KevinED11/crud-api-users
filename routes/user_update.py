from uuid import UUID

from fastapi import APIRouter, HTTPException, Body
from starlette.status import HTTP_404_NOT_FOUND

from routes.create_user import user_list
from models.update_user import UserUpdate
from models.user_read import UserRead
from helpers import get_user_by_id

user_update = APIRouter(tags=["Users"])


@user_update.put("/users/update/{uuid}", response_model=UserRead)
async def update(uuid: UUID, new_data_user: UserUpdate = Body(
    example=
    {"name": "kevin",
     "username": "kevind",
     "age": 25,
     "email": "kevin@hotmail.com",
     "password": "kevin123"
     }

)):
    user_in_list = get_user_by_id(uuid=uuid)

    if user_in_list is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not found")

    user_existing_to_update = user_in_list[0]

    for (key, value) in new_data_user.dict(exclude_unset=True).items():
        setattr(user_existing_to_update, key, value)

    return user_existing_to_update
