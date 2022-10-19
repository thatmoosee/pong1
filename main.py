from paddle import Paddle, Computer
from turtle import Screen
from scoreboard import Scoreboard as sb

screen = Screen()
screen = Screen()
screen.bgcolor('black')


paddle = Paddle()
paddle.user()

computer = Computer()
computer.create()

scoreboard = sb()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


game_is_on = True

while game_is_on:
    paddle.move()
    if paddle.paddle.ycor()>350:
        paddle.opposite()
    if paddle.paddle.ycor()<-350:
        paddle.opposite()


