from turtle import Turtle, Screen

tim = Turtle()

tim.forward(100)
tim.left(90)  # 360 degree divided by the number of sides of the shape.
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)

# shorter code

for _ in range(4):
    tim.forward(100)
    tim.left(90)
