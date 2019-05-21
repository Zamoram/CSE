class Item (object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__ (self, name, tool):
        super(Weapon, self).__init__(name)
        self.damage = True


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__("Boning Knife")
        self.stab = True
        self.shank = 21


class M16(Weapon):
    def __init__(self, name):
        super(M16, self).__init__(name)
        self.shoot = -38


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.slash = -22


class Shotgun(Weapon):
    def __init__(self, name):
        super(Shotgun, self).__init__(name)
        self.blast = -25


class Grenades(Weapon):
    def __init__(self, name):
        super(Grenades, self).__init__(name)
        self.explosive = -30


class Canoe(Weapon):
    def __init__(self, name):
        super(Canoe, self).__init__(name)
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


class Med_Kit(Consumables):
    def __init__(self, name):
        super(Med_Kit, self).__init__(name)
        self.gain_health = 50


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Scale_Armor(Armor):
    def __init__(self, name):
        super(Scale_Armor, self).__init__(name)
        self.add_health =+ 100


class Brigandine(Armor):
    def __init__(self, name):
        super(Brigandine, self).__init__(name)
        self.health_added =+ 150


class Gladiator_Armor(Armor):
    def __init__(self, name):
        super(Gladiator_Armor, )


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

class Player(object):
    def __init__(self, name, health, weapon, armor):
        super(Player, self).__init__(name, health, weapon, armor)
        self.inventory = []

# Items


knife = Weapon("Boning knife", -21)
m16 = Weapon("M16", -38)
sword = Weapon("Sword", -22)
shotgun = Weapon("Shotgun", -25)
grenades = Weapon("Grenades", -30)
canoe = Weapon("Canoe", -15)
toyota = Vehicle("Toyota", 60)
lamborghini = Vehicle("Lamborghini", 200)
acura = Vehicle("NSX", 125)
_armor = Armor("Armor of the Teachers", 100)
bandages = Consumables("Bandages", 30)
med_kit = Consumables("Med Kit", 50)
scale_armor = Consumables("Scale Armor", 100)
brigandine_armor = Consumables("Brigandine Armor", 150)



# Characters
enemy = Character("Enemy", 100, sword, Armor("Scale Armor", 100))
player1 = Character("Player1", 100, canoe, Armor("Brigandine Armor", 150))

enemy.attack(player1)
player1.attack(enemy)
player1.attack(enemy)
enemy.attack(player1)
