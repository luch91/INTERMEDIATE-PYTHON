import colorgram

rgb_colors = []
colors = colorgram.extract("hirst_paint.jpg", 28)
for color in colors:
    r = color.rgb.r
    g = color.rgb.b
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


