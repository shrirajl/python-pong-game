from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.x_increase = 10
        self.y_increase = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_increase
        new_y = self.ycor() + self.y_increase
        self.goto(new_x, new_y)
        ## top and bottom bounce logic
        if new_y > 280 or new_y < -280:
           # new_x = self.xcor() - 10
            self.y_increase *= -1

        # if self.ball_direction == "UP":
        #     new_y = self.ycor() + 10
        # else:
        #     new_y = self.ycor() - 20

    def reverse(self):
        self.x_increase *= -1


