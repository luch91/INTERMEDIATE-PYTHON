# Call a class from within another  class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super(Teacher, self).__init__(name, age)
        self.subject = subject

    def teach(self, student):
        print(f"{self.name} is teaching {student.name} {self.subject}.")
        student.study()


person1 = Person("Alice", 25)
student1 = Student("Bob", 20, "123")
teacher1 = Teacher("Charlie", 35, "Math")

person1.say_hello()  # Output: Hello, my name is Alice and I am 25 years old.
student1.say_hello()  # Output: Hello, my name is Bob and I am 20 years old.
student1.study()  # Output: Bob is studying.
teacher1.teach(student1)  # Output: Charlie is teaching Bob Math. Bob is studying


