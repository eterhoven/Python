from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        sq_1 = Turtle()
        sq_2 = Turtle()
        sq_3 = Turtle()

        sq_1.penup()
        sq_2.penup()
        sq_3.penup()

        sq_1.color("white")
        sq_2.color("white")
        sq_3.color("white")

        sq_1.shape("square")
        sq_2.shape("square")
        sq_3.shape("square")

        sq_2.goto(-20, 0)
        sq_3.goto(-40, 0)

        self.segments = [sq_1, sq_2, sq_3]
    
    
    def extend(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def reset(self):
        self.segments.clear()
        self.create_snake()