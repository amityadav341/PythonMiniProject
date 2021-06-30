from turtle import Turtle, write
class Scoreboard(Turtle):
    def __init__(self,user1,user2):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_scoreboard(user1,user2)
        
    def update_scoreboard(self,user1,user2):
        self.clear()
        self.goto(-50,270)
        self.write(f"{user1}:{self.lscore}",align="center",font=("Courier",20,"normal"))
        self.goto(100,270)
        self.write(f"{user2}:{self.rscore}",align="center",font=("Courier",20,"normal"))
    
    def l_point(self,user1,user2):
        self.lscore+=1
        self.update_scoreboard(user1,user2)
        return self.lscore
    def r_point(self,user1,user2):
        self.rscore+=1
        self.update_scoreboard(user1,user2)
        self.rscore
        return self.rscore
    def winner(self,user):
        self.color("white")
        self.goto(0,0)
        self.write(f"Game Over : Winner is {user}",align="center",font=("Courier",20,"normal"))


# Author:- Amit Yadav