from fastapi import FastAPI
from uvicorn import run as uvicorn_run


from routes.root import root
from routes.get_users import get_users
from routes.create_user import create_user
from routes.get_user_by_id import get_user_by_id
from routes.user_update import user_update
from routes.filtered_users import filter_user
from routes.delete_user import user_delete
from routes.update_field import update_field

app = FastAPI()


app.include_router(root)


app.include_router(create_user)


app.include_router(get_users)


app.include_router(get_user_by_id)


app.include_router(filter_user)


app.include_router(user_update)


app.include_router(update_field)


app.include_router(user_delete)


if __name__ == "__main__":
    uvicorn_run(app=app, host="localhost", port=8000)
