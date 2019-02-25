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
outside = Room("Outside of the house",None, None, None, None,"You are outside of the house and you can not go any farther and you must go back.")
kitchen = Room("The Eater", None, None, None, None, "This is where you cook food")
bedroom1 = Room("Place to sleep", None, None, None, None, "This is where you sleep and do your homework and where you play video games.")
restroom = Room("A place you do your buisness", None, None, None, None, "This is where you go to relieve yourself.")
bedroom2 = Room("The Sleeper", None, None, None, None, "This is where you go to sleep")

# Fixes
living_room.north = outside
living_room.south = dining_room
dining_room.north = living_room
dining_room.south = kitchen
dining_room.east = bedroom1
dining_room.west = bedroom2
outside.south = living_room
kitchen.north = dining_room
kitchen.south = laundry_room
kitchen.west = hallway
bedroom1.north = restroom
bedroom1.west = dining_room
restroom.south = bedroom1
bedroom2.south = hallway
bedroom2.east = dining_room
