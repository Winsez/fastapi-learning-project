from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, Backend"}


@app.get("/status")
def show_status():
    return {"status": "running"}


@app.get("/info")
def show_info():
    return {"project": "AI Vacancy Analyzer", "task": "06A"}


@app.get("/vacancies/{vacancy_id}")
def get_vacancy(vacancy_id: int):
    return {"vacancy_id": vacancy_id}


@app.get("/vacancies")
def get_vacancies(level: str = 'all'):
    return {"level": level}