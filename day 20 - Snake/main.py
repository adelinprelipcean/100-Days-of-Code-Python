from turtle import Screen, write, penup, goto, Turtle
from snake import Snake
from food import Food
import time

DIFFICULTY = 0.1

score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-40, 250)

def UpdateScore():
    score_writer.clear()
    score_writer.write(f'Score: {score}', font=('Arial Black', 14, 'normal'))

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('#8bb904')
screen.title('Snake Xenzia')
screen.tracer(0)

snake = Snake()
food = Food()
score = 0

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(DIFFICULTY)
    snake.move()
    score_writer.write(f'Score: {score}', font=('Arial Black', 14, 'normal'))
    
    if snake.head.distance(food) <= 15:
        score += 1
        snake.add_element()
        food.refresh()
        UpdateScore()
    if snake.head.position()[0] < -500 or snake.head.position()[0] > 500 or snake.head.position()[1] < -300 or snake.head.position()[1] > 300:
        game_on = False
        penup()
        goto(-210,0)
        write('GAME OVER!', font=("Arial Black",46, "normal")) 
        


























screen.exitonclick()
