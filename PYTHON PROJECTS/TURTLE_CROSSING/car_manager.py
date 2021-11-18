from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setpos(300, random.choice(range(-250, 250)))
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT



