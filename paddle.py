from turtle import Turtle, Screen
from turtle import Screen
paddle = []
MOVE_DISTANCE = 20
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
        self.paddle.goto(-410,0)
        self.paddle.setheading(UP)
        self.distance = 0
    def move(self):
        self.paddle.forward(self.distance)
    def up(self):
       self.distance = 5
    def down(self):
        self.distance = -5

    def opposite(self):
        self.distance = -(self.distance)



class Computer:
    def __init__(self):
        pass
    def create(self):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.turtlesize(1, 4, 1)
        self.paddle.goto(410, 0)
        self.paddle.setheading(90)





