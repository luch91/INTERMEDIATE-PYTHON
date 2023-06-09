import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gaps):
    for _ in range(int(360/size_of_gaps)):
        tim.color(random_color())
        tim.circle(100)
        # current_heading = tim.heading() to check the current heading
        tim.setheading(tim.heading() + 10)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
