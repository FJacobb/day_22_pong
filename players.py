from turtle import Turtle
speed = 25


class Paddle(Turtle):
    def __init__(self, list):
        super().__init__()
        self.position = list
        self.box()
        self.hideturtle()
    def box(self):
        for pos in self.position:
            name = Turtle()
            name.penup()
            name.shape("image/player1.gif")
            name.goto(pos)
            name.setheading(90)
            name.color("#ffffff")
            self.player = name
    def move_up(self):
        self.player.setheading(90)
        self.player.forward(speed)


    def move_down(self):
        self.player.setheading(270)
        self.player.forward(speed)