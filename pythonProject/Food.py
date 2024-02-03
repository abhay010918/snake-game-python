from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        # Initialize the food with specific attributes and call the refresh method to set its initial position
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Set a new random position for the food within specified boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
