from fastapi import FastAPI, HTTPException


app = FastAPI()


games = [
    {"id": 1, "name": "Dead by Daylight"},
    {"id": 2, "name": "World of Warcraft"},
    {"id": 3, "name": "Cyberpunk 2077"}
]

@app.get("/games/filter")
def filt_games (word:str = ""):
    filtered_games = []

    for game in games:
        if word.lower() in game["name"].lower():
            filtered_games.append(game)

    return filtered_games


@app.get("/games/search")
def games_list(
    word:str = "",
    min_id:int = 1
):
    filtered_games = []
    for game in games:
        if word.lower() in game["name"].lower() and game["id"] >= min_id:
            filtered_games.append(game)

    return filtered_games
  

@app.get("/games/{game_id}")
def gamescheck(game_id:int):
    for game in games:
        if game["id"] == game_id:
            return game
    
    raise HTTPException(
        status_code=404,
        detail="Game not found"
    )


@app.get("/games")
def gamesfunc(name:str):
    for game in games:
        if game["name"].lower() == name.strip().lower():
            return game

    raise HTTPException(
        status_code=404,
        detail="Game not found"
    )


