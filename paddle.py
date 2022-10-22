from turtle import Turtle, Screen
from turtle import Screen
paddle = []
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
screen = Screen()

class Paddle:

    def __init__(self):
        pass

    def user(self):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.turtlesize(1,4,1)
        self.paddle.goto(-270,0)
        self.paddle.setheading(UP)
        self.distance = 0

    def up(self):
        self.paddle.forward(MOVE_DISTANCE)

    def down(self):
        self.paddle.forward(-MOVE_DISTANCE)
    def opposite(self):
        self.distance = -(self.distance)

class Paddle_r(Paddle):

    def __init__(self):
        pass

    def user(self):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.turtlesize(1,4,1)
        self.paddle.goto(270,0)
        self.paddle.setheading(UP)
        self.distance = 0

    def up(self):
       self.paddle.forward(MOVE_DISTANCE)
    def down(self):
       self.paddle.forward(-MOVE_DISTANCE)

    def opposite(self):
        self.distance = -(self.distance)








