import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self, highest_score):
        super().__init__()
        self.score = 0
        self.highest_score = highest_score

    def show_score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 347.5)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))
        self.setposition(0, 327.5)
        self.color("white")
        self.write(arg=f"Highest Score: {self.highest_score}", move=False, align="center",
                   font=("Courier", 20, "normal"))

    def get_point(self):
        self.score += 1

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over!", move=False, align="center", font=("Courier", 40, "normal"))
        self.goto(0, -40)
        self.write(arg=f"Final Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))
        self.score = 0

    def highest(self):
        return self.highest_score
