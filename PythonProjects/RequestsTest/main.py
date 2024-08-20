import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e5bc108eba9c569397b56b39bebbd61d'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
body_reg = {
    "trainer_token": TOKEN,
    "email": "azarikkk@yandex.ru",
    "password": "1Abrek5885"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_new_name = {
    "pokemon_id": "55619",
    "name": "шурик",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "55619"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_reg)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)'''

'''response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)
message = response_new_name.json()['message']
print(message)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message']
print(message)