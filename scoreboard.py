from turtle import Turtle
X_CORR = 0
Y_CORR = 270
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        print(self.highscore)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(X_CORR, Y_CORR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", 'w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",False,  ALIGNMENT, FONT)

    def refresh(self):
        self.score += 1
        self.update_scoreboard()
