# FileNotFound

try:
    file = open("text_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["skill"])

except FileNotFoundError:
    file = open("text_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"That key{error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")

# Raising exceptions

height = float(input("Height in m: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
BMI = weight / height ** 2
print(BMI)

fruits = ["Apple", "Pear", "Orange"]


def makepie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


