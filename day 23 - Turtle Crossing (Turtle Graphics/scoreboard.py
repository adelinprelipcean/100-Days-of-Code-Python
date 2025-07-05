from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(0, 250)
        self.update_score()
        self.color("black")
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)
    def increase_score(self):
        self.level += 1
    def game_over(self):
        self.clear()
        self.write(f"GAME OVER! You finished {self.level} levels.", align='center', font=("Courier", 16, 'normal'))
