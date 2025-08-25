from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Set food appearance
        self.shape("circle")
        self.penup()                                   # Prevent drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the circle smaller
        self.color("blue")
        self.speed("fastest")                          # Fastest speed for instant placement
        self.refresh()                                 # Place food at a random location initially

    def refresh(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
