import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)