from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def food_location_ok(location):
    location_ok = True
    for segment in snake.segments:
        if segment.distance(location) < 40:
            location_ok = False
    return location_ok

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.is_alive:
        snake.move()

        # Detect collision with wall.
        if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
            snake.is_alive = False

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                snake.is_alive = False

         # Detect collision with food.
        if snake.head.distance(food) < 20:
            scoreboard.increase_score()

            food.new_random_position()
            while not food_location_ok(food.new_position):
                print("invalid location, trying again..")
                food.new_random_position()

            food.refresh()
            snake.extend()
        
    else:
        if snake.explode_count >= 20:
            game_is_on = False
            scoreboard.game_over()
        else:
            snake.explode()

screen.exitonclick()
