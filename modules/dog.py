from modules import base

class Dog(base.Species):
    def __init__(self):
        super().__init__('Dog', base.Family.MAMMAL)
