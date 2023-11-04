import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

'''Screen'''
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')
screen.title('CROSS')

'''import variables'''
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

'''Moves'''
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Collision with the wall then level up
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
screen.exitonclick()
