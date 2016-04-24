import terrain
import csv
import pprint


# This function will take the castle CSV and construct the Castle
def parse_castle_file(file_location):
    with open(file_location, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel', delimiter=',')

        first_row = next(csv_reader)

        # First row contains grid size so we are only interested in items 0 and 1
        size_x = int(first_row[0])
        size_y = int(first_row[1])

        print("x: %s y: %s" % (size_x, size_y))

        # Now parse the next size_y rows to get the terrain
        castle_data = []

        for y in range(size_y):
            terrain_data = next(csv_reader)

            for x in range(size_x):
                castle_data.append({"terrain": terrain_data[x]})

        # Now loop y rows again to get directions
        for y in range(size_y):
            directions_data = next(csv_reader)

            for x in range(size_x):
                castle_data[y * size_x + x]['directions'] = directions_data[x]

        # Finally loop y rows again to get items
        for y in range(size_y):
            item_data = next(csv_reader)

            for x in range(size_x):
                item = item_data[x]

                if len(item) == 0:
                    item = None

                castle_data[y * size_x + x]['item'] = item

        pprint.pprint(castle_data)

        # Now that we have built the data we can construct the castle
        castle = Castle(size_x, size_y, castle_data)

        return castle


class Castle(object):
    def __init__(self, size_x, size_y, castle_data):
        self._tile_list = []
        for tile_data in castle_data:
            terrain_string = tile_data['terrain']
            directions = tile_data['directions']
            item = tile_data['item']
            print("Constructing CastleTile with params, terrain: %s, directions: %s, item: %s" % (
            terrain_string, directions, item))
            self._tile_list.append(CastleTile(terrain_string=terrain_string, directions=directions, item=item))
        self._size_x = size_x
        self._size_y = size_y

    def get_tile(self, x, y):
        tile_index = y * self._size_x + x
        return self._tile_list[tile_index]


class CastleTile(object):
    def __init__(self, terrain_string, directions, item=None):

        if terrain_string is None:
            raise AttributeError("Terrain must be supplied")
        else:
            self._terrain = terrain.Terrain(terrain_string)

        if directions is None or len(directions) == 0:
            self._move_north = False
            self._move_east = False
            self._move_south = False
            self._move_west = False
        else:
            if 'n' in directions.lower():
                self._move_north = True
            else:
                self._move_north = False

            if 'e' in directions.lower():
                self._move_east = True
            else:
                self._move_east = False

            if 's' in directions.lower():
                self._move_south = True
            else:
                self._move_south = False

            if 'w' in directions.lower():
                self._move_west = True
            else:
                self._move_west = False

        self._item = item

    def can_move(self, direction):

        if direction.lower().startswith('n'):
            return self._move_north

        if direction.lower().startswith('e'):
            return self._move_east

        if direction.lower().startswith('w'):
            return self._move_west

        if direction.lower().startswith('s'):
            return self._move_south

        # if we get here we don't know how to move
        raise ValueError("Don't know how to move: " + direction)

    def get_terrain_type(self):
        return self._terrain.get_terrain_type()

    def get_terrain_description(self):
        return self._terrain.get_description()

    def get_item(self):
        return self._item
