from fastapi import FastAPI
from app.routes import health,auth

app= FastAPI()

app.include_router(health.router)
app.include_router(auth.router)

@app.get("/")
def root():
 return {"message": "API is running"}