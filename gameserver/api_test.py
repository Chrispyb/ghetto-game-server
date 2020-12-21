import requests
import json


def test_post():
    payload = {'world_id': 1, 'player_id': 1}
    r = requests.post('http://localhost:5000/test_post', data=payload)

def add_player():
    r = requests.get('http://localhost:5000/new_player')
    return r.text

def test_update(player):
    payload = {'action': 'movement', 'vx':5, 'vy':0, 'player_name': player['name']}
    r = requests.post('http://localhost:5000/update_world', data=payload)
    print(r.text)

def test_update_2(player):
    payload = {'action': 'movement', 'vx':2, 'vy':0, 'player_name': player['name']}
    r = requests.post('http://localhost:5000/update_world', data=payload)
    print(r.text)

def test_update_3(player):
    payload = {'action': 'movement', 'vx':0.0, 'vy':0, 'player_name': player['name']}
    r = requests.post('http://localhost:5000/update_world', data=payload)
    print(r.text)

def get_world_state():
    r = requests.get('http://localhost:5000/get_world')
    print(r.text)



player = add_player()
player = json.loads(player)

player_2 = add_player()
player_2 = json.loads(player_2)

test_update(player)
test_update_2(player_2)
