import turtle as t
from random import choice, randint


ej = t.Turtle()
ej.shape("turtle")
ej.speed(0)


# changing color mode to RGB
t.colormode(255)

# colors = ['aquamarine', 'dark orange', 'orchid', 'cornflower blue', 'medium purple', 'powder blue',
#           'royal blue', 'medium purple', 'light sea green', 'dark orchid']
#
# def random_color():
#     r = randint(0,255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     color = (r, g, b)
#     return color


# # Dashed Line
# for x in range(20):
#     ej.forward(10)
#     ej.penup()
#     ej.forward(10)
#     ej.pendown()


# # Geometric Shape Walk
# sides = 3
# while sides < 10:
#     angle = 360/sides
#     ej.color(choice(colors))
#     for i in range(sides):
#         ej.forward(100)
#         ej.right(angle)
#     sides += 1


# # Random Walk
# ej.pensize(8)
# direction = [0, 90, 180, 270]
# for x in range(500):
#     ej.setheading(choice(direction))
#     ej.forward(20)
#     ej.color(random_color())


# # Circle Illusion
# circle_count = 70
# angle = 360/circle_count
#
# for i in range(circle_count):
#     ej.color(random_color())
#     ej.circle(100)
#     ej.left(angle)


# # Get Hirst painting colors using colorgram
# from colorgram import extract
#
# colors = []
# rgb = extract('hirst.jpg', 30)
#
# for color in rgb:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)
#
# print(colors)

colors = [(19, 112, 165), (217, 149, 94), (204, 68, 26), (185, 15, 41), (218, 74, 101), (225, 206, 101), (216, 126, 161), (168, 48, 87), (24, 39, 150), (22, 171, 197), (24, 188, 126), (118, 171, 201), (204, 154, 21), (22, 132, 47), (14, 13, 80), (212, 9, 6), (206, 86, 72), (228, 206, 9), (238, 164, 179), (112, 196, 160), (138, 222, 172), (7, 103, 23), (241, 168, 158), (7, 44, 17), (128, 110, 183), (140, 216, 225)]

# Hirst Painting
x = -350
y = -350
ej.penup()
ej.hideturtle()

for a in range(15):
    ej.setpos(x, y)
    for b in range(15):
        ej.color(choice(colors))
        ej.dot(15)
        ej.forward(50)
    y += 50



screen = t.Screen()
screen.exitonclick()