# Dictionary comprehension
# Syntax for creating a new dictionary from a list

"""
From a list:

new_dict = {new_key:new_value for item in list}

from a dictionary:

new_dict = {new_key:new_value for(key, value) in dict.items()}

Conditional:

new_dict = {new_key: value for (key, value) in dict.items() if test}
"""
import random

names = ["Joy", "Gladys", "Simeon", "Oluchukwu", "Shiloh", "Darlington", "Darlene", "Ijeoma", "Onyinye"]
new_dict = {student: random.randint(30, 100) for student in names}
print(new_dict)

# to print a new dictionary from new_dict for students who scored 60 and above
passed_students = {student:score for (student, score) in new_dict.items() if score >= 60}
print(passed_students)

# dictionary from a sentence

sentence = "What is the rate of adoption in Nigeria?"
new_list = sentence.split()  # converts sentence to a list
print(new_list)

result = {word: random.randint(2, 10) for word in sentence.split()}
result2 = {word: len(word) for word in sentence.split()}
print(result)
print(result2)

# convert a dictionary of weather in celsius to F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# celsius to F = celsius * 9/5 + 32
weather_f_dict = {day: temp_celsius * 9/5 + 32 for (day, temp_celsius)  in weather_c.items()}
print(weather_f_dict)

# to loop through dictionaries
for (day, temp_celsius) in weather_f_dict.items():
    print(temp_celsius)
