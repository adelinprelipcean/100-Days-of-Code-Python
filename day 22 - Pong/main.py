from turtle import Turtle, Screen
from paddle import *
from ball import *
from scoreboard import *

def go_up():
    Paddle.goto(Paddle.xcor(),Paddle.ycor()+20)

def go_down():
    Paddle.goto(Paddle.xcor(),Paddle.ycor()-20)

screen = Screen()
screen.setup(width=800, height=400)
screen.screensize(canvwidth=800, canvheight=400)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

l_Paddle = Paddle((-370,0))
r_Paddle = Paddle((370,0))
ball = Ball()

screen.onkeypress(l_Paddle.go_up, 'w')
screen.onkeypress(l_Paddle.go_down, 's')
screen.onkeypress(r_Paddle.go_up, 'Up')
screen.onkeypress(r_Paddle.go_down, 'Down')

game_on = True

scoreboard = Scoreboard()

while game_on:
    
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
    
    
    if ball.ycor() < -180 or ball.ycor() > 180:
        ball.bounce()
    
    if ball.distance(r_Paddle.position()) < 50 and ball.xcor() > 340:
        ball.hit()
        scoreboard.p2_score += 10
    if ball.distance(l_Paddle.position()) < 50 and ball.xcor() < -340:
        ball.hit()
        scoreboard.p1_score += 10
        
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.p1_score -= 3
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.p2_score -= 3































screen.exitonclick()