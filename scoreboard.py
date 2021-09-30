from turtle import Turtle


FONT=("Courier", 20, "normal")
class ScoreBoard(Turtle):

    score=0

    def __init__(self):
        super().__init__()
        self.pu()
        self.color((0,255,200))
        self.goto(0,250)
        self.write(f"Score: {self.score}", False, "center", FONT)
        self.hideturtle()

    def game_over(self):
       self.setpos(0,0)
       self.write("GAME OVER", False, "center", FONT)
       self.pu()
       self.hideturtle()
       self.color("white")

    def rewrite(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)