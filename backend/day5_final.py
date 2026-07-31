from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class BuildsListData(BaseModel):
    survivor: str
    perk_count: int
    meta: bool


builds_list = []


@app.post("/survivor-builds", status_code=201)
def post_builds(build_info: BuildsListData):
    if build_info.meta:
        build_rating = "Meta"
    else:
        build_rating = "Casual"

    
    build_id = len(builds_list) + 1

    survivor_build = {
        "id": build_id,
        "survivor": build_info.survivor,
        "perk_count": build_info.perk_count,
        "rating": build_rating
    }

    builds_list.append(survivor_build)

    return survivor_build


@app.get("/survivor-builds")
def get_all_builds():
    return builds_list


@app.get("/survivor-builds/{build_id}")
def get_build_by_id(build_id: int):
    for build in builds_list:
        if build["id"] == build_id:
            return build

    raise HTTPException(
        status_code=404
    )