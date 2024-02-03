from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class scoregaurd(Turtle):
    def __init__(self):
        # Initialize the score and set up the appearance
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        # Update the displayed score on the screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Display the game over message at the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increase the score, clear the existing score display, and update the scoreboard
        self.score += 1
        self.clear()
        self.update_scoreboard()
