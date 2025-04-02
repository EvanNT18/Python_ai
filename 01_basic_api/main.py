from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: str


@app.post("/users/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}
