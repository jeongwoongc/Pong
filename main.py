from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    scoreboard.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() > -380:
        ball.bounce_x()
    
    # Detect out-of-bounds for right paddle
    if ball.xcor() > 380:  
        ball.outofbounds()
        scoreboard.update_r()

    # Detect out-of-bounds for left paddle
    if ball.xcor() < -380:
        ball.outofbounds()
        scoreboard.update_l()
        

screen.exitonclick()
