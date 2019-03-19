class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """ This ,method takes a direction, and finds the variable of the room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)

# These are the instances of the rooms (Instantiation)

# Option 1 - Use the variables, but fix later
living_room = Room("Living Room", None, None, None, None, "This is where you live and start.")
dining_room = Room("Eating Area", None, None, None, None, "This is where you eat.")
outside = Room("Outside of the house",None, None, None, None,"You are outside of the house and you can not go any farther and you must go back.")
kitchen = Room("The Eater", None, None, None, None, "This is where you cook food")
bedroom1 = Room("Place to sleep", None, None, None, None, "This is where you sleep and do your homework and where you play video games.")
restroom = Room("A place you do your buisness", None, None, None, None, "This is where you go to relieve yourself.")
bedroom2 = Room("The Sleeper", None, None, None, None, "This is where you go to sleep")
hallway = Room("The intersection", None, None, None, None, "This leads to many routes")
laundryroom = Room("The washing room", None, None, None, None, "This is where you go to wash your clothes.")
bedroom3 = Room("The guest bedroom", None, None, None, None, "This is where your guests can go to sleep when you have visitors over.")
bathroom = Room("The pooper", None, None, None, None, "Another room to take care of your buisness.")
restroom1 = Room("The buisness taker", None, None, None, None, "This is the first bathroom built in the house.")
garage = Room("The car storer", None, None, None, None, "This is where you park your cars.")
neighborshouse = ("The Neighbor.", None, None, None, None, "This is where you park your cars.")
elementaryschool = ("Jackson", None, None, None, None, "This is where you went to school.")


# Fixes
living_room.north = outside
living_room.south = dining_room
dining_room.north = living_room
dining_room.south = kitchen
dining_room.east = bedroom1
dining_room.west = bedroom2
outside.south = living_room
kitchen.north = dining_room
kitchen.south = laundryroom
kitchen.west = hallway
bedroom1.north = restroom
bedroom1.west = dining_room
restroom.south = bedroom1
bedroom2.south = hallway
bedroom2.east = dining_room
hallway.north = bedroom2
hallway.south = bedroom3
hallway.east = kitchen
hallway.west = bathroom
laundryroom.north = kitchen
bedroom3.north = hallway
bathroom.east = hallway
restroom1.south = bedroom1
garage.east = outside
neighborshouse.south = outside
elementaryschool.west = outside

player = Player(living_room)

directions = ['north','south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)


    command = input(">_")
    if command in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")

    else:
        print("Command not recognized.")