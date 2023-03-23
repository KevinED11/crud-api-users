from uuid import UUID


from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from starlette.responses import Response


from models.create_user import User
from routes.create_user import user_list
from helpers import get_user_by_id

user_delete = APIRouter(tags=["Users"])


@user_delete.delete("/users/delete/{uuid}", response_model=None)
async def delete(uuid: UUID):
    user_in_list: list[User] = get_user_by_id(uuid=uuid)

    if user_in_list is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not found")

    user_to_delete: User = user_in_list[0]

    user_list.remove(user_to_delete)

    return Response(status_code=HTTP_204_NO_CONTENT,
                    content=None)
    