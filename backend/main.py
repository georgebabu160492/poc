import api
from fastapi import FastAPI, status
from database import SessionLocal, engine, Base
from starlette.middleware.cors import CORSMiddleware
from sample_data.load_sample_data import (
    load_employee_sample_data,
    load_project_sample_data,
)


Base.metadata.create_all(bind=engine)

app = FastAPI()


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def load_data():
    load_employee_sample_data()
    load_project_sample_data()


load_data()  # uncomment and run this the first time to load initial data

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/api/project", tags=["allocations"])


@app.get("/health-check/")
async def main_route():
    """
    An API to do health check of the application.
    """
    return {"message": "All good!"}
