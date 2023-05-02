# A passport for 3 people.
"""
The main idea behind this code is to demonstrate the use of classes and objects in Python.
 The Passport class represents a real-world object (a passport) and has attributes such as name,
  surname, age, etc., which describe the properties of a passport. The marital_status method is a behavior
  of the passport object that checks if the passport holder is married based on their age.
"""

"""class Passport:
    def __init__(self, name, surname, middle_name, age, phone_number, nationality, country, religion):
        self.name = name
        self.surname = surname
        self.middle = middle_name
        self.age = age
        self.phone = phone_number
        self.nationality = nationality
        self.country = country
        self.religion = religion
        self.marriage = 0  # this sets the married life to none(default value)

    def marital_status(self, age: any):
        self.age = int(age)
        if self.age >= 30:
            return 1


citizen1 = Passport("Judith", "Ekeleme", "Oluchi",  33,
                    "08130439033", "Nigerian", "Nigeria", "Christianity")

citizen2 = Passport("Luchi", "Choi", "Moon", 32,
                    "09077815953", "South Korean",
                    "South Korea", "Christianity")

citizen3 = Passport("Queen", "Chinwe", "Ekeleme", "23",
                    "09072955583", "German", "Germany",
                    "Christianity")
citizen3.age = 33
print(citizen1.religion)

marital_status = citizen3.marital_status()
print(marital_status)

"""


class Passport:
    def __init__(self, name, surname, middle_name, age, phone_number, nationality, country, religion):
        self.name = name
        self.surname = surname
        self.middle = middle_name
        self.age = int(age)
        self.phone = phone_number
        self.nationality = nationality
        self.country = country
        self.religion = religion
        self.marriage = 0  # this sets the married life to none(default value)

    def marital_status(self):
        if isinstance(self.age, (int, float)):
            if self.age >= 30:
                return 1
        return 0


citizen1 = Passport("Judith", "Ekeleme", "Oluchi",  33,
                    "08130439033", "Nigerian", "Nigeria", "Christianity")

citizen2 = Passport("Luchi", "Choi", "Moon", 32,
                    "09077815953", "South Korean",
                    "South Korea", "Christianity")

citizen3 = Passport("Queen", "Chinwe", "Ekeleme", 23,
                    "09072955583", "German", "Germany",
                    "Christianity")
citizen3.age = 33
print(citizen1.religion)

marital_status = citizen3.marital_status()
print(marital_status)
print(citizen1.marital_status())


class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance
        print(f"Driving {distance} km. Total mileage: {self.image}")

    def can_drive_more(self):
        if self.mileage < 100000:
            return True
        else:
            return False


car1 = Car("Toyota", "Corolla", 2010, 60000)
car2 = Car("Toyota", "Corolla", 2010, 80000)
car3 = Car("Ford", "Escape", 2018, 50000)

print(car1.make, car1.model)
car1.drive(100)
car1.drive(50)
print(car1.can_drive_more())

print(car2.make, car2.model)
car2.drive(200)
car2.drive(300)
print(car2.can_drive_more())

print(car3.make. car3.model)
car3.drive(500)
car3.drive(400)
print(car3.can_drive_more())


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        if not isinstance(miles, int):
            raise TypeError("Miles must be an integer.")
        self.mileage += miles
        if self.mileage >= 10000:
            print("Time for an oil change!")

    def paint(self, new_color):
        self.color = new_color

car1 = Car("Honda", "Civic", 2020, "Red")
car2 = Car("Toyota", "Corolla", 2019, "Blue")
car3 = Car("Ford", "Fiesta", 2018, "Green")

car1.drive(500)
car2.drive(7500)
car3.drive("1000")  # Raises TypeError
