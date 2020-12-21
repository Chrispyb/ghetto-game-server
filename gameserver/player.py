import pymunk
from animation_controller import AnimationController

class Player:

    def __init__(self, name, space):
        self.name = name
        self.animation = AnimationController()
        self.body = pymunk.Body(1,1)  # Create a Body with mass and moment
        self.body.position = 0, 0      # Set the position of the body
        self.velocity_scale = 10.0

        shape = pymunk.Circle(self.body, 10, (0, 0))
        shape.friction = 0.5
        shape.collision_type = 2

        space.add(self.body, shape)       # Add both body and shape to the simulation

    def update_velocity(self, vx, vy):
        scale = self.velocity_scale
        self.body.velocity = (vx * scale, vy * scale)

    def to_json(self):
        obj = {}

        obj['name'] = self.name
        obj['position'] = {'x': self.body.position.x, 'y': self.body.position.y }
        obj['animation'] = self.animation.to_json()
    
        return obj
