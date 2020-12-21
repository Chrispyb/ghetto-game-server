import pymunk
from animation_controller import AnimationController

class Objects:

    def __init__(self, name, space):
        self.name = name
        self.animation = AnimationController()
        self.body = pymunk.Body(1,1)  # Create a Body with mass and moment
        self.body.position = 0, 0      # Set the position of the body

        self.poly = pymunk.Poly.create_box(self.body) # Create a box shape and attach to body
        space.add(self.body, self.poly)       # Add both body and shape to the simulation

    def to_json(self):
        obj = {}

        obj['name'] = self.name
        obj['position'] = {'x': self.body.position.x, 'y': self.body.position.y }
        obj['animation'] = self.animation.to_json()
    
        return obj