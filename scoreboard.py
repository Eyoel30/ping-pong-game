from turtle import Turtle
FONT = "Courier", 80, "normal"
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.w_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"{self.l_score}:{self.w_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def w_point(self):
        self.w_score += 1
        self.update_scoreboard()
