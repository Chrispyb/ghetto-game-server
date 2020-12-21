from world import World
import pymunk

class Game:

    def __init__(self):
        self.world = World()
        self.space = pymunk.Space() 
        self.space.gravity = 0,0

    def update_with_action(self, action):
        self.world.update_with_action(action)

    def add_player(self):
        return self.world.add_player(self.space)

    def get_game(self):
        return self.world.to_json()

    def update_game(self):
        self.world.update()

        print_options = pymunk.SpaceDebugDrawOptions()
        self.space.step(0.02)        
        #self.space.debug_draw(print_options)
        
