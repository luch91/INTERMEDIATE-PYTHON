class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students


class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses


# Create some Student instances
student1 = Student('John', 1)

# Create some Student instances

student2 = Student('Jane', 2)
student3 = Student('Bob', 3)

# Create some Course instances
math_course = Course('Math')
english_course = Course('English')

# Add students to courses
math_course.add_student(student1)
math_course.add_student(student2)
english_course.add_student(student2)
english_course.add_student(student3)

# Create a School instance
school = School('XYZ School')

# Add courses to school
school.add_course(math_course)
school.add_course(english_course)

# Get the students in the math course
math_course_students = math_course.get_students()
print(f"Students in Math course: {[student.get_name() for student in math_course_students]}")

# Get the courses in the school
school_courses = school.get_courses()
print(f"Courses in school: {[course.name for course in school_courses]}")

# Remove the English course from the school
school.remove_course(english_course)

# Get the courses in the school again
school_courses = school.get_courses()
print(f"Courses in school after removing English course: {[course.name for course in school_courses]}")

"""
Explanation:

We define the Student class, which has methods get_name and get_id.
We define the Course class, which has methods add_student, remove_student, and get_students, and has a list of Student 
instances as an attribute.
We define the School class, which has methods add_course, remove_course, and get_courses, and has a list of Course 
instances as an attribute.
We create some instances of Student, Course, and School.
We add some students to some courses, and add those courses to the school.
We get the students in the math course by calling the get_students method on the math_course instance, 
and we get the courses in the school by calling the get_courses method on the school instance.
We remove the English course from the school by calling the remove_course method on the school instance.
We get the courses in the school again to see that the English course has been removed.
"""



class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students


class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses


# Create some Student instances
student1 = Student('John', 1)
student2 = Student('Jane',2)
# Create some Student instances

student3 = Student('Bob', 3)

# Create some Course instances
course1 = Course('Python Programming')
course2 = Course('Data Science')
course3 = Course('Machine Learning')

# Add the students to the courses
course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student2)
course2.add_student(student3)
course3.add_student(student1)
course3.add_student(student3)

# Refactored the code above. The code below:

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students


class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_courses(self):
        return self.courses


# Create some Student instances
student1 = Student('John', 1)
student2 = Student('Jane', 2)

# Create some Student instances
student3 = Student('Alice', 3)

# Create some Course instances and add students to them
math_course = Course('Math')
math_course.add_student(student1)
math_course.add_student(student2)

science_course = Course('Science')
science_course.add_student(student2)
science_course.add_student(student3)

# Create a School instance and add courses to it
school = School('ABC School')
school.add_course(math_course)
school.add_course(science_course)

# Get the students in a course
math_students = math_course.get_students()
print(f"Students in math course:")
for student in math_students:
    print(f"{student.get_name()} (ID: {student.get_id()})")

# Get the courses in a school
school_courses = school.get_courses()
print(f"Courses in {school.name}:")
for course in school_courses:
    print(course.name)

"""
Explanation:

We define the Student class, which has methods get_name and get_id.
We define the Course class, which has methods add_student, remove_student, and get_students, and has a list of
 Student instances as an attribute.
We define the School class, which has methods add_course, remove_course, and get_courses, and has a list of Course 
instances as an attribute.
We create some instances of Student, Course, and School, and add students to courses, and courses to the school.
We get the students in a course by calling the get_students method on a Course instance, and iterate over the
 returned list to print the names and IDs of the students.
We get the courses in a school by calling the get_courses method on a School instance, and iterate over 
the returned list to print the names of the courses.
"""


