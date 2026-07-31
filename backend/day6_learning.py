from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class DBDcharacter(BaseModel):
    name: str
    role: str
    licensed: bool


characters_list = []


@app.post("/dbd-characters", status_code=201)
def post_characters(checkdata: DBDcharacter):
    if checkdata.licensed:
        character_type = "Licensed"
    else:
        character_type = "Original"
        

    character_id = len(characters_list) + 1

    character_data = {
        "id": character_id,
        "name": checkdata.name,
        "role": checkdata.role,
        "type": character_type
    }

    characters_list.append(character_data)

    return character_data


@app.get("/dbd-characters")
def get_characters():
    return characters_list


@app.get("/dbd-characters/{character_id}")
def get_character_by_id(character_id: int):
    for character in characters_list:
        if character["id"] == character_id:
            return character

        raise HTTPException(
            status_code=404
        )