from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class ApplicationCreate(BaseModel):
    candidate: str
    vacancy: str
    remote: bool


applications = []


@app.post("/vacancy-applications", status_code=201)
def create_application(application: ApplicationCreate):
    if not application.remote:
        work_format = "Office"
    else: 
        work_format = "Remote"

    application_id = len(applications) + 1

    new_application = {
        "id": application_id,
        "candidate": application.candidate,
        "vacancy": application.vacancy,
        "format": work_format
    }

    applications.append(new_application)

    return new_application


@app.get("/vacancy-applications")
def get_applications():
    return applications


@app.get("/vacancy-applications/{application_id}")
def get_application_by_id(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application
        
    raise HTTPException(
        status_code=404
    )