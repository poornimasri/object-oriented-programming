class Vehicle:
    def fare(self):
        return 50 * 100


class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.10


bus = Bus()
print(bus.fare())