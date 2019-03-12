class Item (object):
    def __init__(self, name):
        self.name = name


class Cleaning_supplies(Item):
    def __init__ (self, name):
        super(Cleaning_supplies, self).__init__(name)
        self.cleaning = True


class Clorox(Cleaning_supplies):
    def __init__(self, name):
        super(Clorox, self).__init__(name)
        self.grab = True


class Broom(Cleaning_supplies):
    def __init__(self, name):
        super(Broom, self).__init__(name)


class Mop(Cleaning_supplies):
    def __init__(self,name):
        super(Mop)




