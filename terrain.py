
class Terrain(object):

    # We can also use this to find valid terrains
    _terrain_descriptions = {
        "grass" : "in long grass",
        "water" : "in 10 feet of water",
        "corridor" : "in a dark corridor",
        "stable" : "knee deep in horse s**t",
        "courtyard" : "on a stone floor",
        "drawbridge" : "on a magnificent drawbridge (I hope that it is down)",
        "archway" : "You are standing under a large archway"
    }

    def __init__(self, terrain_string):
        if terrain_string is None:
            raise AttributeError("Terrain must be string, but supplied None")

        if terrain_string.lower() in self._terrain_descriptions.keys():
            self._terrain = terrain_string

    def get_terrain_type(self):
        return self._terrain

    def get_description(self):
        return self._terrain_descriptions[self._terrain]
