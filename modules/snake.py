from modules import base

class Snake(base.Species):
    def __init__(self):
        super().__init__('Snake', base.Family.REPTILE)
