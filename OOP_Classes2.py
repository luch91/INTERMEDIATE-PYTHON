# classes that call one another.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} ({self.year}) is starting...")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def drive(self):
        print(f"{self.make} {self.model} ({self.year}) with {self.num_doors}")


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.make} {vehicle.model} ({vehicle.year}) added to the garage.")

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)
        print(f"{vehicle.make} {vehicle.model} ({vehicle.year}) removed from the garage")

    def start_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.start()


car1 = Car("Toyota", "Camry", 2021, 4)
car2 = Car("Honda", "Civic", 2022, 2)
car3 = Car("Hyundai", "Mox", 2025, 6)
garage1 = Garage()

garage1.add_vehicle(car1)
garage1.add_vehicle(car2)
garage1.add_vehicle(car3)
garage1.start_all_vehicles()
garage1.remove_vehicle(car1)
garage1.start_all_vehicles()




