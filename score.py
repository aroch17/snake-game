from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score = 0
        with open("data.txt") as file:
            # Reads high score from file
            self.high_score = int(file.read())
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Writes the high score in the file
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()
