import pymunk
import random
from player import Player
import math
class World:

    def __init__(self):
        self.players = {}
        self.objects = {}


    def update_with_action(self, action):
        if(action['action'] == 'movement'):
            vx = float(action['vx'])
            vy = float(action['vy'])

            player_name = action['player_name']
            self.players[player_name].update_velocity(vx,vy)
            
    def to_json(self):

        compound = {}
        players = {}
        for key in self.players:
            player = self.players[key]
            players[player.name] = player.to_json()

        objects = {}
        for key in self.objects:
            obj = self.object[key]
            object[obj.name] = obj.to_json()

        compound['players'] = players
        compound['objects'] = objects

        return compound

    def add_player(self, space):
        exit = False

        while exit == False:
            name = ''.join(random.choice('abcdefgABDDEFG') for _ in range(10))
            
            if name in self.players:
                exit = False
            else:
                self.players[name] = Player(name, space)
                return self.players[name].to_json()


            

    def update(self):
        v = 1
