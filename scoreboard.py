from turtle import Turtle

class Scoreboard(Turtle):
    """Displays the current and status of the game."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Displays the current score at the top of the screen."""
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def add_score(self):
        """Increase the score by 1 and update the score written on top."""
        self.score += 1
        self.clear() #clearing the previous drawing
        self.update_score()

    def game_over(self):
        """Triggered when the game is over. i.g. collision with head or tail."""
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=("Arial", 15, "normal"))