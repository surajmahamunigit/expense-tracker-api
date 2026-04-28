from fastapi import FastAPI

from app.routes import health, auth, expense
from app.db.init_db import init_db


app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(expense.router)


@app.get("/")
def root():
    return {"message": "API is running"}
