import time
from turtle import Screen, Shape
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

# Game parameters
game_speed = 1
current_speed = 1
car_list = []

# Car shape define
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
for i in colors:
    s = Shape("compound")
    poly = ((-10,-20),(10,-20),(10,20),(-10, 20))
    s.addcomponent(poly, f"{i}")
    screen.register_shape(f"car_{i}", s)

# Player/Cars define
player = Player()
for i in range(10):
    car = CarManager(current_speed)
    car_list.append(car)

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.01*game_speed)
    screen.onkeypress(player.move, "Up")
    screen.listen()
    screen.update()
    
    # Cars behavior
    for car in car_list:
        car.move()
        car.update()
        
    # Collision with cars
    for car in car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 250:
        player.reset_position()
        
        # Increase cars speed
        current_speed *= 1.1
        
        # Increase speed for existing cars
        for car in car_list:
            car.car_speed = current_speed
        
        # Add 2 more cars
        for i in range(2):
            car = CarManager(current_speed)
            car_list.append(car)
            
        # Update score board
        scoreboard.increase_score()
        scoreboard.update_score()
            
screen.exitonclick()
    
    
