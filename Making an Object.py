class Car(object):
    def __init__(self, company="Acura", color="Red", car_start="Engine On"):
        self.speed = 200
        self.gas_left = 25
        self.brand = company
        self.color = color
        self.turn_key = car_start
        self.running = True

    def accelerate(self, speed):
        if self.running:
            if self.gas_left
