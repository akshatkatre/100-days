from turtle import Screen
import time
from pong_game_22.paddle import Paddle
from pong_game_22.ball import Ball
from pong_game_22.scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

screen.listen()

right_paddle = Paddle(x_position=350, y_position=0)
left_paddle = Paddle(x_position=-350, y_position=0)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect Top Wall and Bottom Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        print("hit the paddle")
        ball.bounce_x()

    # Detect right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    # Detect left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()
