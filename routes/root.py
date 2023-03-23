from fastapi import APIRouter

root = APIRouter(tags=["Users"])


@root.get("/")
async def get_root():
    return {"Message": "Hello world"}
