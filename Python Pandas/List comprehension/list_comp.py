# List comprehension: create a new list from another list using a line of code

# old code
"""
numbers = [1, 2, 3]
new_num = []
for n in numbers:
    addnew = n + 1
new_list = new_num.append(addnew)
print(new_num)
"""
# one-line key
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [new_numbers + 1 for new_numbers in numbers]

name = "Oluchi"  # [letter for letter in name]
name_list = [letter for letter in name]

# create a new list from range(1,5) and multiply the result by 2
range_list = [item * 2 for item in range(1, 5)]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# create a new list if any of the items has length of 7 and above
names = ["Joy", "Gladys", "Simeon", "Oluchukwu", "Shiloh", "Darlington"]
new_names = [name for name in names if len(name) >= 7]
new_names_upper = [name.upper() for name in names if len(name) >= 7]
print(new_names_upper)








