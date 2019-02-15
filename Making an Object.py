class Car(object):
    def __init__(self, company="Acura", color="Red", car_start="Engine On"):
        self.speed = 200
        self.gas_left = 10
        self.brand = company
        self.color = color
        self.turn_key = car_start
        self.running = True

    def accelerate(self, gas):
        if self.running:
            if self.gas_left <= 25:
                print("Need more gas, fill me up.")
                return
            self.gas_left += gas
            if self.gas_left >= 75:
                print("I'm full, lets drive.")
                self.gas_left = 75


            else:
                print("The car is now at %d%%" % self.gas_left)
        else:
            print("It's ready to drive.")

    def drive(self):
        self.running = False
        print("We should go and get a ticket and ram some cars.")
        print("I'll buy another car anyways.")

    def speed(self, fuel):
        self.gas_left -= fuel
        print("Stomp on the pedal, lets go faster")
        print("Alright but we're running out of gas.")

my_Vehicle =