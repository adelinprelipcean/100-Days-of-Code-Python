from turtle import Turtle, Screen

screen = Screen()

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(5, 1)
        self.paddle.setposition(position)
        
    def go_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def go_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
    
    def position(self):
        return self.paddle.position()