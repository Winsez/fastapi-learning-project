from fastapi import FastAPI

from backend.day11_app.routers.tools import router as tools_router
from backend.day11_app.routers.users import router as users_router


app = FastAPI()


app.include_router(users_router)
app.include_router(tools_router)