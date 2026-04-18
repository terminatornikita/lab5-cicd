from fastapi import FastAPI
from src.routers import user

app = FastAPI(title="User API", version="0.1.0")

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Hello from CI/CD lab!"}
