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
        self.health = +30


class Med_Kit(Consumables):
    def __init__(self, name):
        super(Med_Kit, self).__init__(name)
        self.gain_health = +75


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

    def take_change(self, damage):
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
sword = Weapon("Sword", 45)
Knife = Weapon("Knife", 85)
wiebe_armor = Armor("Armor of the Teachers", 100)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 100, Knife, wiebe_armor)

orc.attack(wiebe)
wiebe.attack(orc)
wiebe.attack(orc)
