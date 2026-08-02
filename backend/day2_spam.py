from fastapi import FastAPI, HTTPException


app = FastAPI()


vacancies = [
    {
        "id": 1,
        "title": "Junior Python Developer",
        "level": "Junior",
        "remote": True,
        "verified": True
    },
    {
        "id": 2,
        "title": "Python Backend Developer",
        "level": "Middle",
        "remote": False,
        "verified": True
    },
    {
        "id": 3,
        "title": "AI Automation Engineer",
        "level": "Junior",
        "remote": True,
        "verified": False
    },
    {
        "id": 4,
        "title": "Python Intern",
        "level": "Intern",
        "remote": True,
        "verified": True
    },
    {
        "id": 5,
        "title": "Junior Backend Developer",
        "level": "Junior",
        "remote": False,
        "verified": False
    }
]


@app.get("/vacancies/filter")
def vac_filter(
    level: str,
    remote_only: bool = False,
    verified_only: bool = False,
    offset: int = 0,
    limit: int = 2
):
    good_vac = []

    for vacancy in vacancies:
        if (
            vacancy["level"].lower() == level.lower()
            and (not remote_only or vacancy["remote"])
            and (not verified_only or vacancy["verified"])
        ):
            good_vac.append(vacancy)

    return good_vac[offset:offset + limit]


@app.get("/vacancies/{vacancy_id}")
def vac_id(vacancy_id: int):
    for vacancy in vacancies:
        if vacancy["id"] == vacancy_id:
            return vacancy

    raise HTTPException(
        status_code=404,
        detail="Vacancy not found"
    )