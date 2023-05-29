"""
# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

"""
from tkinter import *


def button_clicked():
    print("Button clicked")
    new_text = input.get()
    my_label.config(text= new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=010, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)



