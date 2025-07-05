from turtle import Turtle
import time

DIFFICULTY = 9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep((11-DIFFICULTY)/50) 
        
    def bounce(self):
        self.y_move *= -1
    
    def hit(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.setposition(0, 0)
        self.bounce()