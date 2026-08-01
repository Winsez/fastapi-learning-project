from fastapi import FastAPI


app = FastAPI()


@app.get("/vacancies/{vacancy_id}")
def vaca (
    vacancy_id: int,
    role: str,
    format: str = "remote"
):
    return {
        "vacancy_id": vacancy_id,
        "role": role,
        "format": format
    }