COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 3

    def create_car(self):
        choice=random.randint(0,6)
        if choice==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            y_cor=random.randint(-250,250)
            new_car.goto(280,y_cor)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.MOVE_DISTANCE)
    def increase_speed(self):
        self.MOVE_DISTANCE+=self.MOVE_INCREMENT

