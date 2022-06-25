#Create snake class and move to oops
from turtle import Turtle
moves = 20
up = 90
left = 180
down = 270
right = 0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.penup()
        self.snake()
        self.head = self.segments[0]

    def snake(self):
        gap = 0
        for index in range(3):
           
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=gap,y=0)
            gap = gap - 20
            self.segments.append(new_segment)
    
    def add_segment(self):
        position = self.segments[-1].position()
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.move()

    def move(self):
        for segment_no in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_no - 1].xcor()
            new_y = self.segments[segment_no - 1].ycor()
            self.segments[segment_no].goto(new_x, new_y)
        self.head.forward(moves)
        
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(90)

        
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(180)

        
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(0)