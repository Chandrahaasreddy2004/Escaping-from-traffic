A=1
FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write("Level:1",align="center",font=FONT)

    def update_scoreboard(self):
        self.clear()
        global A
        A+=1
        self.write(f"Level:{A}", align="center", font=FONT)

    def looses(self):
        self.goto(0,0)
        self.write("GAME OVER.TRY AGAIN!....",align="center",font=FONT)




