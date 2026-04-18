from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict

router = APIRouter(prefix="/users", tags=["users"])

class User(BaseModel):
    id: int
    name: str

class UserCreate(BaseModel):
    name: str

fake_db: Dict[int, User] = {
    1: User(id=1, name="Ivan"),
    2: User(id=2, name="Maria")
}
next_id = 3

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    global next_id
    new_user = User(id=next_id, name=user_data.name)
    fake_db[next_id] = new_user
    next_id += 1
    return new_user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserCreate):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = User(id=user_id, name=user_data.name)
    fake_db[user_id] = updated_user
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return None
