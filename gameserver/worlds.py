from player import Player

worlds = {}
numWorlds = 0
maxPlayersPerWorld = 20

def construct_worlds(num_worlds):
    global worlds
    global numWorlds 
    numWorlds = num_worlds

    for i in range(num_worlds):
        world = {}
        players = {}

        world['players'] = players
        worlds[i] = world

def add_player_to_world(world_num):
    global maxPlayersPerWorld
    global worlds

    if world_num in worlds:
        world = worlds[world_num]

        if len(world['players']) >= maxPlayersPerWorld:
            return {}
        else:
            player_id = len(world['players'])
            player = {}
            player['id'] = player_id
            world['players'][player_id] = player
            return player

def update_game(request):

    global worlds
    action = request['action']



def add_player():
    player = add_player_to_world(0)
    return player

def get_world(world_num):
    global worlds
    return worlds[world_num]



def print_worlds():
    global worlds
    print(worlds)