from paddle import Paddle, Paddle_r
from turtle import Screen
from scoreboard import Scoreboard as sb

screen = Screen()
screen = Screen()
screen.screensize(400,400)
screen.bgcolor('black')


paddle = Paddle()
paddle.user()


r_paddle = Paddle_r()
r_paddle.user()


scoreboard = sb()

screen.listen()
screen.onkeypress(paddle.up, "w")
screen.onkeypress(paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")



game_is_on = True

while game_is_on:
    screen.update()
    if paddle.paddle.ycor()>350:
        paddle.opposite()
    if paddle.paddle.ycor()<-350:
        paddle.opposite()


