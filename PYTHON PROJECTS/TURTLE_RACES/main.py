import colorgram as c
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour")

if user_bet:
    is_race_on = True


tom = Turtle(shape="turtle")
tom.penup()
tom.color("red")
tom.goto(-230,-100)

tam = Turtle(shape="turtle")
tam.penup()
tam.color("yellow")
tam.goto(-230,-60)

tum = Turtle(shape="turtle")
tum.penup()
tum.color("orange")
tum.goto(-230,-20)

tym = Turtle(shape="turtle")
tym.penup()
tym.color("blue")
tym.goto(-230, 20)

tim = Turtle(shape="turtle")
tim.penup()
tim.color("purple")
tim.goto(-230, 60)

tem = Turtle(shape="turtle")
tem.penup()
tem.color("green")
tem.goto(-230, 100)

all_turtles = [tom, tam, tum, tym, tim, tem]

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()