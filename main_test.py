from fastapi.testclient import TestClient
from fastapi import status
from main import app
client = TestClient(app)

def test_login():
    #given
    id = "asd"
    password = "csa"
    form = {
        "id": id,
        "password": password
    }
    #when
    response = client.post("/login", json=form)
    #then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == id
    