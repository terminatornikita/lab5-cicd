import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_existed_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Ivan"

def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user():
    new_user = {"name": "Petr"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Petr"
    assert "id" in data

def test_update_user():
    updated_data = {"name": "Sergey"}
    response = client.put("/users/1", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sergey"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204
    # Проверим, что пользователь действительно удалён
    get_response = client.get("/users/1")
    assert get_response.status_code == 404
