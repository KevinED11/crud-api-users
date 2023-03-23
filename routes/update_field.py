from uuid import UUID


from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND


from models.update_field import UpdateFieldUser
from models.create_user import User
from helpers import get_user_by_id


update_field = APIRouter(tags=["Users"])


@update_field.patch("/users/update/{uuid}")
async def update_fields(uuid: UUID, new_data_user: UpdateFieldUser):
    user_in_list: list[User] = get_user_by_id(uuid=uuid)

    if user_in_list is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not found")

    user_existing_to_update: User = user_in_list[0]

    for (key, value) in new_data_user.dict(exclude_unset=True).items():
        setattr(user_existing_to_update, key, value)

    return user_existing_to_update
