from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
ball = Ball()
scoreboard = ScoreBoard()
paddle_player1 = Paddle(-350, 0)
paddle_player2 = Paddle(350, 0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG!")
screen.listen()
screen.onkey(paddle_player1.go_up, "w")
screen.onkey(paddle_player1.go_down, "s")
screen.onkey(paddle_player2.go_up, "Up")
screen.onkey(paddle_player2.go_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    scoreboard.update_scoreboard()
    screen.update()
    ball.move()
    # Detech Wall collison
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detech right padddle collision
    if ball.distance(paddle_player2) < 50 and ball.xcor() > 320 or ball.distance(paddle_player1) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_score1()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_score2()


screen.exitonclick()

