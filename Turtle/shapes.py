# draws shapes ranging between 3 sides to 10 sides interlaying one another and with random colours

import turtle as t
import random

tim = t.Turtle()

colours = ["blue", "lime green", "red", "magenta", "dark violet", "gold"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_num in range(3, 14):
    tim.color(random.choice(colours))
    draw_shape(shape_side_num)
