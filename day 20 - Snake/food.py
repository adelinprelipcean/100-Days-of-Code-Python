from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-450,450), random.randint(-275, 200))
    def refresh(self):
        self.goto(random.randint(-450,450), random.randint(-275, 200))
        