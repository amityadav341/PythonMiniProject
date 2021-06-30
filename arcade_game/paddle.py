from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,p):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5.0,stretch_len=1.0)
        self.color("white")
        self.penup()
        self.goto(p)
    def go_up(self):
        new_y=self.ycor()+30
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-30
        self.goto(self.xcor(),new_y)


# Author:- Amit Yadav
