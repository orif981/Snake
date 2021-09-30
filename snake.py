import turtle
from turtle import Turtle
MOVE_DISTANCE = 20
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor((0, 0, 0))
screen.title("Snake")
screen.listen()
turtle.colormode(255)
turtle.tracer(0)
starting_pos = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()

    def last_seg_cors(self):
        return self.seg[-1].xcor(),self.seg[-1].ycor()

    def create_snake(self):
        for item in starting_pos:
            self.add_seg(item[0],item[1])

    def add_seg(self,x,y):
        segment = Turtle("square")
        segment.color("white")
        segment.pu()
        segment.goto(x,y)
        self.seg.append(segment)

    def left(self):
        if self.seg[0].heading() != 0:
            self.seg[0].seth(180)

    def up(self):
        if self.seg[0].heading() != 270:
            self.seg[0].seth(90)

    def down(self):
        if self.seg[0].heading() != 90:
            self.seg[0].seth(270)

    def right(self):
        if self.seg[0].heading() != 180:
            self.seg[0].seth(0)

    def move(self):
        self.x,self.y=self.last_seg_cors()
        for i in range(len(self.seg)-1, 0, -1):
            self.seg[i].goto(self.seg[i-1].pos())
        screen.onkeypress(self.right, "d")
        screen.onkeypress(self.up, "w")
        screen.onkeypress(self.down, "s")
        screen.onkeypress(self.left, "a")
        self.seg[0].forward(MOVE_DISTANCE)

    def extend(self):
        self.add_seg(self.x,self.y)




if __name__ == '__main__':
    pass
