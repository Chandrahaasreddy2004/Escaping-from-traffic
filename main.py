A=0
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    car_manager.create_car()
    car_manager.move()
    #if user lost
    for cc in car_manager.cars:
        if(cc.distance(player)<25):
            game_is_on=False
            scoreboard.looses()

    #if user wins a level
    if(player.ycor()>280):
        player.reset()
        scoreboard.update_scoreboard()
        car_manager.update_level()


    screen.update()

screen.exitonclick()

