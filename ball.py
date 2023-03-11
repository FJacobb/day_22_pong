from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("image/ball.gif")
        self.shapesize(0.5)
        self.speed(0.9)
        self.y = 5
        self.x = 5
        self.delay = 0.04
    def reset_ball(self):
        self.goto(0,0)
        self.delay = 0.04

    def move(self,paddle1,paddle2):
        if self.ycor() > 190 :
            self.y = -3
        elif self.ycor()<=-185:
            self.y = 3
        if self.distance(paddle1.player) <30 and self.xcor()<-265 or self.distance(paddle2.player) <30and self.xcor()>265:
            self.x *=-1
            if self.delay>0.015:
                self.delay-=0.002



        self.goto(self.xcor() - self.x, self.ycor() + self.y)
