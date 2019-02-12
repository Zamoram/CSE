class Laptop(object):
    def __int__(self, screen_resolution, extra_space, color):
        # Thing that a Laptop has
        # Everything in this list should be relevant to the program
        self.procceser = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Linux"

    def charge(self, time):
        # Computer is already charged
        if self.charge >= 100
            print("The computer is already charged.")
            return

        self.battery_left += time # This adds to the battery life
        # Computer is mostly charged
        if self.battery > 100:
            print("The computer quickly charges.")
            self.battery_left = 100

        # Computer is not charged at all
        else:
            print("The computer is now at %d%% " % self.battery_left)


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("90000000000x9000000000", 99999999999, "Awsome")