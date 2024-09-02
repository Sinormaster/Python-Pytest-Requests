import requests

import pytest


URL ='https://api.pokemonbattle.ru/v2'

TRANER_ID =  '5141'


def test_treners():
 response = requests.get(url = f'{URL}/trainers')
 print(response.text)



def test_my_trener():
  response_my_trener = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRANER_ID})
  print(response_my_trener.text)