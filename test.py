import requests
import pytest

url = "http://127.0.0.1:8000"


def get_access_token(username, password):
    token_url = f"{url}/token"
    response = requests.post(
        token_url,
        data={"username": username, "password": password},
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise ValueError(f"Failed to obtain access token: {response.text}")


def test_create_user():
    data = {
        "email": "test",
        "password": "test"
    }
    response = requests.post(f"{url}/users", json=data)
    assert response.status_code == 200


# post endpoint test
def test_create_film():
    data = {"title": "Test Film", "release_year": 2022}
    response = requests.post(f"{url}/films", json=data)
    assert response.status_code == 200


def test_create_person():
    data = {
        "name": "this person is actor",
        "age": 34,
        "film_id": 1
    }
    response = requests.post(f"{url}/persons", json=data)
    assert response.status_code == 200


def test_create_starship():
    data = {
        "name": "schipke",
        "model": "cruizer",
        "film_id": 1
    }
    response = requests.post(f"{url}/starships", json=data)
    assert response.status_code == 200


# get endpoints test
def test_get_user_me():
    access_token = get_access_token("test", "test")
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{url}/users/me", headers=headers)
    assert response.status_code == 200


def test_read_films():
    response = requests.get(f"{url}/films")
    assert response.status_code == 200


def test_read_persons_by_name():
    response = requests.get(f"{url}/persons/")
    assert response.status_code == 200


def test_read_starships():
    response = requests.get(f"{url}/starships")
    assert response.status_code == 200


def test_get_all_films_with_characters_starships():
    access_token = get_access_token("test", "test")
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{url}/films/all_with_characters_starships", headers=headers)
    assert response.status_code == 200


def test_update_film_title():
    data = {"title": "Updated Title"}
    response = requests.put(f"{url}/films/1", json=data)
    assert response.status_code == 200


def test_delete_film():
    response = requests.delete(f"{url}/films/1")
    assert response.status_code == 200


# Add more tests for other endpoints as needed


if __name__ == "__main__":
    pytest.main(["-sv", "test_main.py"])
