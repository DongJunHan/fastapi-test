from fastapi.testclient import TestClient
from fastapi import status

from main import app

client = TestClient(app)


def test_login():
    # given
    id = "asdf"
    password = "zxcv"
    form = {
        "id": id,
        "password": password
    }
    # when
    response = client.post("/login", json=form)
    # then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == id


def test_login_fail():
    # given
    form = {
        "id": "vsd",
        "password": "cas"
    }
    # when
    response = client.post('/login', json=form)
    # then
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()['detail'] == "please right id or password"
