class Room(object):
    # This is a constructor
    def __init__(self, name="", north=None, south=None, east=None, west=None, description="", item=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item


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
        super(Sword, self).__init__(name)
        self.protection = 40
        self.usage_left = 100

    def swinging(self):
        self.usage_left -= 1
        print("You are swinging the sword")

    def block(self):
        self.protection -= 1
        print("Used the sword as a protection")


class Iron(Sword):
    def __init__(self):
        super(Iron, self).__init__("Iron Sword")


class Steel(Sword):
    def __init__(self):
        super(Steel, self).__init__("Steel Sword")


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
    def __init__(self, name, health_added):
        super(Consumables, self).__init__(name,)
        self.health_added = health_added
        self.heal = True


class Bandages(Consumables):
    def __init__(self, name, health_added):
        super(Bandages, self).__init__(name, health_added)
        self.health = 30


class MedKit(Consumables):
    def __init__(self, name, health_added):
        super(MedKit, self).__init__(name, health_added)
        self.gain_health = 50


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class ScaleArmor(Armor):
    def __init__(self, name, armor_amt):
        super(ScaleArmor, self).__init__(name, armor_amt)
        self.add_health = 100


class BrigandineArmor(Armor):
    def __init__(self, name, armor_amt):
        super(BrigandineArmor, self).__init__(name, armor_amt)
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


class Enemy(object):
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


# Items
knife = Weapon("Boning knife", -21)
m16 = Weapon("M16", -38)
sword = Weapon("Sword", -22)
shotgun = Weapon("Shotgun", -25)
grenades = Weapon("Grenades", -30)
canoe = Weapon("Canoe", -15)
toyota = Vehicle("Toyota",)
lamborghini = Vehicle("Lamborghini",)
acura = Vehicle("NSX",)
wiebe_armor = Armor("Armor of the Teachers", 100)
bandages = Consumables("Bandages", 30)
med_kit = Consumables("Med Kit", 50)
scale_armor = Consumables("Scale Armor", 100)
brigandine_armor = Consumables("Brigandine", 150)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 100, canoe, wiebe_armor)
enemy = Character("Enemy", 150, shotgun, scale_armor)

# north=None, south=None, east=None, west=None
# Option 1 - Use the variables,but fix later
living_room = Room("This is a living room", Sword,  "Outside", "Dining Room", None, None, "This is where you live and start "
                                                    "or if you already " "moved, this is where you spawned.",)
dining_room = Room("Dining Room", "Living Room", "Kitchen", "Bed Room1", "Bed Room2", "This is where you eat.")
outside = Room("Outside of the house", "Neighbors House", "Living Room", "Elementary School", "Garage",
               "You are outside of the house and you have four options to go from here, choose your next path.")
kitchen = Room("Kitchen", "Dining Room", "Laundry Room", None, "Hallway", "This is where you cook food")
bedroom1 = Room("This is Bed Room1", "Restroom", None, None, "Dining Room",
                "This is where you sleep and do your homework and where you play video games.")
restroom = Room("A place you do your business also known as the Restroom", None, "Bed Room1", None, None, "You have.")
bedroom2 = Room("The Sleeper", None, "Hallway", "Dining Room", None, "This is where you go to sleep")
hallway = Room("The intersection", "Bed Room2", "BedRoom3", "Kitchen", "Bathroom", "This leads to many routes")
laundry_room = Room("Laundry Room", "Kitchen", None, None, None, "This is where you go to wash your clothes.")
bedroom3 = Room("Bed Room3", "Hallway", None, None, None,
                "This is where your guests can go to sleep when you have visitors over.")
bathroom = Room("Bathroom", None, None, "Hallway", None, "Another room to take care of your business.")
restroom1 = Room("Restroom1", None, "Bed Room1", None, None, "This is the first bathroom built in the house.")
garage = Room("Garage", None, None, "Outside", None, "This is where you park your cars.")
neighbors_house = Room("The Neighbor.", None, "Outside", None, None, "This is where your neighbor lives.")
elementary_school = Room("Elementary School", None, None, None, "Outside", "This is where you went to school.")


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
# Controller
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
    elif "take" in command.lower():
        if player.current_location.items is not None:
            item_name = command[5:]
            item_found = None
            if player.current_location.items.name.lower() == item_name.lower():
                item_found = player.current_location.items

            if item_found is not None:
                player.inventory.append(item_found)
                player.current_location.items = None
        else:
            print("There are not items here")

    elif "drop" in command.lower():
        if player.current_location.items is None:
            item_name = command[5:]
            drop_item = None
            for item in player.inventory:
                if item.name.lower() == item_name.lower():
                    drop_item = item

            if drop_item is not None:
                player.current_location.items = drop_item
                player.inventory.remove(drop_item)
        else:
            print("There is already an item here.")

    elif "use" in command.lower():
        if player.current_location.items is None:
            item_name = command[5:]
            use_item = None
            for item in player.inventory

    else:
        print("Command not recognized.")