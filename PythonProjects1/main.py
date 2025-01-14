import requests  

url = 'https://api.pokemonbattle.ru/v2' 
token = '89c3310f6f34778eb7f41e3b39c2e2d9' 
header = {'Content-Type' : 'application/json', 'trainer_token' : token}

body_create = {
    "name": "Ime",
    "photo_id": 22
}

body_name_change = {
    "pokemon_id": "193902",
    "name": "Mila",
    "photo_id": 22
}

body_catch = {
    "pokemon_id" : "193902"
}


response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.status_code)
print(response_create.text)

response_name_change = requests.put(url = f'{url}/pokemons', headers = header, json = body_name_change)
print(response_name_change.status_code)
print(response_name_change.text)

response_catch = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response_catch.status_code)
print(response_catch.text)

