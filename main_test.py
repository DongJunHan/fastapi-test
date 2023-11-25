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


def test_create_user():
    # given
    form = {
        "id": "vda",
        "password": "sadv",
        "password_confirm": "sadv",
        "name": "json"
    }
    # when
    response = client.post('/users', json=form)
    # then
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == 'vda'
    assert response.json()['password'] == 'sadv'
    assert response.json()['name'] == 'json'
