from turtle import Turtle, Screen
screen = Screen()

#constants for starting position and snake movement
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self._create_snake()
        self.snake_head = self.snake[0]

    def _create_snake(self):
        """Create three segments for the snake's initial body."""
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        """Add segment for the snake's body."""
        snakey = Turtle(shape="square")
        snakey.color("white")
        snakey.penup()
        snakey.goto(position)
        self.snake.append(snakey)

    def extend(self):
        """Extends the length of the snake."""
        self.add_segment(self.snake[-1].position())

    def move(self):
        """
        Allows the snake to move automatically.
        :return: None
        """
        # Update body segments: each one moves to the position of the segment before it.
        # This ensures the snake's body follows smoothly behind the head.
        # Finally, move the head forward to complete the step.
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x_pos = self.snake[segment - 1].xcor()
            new_y_pos = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x_pos, new_y_pos)

        self.snake_head.forward(20)

    #movement controls for the game
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def change_snake_color(self, food_color):
        """Changes the snake color based on the food current color."""
        #no ripple effect
        # for segment in self.snake:
        #     segment.color(food_color)

        # adds ripple effect
        for i, segment in enumerate(reversed(self.snake)):
            screen.ontimer(lambda s=segment: s.color(food_color), i * 100)

    def reset_snake(self):
        """Initialize the snake again if game is over."""
        for s in self.snake:
            s.reset() #clears the drawing from the screen
        self.snake.clear()
        self._create_snake()
        self.snake_head = self.snake[0]


