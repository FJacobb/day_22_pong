from turtle import Screen
from players import Paddle
from ball import Ball
from time import sleep
from score import Score
screen = Screen()
screen.bgpic("image/background_1.png")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)
screen.addshape("image/ball.gif")
screen.addshape("image/player1.gif")

player1 = Paddle([(-285,0)])
player2 = Paddle([(280,0)])
ball = Ball()
score =Score()

screen.listen()



play_game = True


screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")
while play_game:

    sleep(ball.delay)
    ball.move(player1,player2)
    if ball.xcor() > 300:
        score.player_1()
        ball.reset_ball()
    elif ball.xcor()<-300:
        score.player_2()
        ball.reset_ball()
    screen.update()
screen.exitonclick()