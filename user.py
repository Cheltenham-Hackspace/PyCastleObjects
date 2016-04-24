
class User(object):

    def __init__(self, castle, start_x=0, start_y=0):
        self._x = start_x
        self._y = start_y
        self._castle = castle

    def get_location(self):
        return self._x, self._y

    def move(self, direction):

        can_move = self._castle.get_tile(self._x, self._y).can_move(direction)

        if can_move:
            self._move(direction)
        else:
            print("Cannot move direction: %s" % direction)

    def _move(self, direction):

        if direction.lower() == 'n':
            self._y -= 1
        elif direction.lower() == 'e':
            self._x += 1
        elif direction.lower() == 'w':
            self._x -= 1
        elif direction.lower() == 's':
            self._y += 1
        else:
            raise ValueError("Don't know how to move: %s" % direction)

    def print_location(self):
        tile = self._castle.get_tile(self._x, self._y)
        terrain_type = tile.get_terrain_type()
        terrain_message = tile.get_terrain_description()
        item = tile.get_item()

        print("(%s, %s, %s) You are standing %s" % (self._x, self._y, terrain_type, terrain_message))
        if item is not None:
            print("This tile contains: %s" % item)
