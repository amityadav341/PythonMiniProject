from turtle import Turtle,Screen, position, textinput, width
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.title("Arcade Game")
screen.bgcolor("black")
screen.tracer(0)

user1=textinput(title="Arcade game",prompt="Enter name of player 1").upper()
user2=textinput(title="Arcade game",prompt="Enter name of player 2").upper()
r_paddle=Paddle((380,0))
l_paddle=Paddle((-385,0))

ball=Ball()
scoreboard=Scoreboard(user1,user2)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
l=0
r=0
is_game_on=True
while is_game_on:
     time.sleep(ball.move_speed)
     screen.update()
     ball.move()
     
     
     if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_x()
     if ball.distance(r_paddle)<50 and ball.xcor()>350 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.bounce_y()
     if ball.xcor()>380:
        l=scoreboard.l_point(user1,user2)
        ball.reset_position()
       
     if ball.xcor()<-380:
        r=scoreboard.r_point(user1,user2)
        ball.reset_position()

     if r==5:
         is_game_on=False
         scoreboard.winner(user2)
     if l==5:
         is_game_on=False
         scoreboard.winner(user1)
screen.exitonclick()


# Author:- Amit Yadav