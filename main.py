class BMW:
    def fuel_type(self):
        print("BMW Fuel Type: Petrol")

    def max_speed(self):
        print("BMW Max Speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari Fuel Type: Petrol")

    def max_speed(self):
        print("Ferrari Max Speed: 340 km/h")

def car_details(car):
    car.fuel_type()
    car.max_speed()
    print()

bmw = BMW()
ferrari = Ferrari()

car_details(bmw)
car_details(ferrari)