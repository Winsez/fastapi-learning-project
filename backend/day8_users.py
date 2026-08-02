from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str


users = []


@app.post("/users", response_model=UserResponse, status_code=201)
def users_post(user_data: UserCreate):
    user_id = len(users) + 1

    new_user = {
        "id": user_id,
        "username": user_data.username,
        "email": user_data.email,
        "password": user_data.password
    }

    users.append(new_user)

    return new_user


@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )