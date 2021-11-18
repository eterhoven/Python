import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

#Detect a collision with a car
def squish():
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.listen()
screen.onkey(player.move, "Up")


loop = 0
game_is_on = True
while game_is_on:  
    
    time.sleep(0.1)
    screen.update()
    carmanager.move()
    player.position()
    squish()
    loop += 1
    if loop == 6:
        carmanager.create_car()
        loop = 0
    if player.is_at_finish():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()
