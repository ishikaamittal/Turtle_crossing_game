import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for cars in car_manager.all_cars:
        if cars.distance(player_turtle) < 26:
            score_board.game_over()
            game_is_on = False

    if player_turtle.ycor() > 280:
        score_board.increase_score()
        player_turtle.reset()
        car_manager.next_level()

screen.exitonclick()
