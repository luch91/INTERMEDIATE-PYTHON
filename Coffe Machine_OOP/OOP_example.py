# A passport for 6 people.

class Passport:
    def __init__(self, name, surname, middle_name, age: 0, phone_number, nationality, country, religion):
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
        if self.age >= 30:
            return 1


citizen1 = Passport("Judith", "Ekeleme", "Oluchi", 33,
                    "08130439033", "Nigerian", "Nigeria", "Christianity")

citizen2 = Passport("Luchi", "Choi", "Moon", 32,
                    "09077815953", "South Korean",
                    "South Korea", "Christianity")

citizen3 = Passport("Queen", "Chinwe", "Ekeleme", "23",
                    "09072955583", "German", "Germany",
                    "Christianity")
print(citizen1.religion)

print(citizen3.marital_status())


