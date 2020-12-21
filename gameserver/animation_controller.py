class AnimationController():

    def __init__(self):
        self.animation = None
        self.frame_num = 0

    def to_json(self):
        return self.__dict__
    