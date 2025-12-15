import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen  = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

paddle_right = Paddle(x_location=350, color="blue")
paddle_left = Paddle(x_location=-350, color="red")

ball = Ball()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

scorecard = Scorecard()

is_game_on = True

while is_game_on:
    ball.move()
    time.sleep(ball.move_speed)

    ## to check whether ball hits paddle and reverse it
    if ball.distance(paddle_right) < 50  and  ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.reverse()
        ball.move_speed *= 0.9
        time.sleep(ball.move_speed)

    ## check ball going out of bound, update the score
    if ball.xcor() > 380 or ball.xcor() < -380:
        scorecard.update_score(ball.xcor())
        ball.goto(0,0)
        ball.reverse()
        ball.move_speed = 0.1
        time.sleep(ball.move_speed)

screen.exitonclick()