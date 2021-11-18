import colorgram as c
import turtle as t
import random

t.colormode(255)

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")

colour_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189)]


def draw_dots():
    halt = 0
    while halt <= 9:
        random_colour = random.choice(colour_list)
        timmy_the_turtle.dot(20, random_colour)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        halt += 1

timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()
timmy_the_turtle.setpos(0, -300)
timmy_the_turtle.pendown()

x = 0
y = -250
while x <= 9:
    draw_dots()
    timmy_the_turtle.setpos(0, y)
    timmy_the_turtle.pendown()
    x += 1
    y += 50

screen = t.Screen()
screen.exitonclick()

#20 in size and spaced by 50
#rgb_colours = []
#colours = c.extract('image.jpg.jpg',6)
#for colour in colours:
#    r = colour.rgb.r
#    g = colour.rgb.g
#    b = colour.rgb.b
#    new_colour = (r, g, b)
#    rgb_colours.append(new_colour)

#print(rgb_colours)
