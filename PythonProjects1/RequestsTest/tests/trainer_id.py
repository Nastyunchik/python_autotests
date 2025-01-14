import requests
import pytest

TOKEN = '89c3310f6f34778eb7f41e3b39c2e2d9'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 15242

def test_response_contains_trainer_name():
    url = f"{URL}/{TRAINER_ID}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    assert "name" in response_data
    assert response_data["name"] == 'nastya'