import requests
import pytest

TOKEN = '89c3310f6f34778eb7f41e3b39c2e2d9'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN 
    }

def test_get_trainers():
    response = requests.get(URL, headers=HEADERS)
    try:
        assert response.status_code == 200
        print("Тест пройден")
    except AssertionError:
        print(f"Тест не пройден {response.status_code}")

import json

TRAINER_ID = 15242
TOKEN = '89c3310f6f34778eb7f41e3b39c2e2d9'
URL = 'https://api.pokemonbattle.ru/v2/trainers'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

def test_response_contains_trainer_name():
    url = f'{URL}/?trainer_id={TRAINER_ID}'
    response_get = requests.get(url, headers=HEADERS)
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert response_data["data"][0]["trainer_name"] == 'nastya'
    print("тренер nastya")
    