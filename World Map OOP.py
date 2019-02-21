class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

# These are the instances of the rooms (Instantiation)

# Option 1 - Use the variables, but fix later
living_room = Room("Living Room", None, None, None, None, "This is where you live and start.")
dining_room = Room("Eating Area", None, None, None, None, "This is where you eat.")
outside = Room("Outside of the house",None, None,"This is where you sleep and do your homework and where you play video games." )
kitchen = Room()
bedroom1 = Room("Place to sleep", None, None, None, None,)
restroom = Room

# Fixes
living_room.north = outside
living_room.south = dining_room
dining_room.south = kitchen
dining_room.east = bedroom1
outside.south = living_room

bedroom1.north = restroom
bedroom1.west = dining_room
