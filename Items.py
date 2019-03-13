class Item (object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__ (self, name, tool):
        super(Weapon, self).__init__(name)
        self.tool = True


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.stab = True


class M17(Weapon):
    def __init__(self, name):
        super(M17, self).__init__(name)
        self.shoot = True


class Scar(Weapon):
    def __init__(self,name):
        super(Scar, self)

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
            self. health -= damage - self.armor.
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
