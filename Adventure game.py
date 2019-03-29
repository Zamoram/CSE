class Room(object):
    # This is a constructor
    def __init__(self, name="", north=None, south=None, east=None, west=None, description=""):
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
outside = Room("Outside of the house",None, None, None, None, "You are outside of the house and you can not go any farther and you must go back.")
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
neighborshouse = Room("The Neighbor.", None, None, None, None, "This is where your neighbor lives.")
elementaryschool = Room("Jackson", None, None, None, None, "This is where you went to school.")


# Fixes
living_room.north = outside
living_room.south = dining_room
dining_room.north = living_room
dining_room.south = kitchen
dining_room.east = bedroom1
dining_room.west = bedroom2
outside.north = neighborshouse
outside.south = living_room
outside.east = elementaryschool
outside.west = garage
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



class Item (object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__ (self, name, tool):
        super(Weapon, self).__init__(name)
        self.damage = True


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.stab = True


class M16(Weapon):
    def __init__(self, name):
        super(M16, self).__init__(name)
        self.shoot = -125


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.slash = -100

class Shotgun(Weapon):
    def __init__(self, name):
        super(Shotgun, self).__init__(name)
        self.blast = -150


class Grenades(Weapon):
    def __init__(self, name):
        super(Grenades, self).__init__(name)
        self.explosive = -175

class Vehicle(Item):
    def __init__(self, name):
        super(Vehicle, self).__init__(name)
        self.drive = True


class Toyota(Vehicle):
    def __init__(self, name):
        super(Toyota, self).__init__(name)
        self.miles_per_hour = 60


class Lamborghini(Vehicle):
    def __init__(self, name):
        super(Lamborghini, self).__init__(name)
        self.speed = 200


class Acura(Vehicle):
    def __init__(self, name):
        super(Acura, self).__init__(name)
        self.speed = 125


class Consumables(Item):
    def __init__(self, name):
        super(Consumables, self).__init__(name)
        self.heal = True


class Bandages(Consumables):
    def __init__(self, name):
        super(Bandages, self).__init__(name)
        self.health = 30


class Med_Kit(Consumables):
    def __init__(self, name):
        super(Med_Kit, self).__init__(name)
        self.gain_health

class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some Fabulous armor!")
        else:
            self. health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %(self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the Teachers", 100)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 100, canoe, wiebe_armor)

orc.attack(wiebe)
wiebe.attack(orc)
wiebe.attack(orc)

world_map = {
    'Living Room': {
        'Name': "Living Room",
        'Description': "This is where you live and start.",
        'Paths': {
            'North': "Outside",
            'South': "Dining Room"
        }
    },
    'Dining Room': {
        'Name': "Eating Area",
        'Description': "This is where you eat",
        'Paths': {
            'East': "Bed_Room1",
            'South': "Kitchen",
            'North': "Living Room",
            'West': "Bed_Room2"
        }
    },
    'Outside': {
        'Name': "Outside of the house",
        'Description': "You are outside of the house and you can not go any farther and you must go back.",
        'Paths': {
            'North': "Neighborshouse",
            'South': "Living Room",
            'East': "Elementaryschool",
            'West': "Garage"

        }
    },
    'Bed_Room1': {
        'Name': "Place to sleep",
        'Description': "This is where you sleep and do your homework and where you play video games.",
        'Paths': {
            'North': "Restroom",
            'West': "Dining Room"
        }
    },
    'Restroom': {
        'Name': "A place you do your buisness",
        'Description': "This is where you go to relieve yourself.",
        'Paths': {
            'South': "Bed_Room1"
        }
    },
    'Bed_Room2': {
        'Name': "The Sleeper",
        'Description': "This is where you go to sleep",
        'Paths': {
            'East': "Dining_Room",
            'South': "Hallway"
        }
    },
    'Kitchen': {
        'Name': "The Eater",
        'Description': "This is where you cook food",
        'Paths': {
            'North': "Dining_Room",
            'South': "Laundry Room",
            'West': "Hallway"
        }
    },
    'Hallway': {
        'Name': "The intersection",
        'Description': "This leads to many routes.",
        'Paths': {
            'North': "Bed_Room2",
            'East': "Kitchen",
            'South': "BedRoom3",
            'West': "BathRoom"
        }

    },
    'BathRoom': {
        'Name': "The pooper",
        'Description': "Another room to take care of your business",
        'Paths': {
            'East': "Hallway"

        }
    },
    'BedRoom3': {
        'Name': "The guest bedroom",
        'Description': "This is where your guests can go to sleep when you have visitors over",
        'Paths': {
            'North': "Hallway"
        }
    },
    'LandryRoom': {
        'Name': "The washing room",
        'Description': "This is where you go to wash your clothes.",
        'Paths': {
            'North': "Kitchen"
        }
    },
    'Restroom1': {
        'Name': "The buisness taker",
        'Description': "This is the first bathroom built in the house",
        'Paths': {
            'South': "Bed_Room1"
        }
    },
    'Garage': {
        'Name': "The car storer",
        'Description': "This is where you park your cars",
        'Paths': {
            'East': "Outside"
        }
    },
    'NeighborsHouse': {
        'Name': "The Neighbor",
        'Description': "This is where your neighbor lives",
        'Paths': {
            'South': "Outside"
        }
    },
    'ElementarySchool': {
        'Name': "Jackson",
        'Description': "This is you went to school",
        'Paths': {
            'West': "Outside"
        }
    }
}
# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Living Room"]  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['Room'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
    elif "take" in command:
        item_name = command[5:]
        found_item = none
        for item in player.current_location.items:
            if item.name == item_name
                found_item = item
            if found_item is not name:
                player.inventory.append(found_item)
                player.current_location.items.remove(found_item)

        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")

    else:
        print("Command not recognized.")
found_item = none
for item in player.current_location.items:
