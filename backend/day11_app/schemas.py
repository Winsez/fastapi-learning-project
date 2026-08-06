from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str


class ToolCreate(BaseModel):
    name: str
    category: str
    free: bool


class ToolUpdate(BaseModel):
    name: str
    category: str
    free: bool


class ToolResponse(BaseModel):
    id: int
    name: str
    category: str
    status: str


