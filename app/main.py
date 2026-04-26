from fastapi import FastAPI
from app.routes import health,auth
from app.db.database import engine, Base
from app.models.user import User


Base.metadata.create_all(bind=engine)
app= FastAPI()


app.include_router(health.router)
app.include_router(auth.router)

@app.get("/")
def root():
 return {"message": "API is running"}