import random
from turtle import Turtle

#rainbow colors for updating the food color and snake's color
#can use RGB or other type for a wide variety of colors
colors = ["red",  "orange", "yellow", "green", "blue", "indigo", "violet"]

class Food(Turtle):
    """Inherits from the Turtle class and display food at random loc in the canvas."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=.75, stretch_len=.75) #making the size to 10x10 pixels
        self._current_color = "white" #default color
        self.refresh()

    def refresh(self):
        """Refreshes the food color and location."""
        self._current_color = random.choice(colors)
        self.color(self._current_color)
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(random_x_pos, random_y_pos)

    def food_color(self):
        """Returns the current food color and be used as an argument for the change_snake_color method."""
        return self._current_color
