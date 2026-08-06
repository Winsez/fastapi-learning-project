from fastapi import APIRouter, HTTPException
from backend.day11_app.schemas import ToolCreate, ToolUpdate, ToolResponse


router = APIRouter(
    prefix="/tools",
    tags=["tools"]
)


tools = []


@router.post("", response_model=ToolResponse, status_code=201)
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


@router.get("", response_model=list[ToolResponse])
def get_tools():
    return tools


@router.get("/{tool_id}", response_model=ToolResponse)
def get_tools_by_id(tool_id: int):
    for tool in tools:
        if tool["id"] == tool_id:
            return tool

    raise HTTPException(
        status_code=404,
        detail="Tool not found"
    )


@router.put("/{tool_id}", response_model=ToolResponse)
def put_tools_by_id(tool_data: ToolUpdate, tool_id: int):
    if tool_data.free:
        new_status = "Free"
    else:
        new_status = "Paid"

    for tool in tools:
        if tool["id"] == tool_id:
            tool["name"] = tool_data.name
            tool["category"] = tool_data.category
            tool["status"] = new_status
        
            return tool

    raise HTTPException(
        status_code=404,
        detail="Tool not found"
    )
