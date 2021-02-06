# Turtle Shape Creator

color = input('Choose a color: ')
line_width = int(input('Choose a line width: '))
line_len = int(input('Choose a line length: '))
shape = input('Choose either a line, triangle, or square: ')

import turtle
aScreen = turtle.Screen()

frank = turtle.Turtle()
frank.color(color)
frank.width(line_width)
tri_angle = 120
sq_angle = 90

if shape == 'line':
    frank.color(color)
    frank.width(line_width)
    frank.forward(line_len)
  

if shape == 'triangle':
    frank.color(color)
    frank.width(line_width)
    frank.forward(line_len)
    frank.left(tri_angle)
    frank.forward(line_len)
    frank.left(tri_angle)
    frank.forward(line_len)

if shape == 'square':
    frank.color(color)
    frank.width(line_width)
    frank.forward(line_len)
    frank.left(sq_angle)
    frank.forward(line_len)
    frank.left(sq_angle)
    frank.forward(line_len)
    frank.left(sq_angle)
    frank.forward(line_len)
