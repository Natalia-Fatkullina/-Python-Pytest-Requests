import requests
import pytest

trainer_token = '133932ca48d486beca88387cf05898f0'
host = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type' : 'application/json', 'trainer_token' : trainer_token}
parametrs ={'trainer_id' :  7148}

def test_status_code():
    status = requests.get(url=f'{host}/pokemons', params=parametrs, headers=header)
    assert status.status_code == 200

@pytest.mark.parametrize('key,  value', [('id', '7148'), ('trainer_name', 'Супер Нат'), ('level', '5'),('city', 'Токио')])

def test_parametrize(key, value):
    trainer = requests.get(url=f'{host}/trainers', params=parametrs, headers=header)
    assert  trainer.json()['data'][0][key] == value

