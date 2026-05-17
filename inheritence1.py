class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    pass
School_bus=bus("volvo",120,15)
print("Vehicle name is=",School_bus.name)
print("Vehicle maximum speed is=",School_bus.max_speed)
print("Vehicle mileage is=",School_bus.mileage)
