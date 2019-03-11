class Item (object):
    def __init__(self, name):
        self.name = name


class Cleaning_supplies(Item):
    def __init__ (self, name):
        super(Cleaning_supplies, self)
        self.cleaning = True


