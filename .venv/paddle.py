from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_location, color="white"):
        super().__init__()
        self.shape(name="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_location,y=0)
        self.color(color)
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)