from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# disable tracer
screen.tracer(0)

# get paddles
player_1_paddle = Paddle("left")
player_2_paddle = Paddle("right")

# create ball
ball = Ball()

# create scoreboard
scoreboard = ScoreBoard()

# listen for events
screen.listen()
screen.onkey(key="Up", fun=player_2_paddle.go_up)
screen.onkey(key="Down", fun=player_2_paddle.go_down)
screen.onkey(key="w", fun=player_1_paddle.go_up)
screen.onkey(key="s",fun=player_1_paddle.go_down)

# start game
game_is_on = True

while game_is_on:
    # update screen - required if tracer is disabled.
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collission with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect collission with right paddle
    if (ball.distance(player_2_paddle) < 50 and ball.xcor() > 320) or (ball.distance(player_1_paddle) < 50 and ball.xcor() < -320):
        # needs to bounce
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        

    # detect when left paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()





# exit screen on click
screen.exitonclick()