from fastapi import APIRouter, HTTPException
from backend.day11_app.schemas import UserCreate, UserUpdate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["users"]
    )


users = []


@router.post("", response_model=UserResponse, status_code=201)
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


@router.get("", response_model=list[UserResponse])
def get_users():
    return users


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@router.put("/{user_id}", response_model=UserResponse)
def put_user_by_id(user_id: int, user_update: UserUpdate):
    for user in users:
        if user["id"] == user_id:
            user["username"] = user_update.username
            user["email"] = user_update.email
            user["password"] = user_update.password
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )