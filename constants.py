class Reference:                # Class for links on variable
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def set(self, new_value):
        self.value = new_value


TILE_WIDTH = 68
TILE_HEIGHT = 17
X_OFFSET = 34
FPS = 60
PLAYER_MAX_SPEED = 3
PLAYER_START_SPEED = 0.02
GLOBAL_LIGHTNING_ANGLE = 90
black = 0
white = 1
block = 0
stone_wall = 1
tree = 2
MASTER_VOLUME = Reference(0.0)
