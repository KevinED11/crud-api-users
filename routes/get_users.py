from fastapi import APIRouter

from routes.create_user import user_list

get_users = APIRouter(tags=["Users"])


@get_users.get("/users")
async def get_all_user():
    if not user_list:
        return ["empty"]

    return user_list
