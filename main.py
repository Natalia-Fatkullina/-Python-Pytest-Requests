import time
import  pytest
import  requests

trainer_token = '133932ca48d486beca88387cf05898f0'
host = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type' : 'application/json', 'trainer_token' : trainer_token}
create_pokemons = {
    'name' : 'generate',
    'photo_id' : '-1'}

# 1 Создать покемона
first = requests.post(url = f'{host}/pokemons', headers = header,
                    json = create_pokemons)
print(first.text )
# id покемона
pokemon_id = first.json()['id']
print(pokemon_id)

# 2 Сменить имя покемона
new_name = {
    'pokemon_id':  pokemon_id,
     'name' : 'generate',
    'photo_id' : '-1'}
second = requests.put(url = f'{host}/pokemons', headers = header,
                    json = new_name)
print(second.text )

# 3 Поймать покемона в покебол
add_pokeball = { "pokemon_id": pokemon_id}
third = requests.post(url = f'{host}/trainers/add_pokeball', headers = header,
                    json = add_pokeball)
print(third.text )


#  Провести битву (до тех пор пока покемон не проиграет)
parametrs = {'status' : 1, 'in_pokeball': 1,  'sort' : 'asc_date'}
def get_enemy():
    all_pokemons = requests.get(url = f'{host}/pokemons', params = parametrs,  headers = header)
    enemy = all_pokemons.json()['data'][2]['id']
    return (enemy)

def battle():
    battle_body = {
        'attacking_pokemon': pokemon_id,
        'defending_pokemon': get_enemy()}
    battle = requests.post(url=f'{host}/battle', headers=header,
                           json=battle_body)
    return battle
# Провести битву

while True:
    response = battle()
    result = response.json().get('result',  '')
    print(response.text)
    if result != 'Твой покемон победил':
        break
    time.sleep(1)



