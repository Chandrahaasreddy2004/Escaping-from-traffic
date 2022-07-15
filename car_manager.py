COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
A=0
from turtle import Turtle,Screen
import random

class CarManager:
    def __init__(self):
        self.cars=[]
        self.distance=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice=random.randint(0,6)
        if(random_choice==6):
            chandu = Turtle()
            screen = Screen()
            chandu.shape("square")
            chandu.shapesize(1, 2)
            chandu.color(random.choice(COLORS))
            screen.tracer(0)
            chandu.penup()
            chandu.goto(290, random.randint(-230, 230))
            chandu.setheading(180)
            screen.update()
            self.cars.append(chandu)


    def move(self):
        for car in self.cars:
            car.forward(10)


    def update_level(self):
        for car in self.cars:
            global MOVE_INCREMENT
            MOVE_INCREMENT+=10
            car.forward(MOVE_INCREMENT)