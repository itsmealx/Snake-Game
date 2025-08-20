from turtle import Turtle

class Scoreboard(Turtle):
    """Displays the current and status of the game."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as high_score:
            self.highest_score = int(high_score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """Displays the current score at the top of the screen."""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highest_score}", align="center", font=("Arial", 15, "normal"))

    def add_score(self):
        """Increase the score by 1 and update the score written on top."""
        self.score += 1
        self.update_score()

    def restart(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("high_score.txt" , mode="w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_score()
