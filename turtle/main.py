from turtle import Turtle,Screen, pencolor, title
import random

screen=Screen()

colors=["violet","blue","green","yellow","orange","red"]

y_pos=[-200,-125,-50,25,100,175]

screen.setup(width=500,height=500)

all_turt=[]

is_on=True

user_bet=screen.textinput(title="Make your bet",prompt="which color turtle will win the race? Enter your choice: \n violet,blue,green,yellow,orange,red")
if user_bet:
    for i in range(0,6):
        tim=Turtle(shape="turtle")
        tim.color(colors[i])
        tim.penup()
        tim.goto(x=-200,y=y_pos[i])
        all_turt.append(tim)
    while is_on:
    
        for tim in all_turt:
            if tim.xcor()>220:

                is_on=False

                win_turt=tim.pencolor()

                if user_bet==win_turt:

                    print(f"Congratulation! you win")
                    break
                    
                else:

                    print(f"You loose! Winning Turtle is {win_turt} ")
                    break

            dis=random.randint(1,10)

            tim.forward(dis)
else:
    print("Enter your bet")      

screen.exitonclick()


# Author:- Amit Yadav