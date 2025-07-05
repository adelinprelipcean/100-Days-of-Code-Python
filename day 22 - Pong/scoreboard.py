from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 100)
        self.write(self.p1_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 100)
        self.write(self.p2_score, align="center", font=("Arial", 50, "normal"))