import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
    #when player makes it to the end, reset position and increase the speed of the cars
    if player.ycor() > 280:
        player.reset_player()
        car.level_up()
        sb.increase_score()
        sb.update_score()








screen.exitonclick()

