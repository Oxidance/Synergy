class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'Вместимость одного автобуса {self.name} {capacity} пассажиров'

class Autobus(Transport):


bus = Autobus.seating_capacity(capacity=50)
print(bus.seating_capacity())