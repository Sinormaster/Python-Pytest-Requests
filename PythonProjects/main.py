import requests



URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='1a7a8d3b59a1790d2f868986685fe8db'
HEADER = {'Content-Type': 'application/json' , 'trainer_token' :TOKEN}
body_registration = {
    "name": "GIGI",
    "photo_id": 1
}

body_change_name = {
    "pokemon_id": "65957",
    "name": "XIXI",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "35318"
}

response = requests.post(url =  f'{URL}/pokemons', headers =  HEADER , json = body_registration)
print(response.text)


response_change = requests.put(url =  f'{URL}/pokemons', headers =  HEADER , json = body_change_name)
print(response_change.text)



response_catch = requests.post(url =  f'{URL}/trainers/add_pokeball', headers =  HEADER , json = body_catch)
print(response_catch.text)