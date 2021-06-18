from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.set_pos()

    def set_pos(self):
        x_pos = random.randint(-250, 250)
        y_pos = random.randint(-250, 250)
        self.goto(x_pos, y_pos)
