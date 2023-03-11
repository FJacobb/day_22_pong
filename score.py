from turtle import Turtle
class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.hideturtle()
        self.color("#ffffff")
        self.penup()
        self.text()


    def text(self):
        self.clear()
        self.goto(0, 170)
        self.write(f"{self.player1}   {self.player2}",True,align="center",font=("Copperplate Gothic Bold", 20,"bold"))


    def player_1(self):
        self.player1+=1
        self.text()

    def player_2(self):
        self.player2 +=1
        self.text()