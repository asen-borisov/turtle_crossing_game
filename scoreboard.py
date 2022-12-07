FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.lvl}", align="left", font=FONT)

    def lvl_inc(self):
        self.lvl += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)



