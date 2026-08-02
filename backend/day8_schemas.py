from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class ToolCreate(BaseModel):
    name: str
    category: str
    free: bool


class ToolResponse(BaseModel):
    id: int
    name: str
    category: str
    status: str


tools = []


@app.post("/tools", response_model=ToolResponse, status_code=201)
def post_tool(tool_data: ToolCreate):
    if tool_data.free:
        tool_status = "Free"
    else:
        tool_status = "Paid"

    tool_id = len(tools) + 1

    new_tool = {
        "id": tool_id,
        "name": tool_data.name,
        "category": tool_data.category,
        "status": tool_status,
    }

    tools.append(new_tool)

    return new_tool


@app.get("/tools", response_model=list[ToolResponse])
def get_tools():
    return tools


@app.get("/tools/{tool_id}", response_model=ToolResponse)
def get_tools_by_id(tool_id: int):
    for tool in tools:
        if tool["id"] == tool_id:
            return tool

    raise HTTPException(
        status_code=404,
        detail="Tool not found"
    )