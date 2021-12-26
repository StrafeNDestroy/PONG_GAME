from turtle import Turtle
ALIGNMENT_PLAYER1 = "center"
ALIGNMENT_PLAYER2 = "center"
FONT = ("Courier", 80, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.goto(-100, 190)
        self.write(f"{self.score_player1}", move=False, align=ALIGNMENT_PLAYER1, font=FONT)
        self.goto(100, 190)
        self.write(f"{self.score_player2}", move=False, align=ALIGNMENT_PLAYER2, font=FONT)

    def increase_score1(self):
        self.score_player1 += 1
        self.clear()
        self.update_scoreboard()
    def increase_score2(self):
        self.score_player2 += 1
        self.clear()
        self.update_scoreboard()
