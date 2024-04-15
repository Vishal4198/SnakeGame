from turtle import Turtle
import random

FOOD_COLOR = "red"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(FOOD_COLOR)
        self.speed(0)
        self.refresh()

    def refresh(self):
        randon_x = random.randint(-280, 280)
        randon_y = random.randint(-280, 280)
        self.goto(randon_x, randon_y)
