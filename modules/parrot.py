from modules import base

class Parrot(base.Species):
    def __init__(self):
        super().__init__('Parrot', base.Family.BIRD)
