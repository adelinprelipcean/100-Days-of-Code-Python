from turtle import Turtle, Shape, Screen
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
STARTING_X = 300

cars = ["car_red", "car_yellow", "car_blue", "car_green", "car_orange", "car_purple"]

class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.shape(random.choice(cars))
        self.setheading(180)
        self.car_speed = speed
        self.teleport(random.randint(-300, 300), random.randint(-250,250))
    # Move car
    def move(self):
        self.forward(MOVE_INCREMENT * self.car_speed)
    # Regenerate car
    def update(self):
        if self.xcor() < -250:
            self.teleport(STARTING_X, random.randint(-250,250))