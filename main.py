from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

border = Border()
snake = Snake()
scoreboard = Scoreboard()
food = Food(snake.segments)

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
            food.refresh(snake.segments)
            snake.extend()
        
    else:
        if snake.explode_count < 20:
            snake.explode()
        else:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
