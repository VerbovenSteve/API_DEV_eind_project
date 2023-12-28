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



# Add more tests for other endpoints as needed


if __name__ == "__main__":
    pytest.main(["-sv", "test_main.py"])