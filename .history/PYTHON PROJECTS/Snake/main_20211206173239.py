from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#difficulty = input("Choose a level. Easy, medium, or hard").lower()
#if difficulty == "easy":
#    snake.segments[0].speed("slow")
#elif difficulty == "medium":
#    snake.segments[0].speed("normal")
#elif difficulty == "hard":
#    snake.segments[0].speed("fast")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #detect collision with food
    if snake.segments[0].distance(food) < 15:
        scoreboard.keep_score()
        snake.extend()
        food.refresh()
    
    #detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
        screen.update()
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            screen.update()

screen.exitonclick()