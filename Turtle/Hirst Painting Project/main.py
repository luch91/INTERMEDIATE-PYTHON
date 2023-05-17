import turtle as turtle_module
import random

# import colorgram

# rgb_colors = []
# colors = colorgram.extract("hirst_paint.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(249, 234, 234), (196, 120, 120), (139, 171, 171), (72, 116, 116), (138, 162, 162), (124, 95, 95),
              (181, 153, 153), (139, 60, 60), (220, 142, 142), (178, 55, 55), (21, 46, 46), (54, 113, 113),
              (38, 20, 20), (185, 107, 107), (229, 164, 164), (137, 38, 38), (194, 84, 84), (71, 132, 132),
              (10, 25, 25), (221, 181, 181), (167, 196, 196), (86, 25, 25), (36, 83, 83), (96, 153, 153),
              (116, 35, 35), (113, 150, 150), (162, 210, 210)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.setheading(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
