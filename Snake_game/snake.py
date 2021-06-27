from turtle import Turtle
seg_pos=[(0,0),(-20,0),(-40,0)]
mov_dis=20
class Snake:
     def __init__(self):
         self.segments=[]
         self.create_snake()
        
     def create_snake(self):
         for pos in seg_pos:
             self.add_segment(pos)
            
     def add_segment(self,pos):
         new_segment=Turtle(shape="square")
         new_segment.color("white")
         new_segment.penup()
         new_segment.goto(pos)
         self.segments.append(new_segment)
         
     def extend(self):
         self.add_segment(self.segments[-1].position())

     def move(self):
         for s in range(len(self.segments)-1,0,-1):
                new_seg_x=self.segments[s-1].xcor()
                new_seg_y=self.segments[s-1].ycor()
                self.segments[s].goto(new_seg_x,new_seg_y)
         self.segments[0].forward(mov_dis)

     def up(self):
         if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
     def down(self):
         if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
     def left(self):
         if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
     def right(self):    
         if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
                

# Author:- Amit Yadav