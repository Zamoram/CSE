class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east

# These are the instances of the rooms (Instantiation)

# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room",)
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room",)
parking_lot = Room("The Parking Lot", None, R19A)

Living_Room =  Room("")
