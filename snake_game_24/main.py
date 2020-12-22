from turtle import Screen
from snake_game_24.snake import Snake
from snake_game_24.food import Food
from snake_game_24.scoreboard import ScoreBoard
import time

SLEEP_TIME = 0.15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('The Snake Game')
screen.tracer(0)

screen.listen()

snake = Snake()
food = Food()
game_scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        game_scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_scoreboard.reset_scoreboard()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_scoreboard.reset()
            snake.reset_scoreboard()

screen.exitonclick()