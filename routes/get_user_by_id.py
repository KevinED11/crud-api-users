from uuid import UUID


from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from routes.create_user import user_list
from models.user_read import UserRead

get_user_by_id = APIRouter(tags=["Users"])


@get_user_by_id.get("/users/id/{uuid}", response_model=UserRead)
async def get_user(uuid: UUID):
    user = (user for user in user_list if user.id == uuid)

    try:
        existing_user = next(user)
    except StopIteration:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not found")

    return existing_user
