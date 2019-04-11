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
    def __init__(self, name, starting_location, weapon, armor):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location
        self.weapon = weapon
        self.armor = armor
        self.name = name

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some Fabulous armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

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
        room_name = getattr(self.current_location, direction)
        return room_name


class Item (object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__(name, 21)
        self.stab = True
        self.shank = 21


class M16(Weapon):
    def __init__(self, name):
        super(M16, self).__init__(name, 38)
        self.shoot = -38


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name, 22)
        self.slash = -22


class Shotgun(Weapon):
    def __init__(self, name):
        super(Shotgun, self).__init__(name, 25)
        self.blast = -25


class Grenades(Weapon):
    def __init__(self, name):
        super(Grenades, self).__init__(name, 30)
        self.explosive = -30


class Canoe(Weapon):
    def __init__(self, name):
        super(Canoe, self).__init__(name, 15)
        self.whack = -15


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


class MedKit(Consumables):
    def __init__(self, name):
        super(MedKit, self).__init__(name)
        self.gain_health = 50


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class ScaleArmor(Armor):
    def __init__(self, name, armor_amt):
        super(ScaleArmor, self).__init__(name, armor_amt)
        self.add_health = 100


class Brigandine(Armor):
    def __init__(self, name, armor_amt):
        super(Brigandine, self).__init__(name, armor_amt)
        self.health_added = 150


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
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Enemy(Character):
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
knife = Knife("Boning knife")
m16 = M16("M16")
sword = Sword("Sword")
shotgun = Shotgun("Shotgun")
grenades = Grenades("Grenades")
canoe = Canoe("Canoe")
toyota = Vehicle("Toyota")
lamborghini = Vehicle("Lamborghini")
acura = Vehicle("NSX")
wiebe_armor = Armor("Armor of the Teachers", 100)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 100, canoe, wiebe_armor)
enemy = Character("Enemy", 150,)


# Option 1 - Use the variables,but fix later
living_room = Room("Living Room", None, None, None, None, "This is where you live and start.")
dining_room = Room("Eating Area", None, None, None, None, "This is where you eat.")
outside = Room("Outside of the house", None, None, None, None,
               "You are outside of the house and you can not go any farther and you must go back.")
kitchen = Room("The Eater", None, None, None, None, "This is where you cook food")
bedroom1 = Room("Place to sleep", None, None, None, None,
                "This is where you sleep and do your homework and where you play video games.")
restroom = Room("A place you do your business", None, None, None, None, "This is where you go to relieve yourself.")
bedroom2 = Room("The Sleeper", None, None, None, None, "This is where you go to sleep")
hallway = Room("The intersection", None, None, None, None, "This leads to many routes")
laundry_room = Room("The washing room", None, None, None, None, "This is where you go to wash your clothes.")
bedroom3 = Room("The guest bedroom", None, None, None, None,
                "This is where your guests can go to sleep when you have visitors over.")
bathroom = Room("The pooper", None, None, None, None, "Another room to take care of your business.")
restroom1 = Room("The buisness taker", None, None, None, None, "This is the first bathroom built in the house.")
garage = Room("The car storer", None, None, None, None, "This is where you park your cars.")
neighbors_house = Room("The Neighbor.", None, None, None, None, "This is where your neighbor lives.")
elementary_school = Room("Jackson", None, None, None, None, "This is where you went to school.")


# Fixes
living_room.north = outside
living_room.south = dining_room
dining_room.north = living_room
dining_room.south = kitchen
dining_room.east = bedroom1
dining_room.west = bedroom2
outside.north = neighbors_house
outside.south = living_room
outside.east = elementary_school
outside.west = garage
kitchen.north = dining_room
kitchen.south = laundry_room
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
laundry_room.north = kitchen
bedroom3.north = hallway
bathroom.east = hallway
restroom1.south = bedroom1
garage.east = outside
neighbors_house.south = outside
elementary_school.west = outside


directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
playing = True

player = Player("person1", living_room, sword, wiebe_armor)

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif "take" in command:
        item_name = command[5:]
        found_item = None
        for item in player.current_location.items:
            if item.name == item_name:
                found_item = item
            if found_item is not item_name:
                player.inventory.append(found_item)
                player.current_location.items.remove(found_item)

    else:
        print("Command not recognized.")
