from turtle import Turtle

# Text alignment and font settings
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()              # Hide the turtle cursor (only show text)
        self.goto(0, 270)              # Position at the top of the screen
        self.score = 0
        self.new_score()               # Display the initial score

    def increase(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.clear()                   # Clear the previous score text
        self.new_score()               # Write the new score

    def new_score(self):
        """Write the current score on the screen."""
        self.write(align=ALIGNMENT, arg=f"Score: {self.score}", font=FONT)

    def game_over(self):
        """Display 'Game Over' message in the center of the screen."""
        self.goto(0, 0)
        self.write(align=ALIGNMENT, arg="Game Over", font=FONT)
