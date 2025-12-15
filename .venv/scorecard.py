from turtle import Turtle


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()

        self.goto(0,270)
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"RED: {self.left_score} || BLUE: {self.right_score}", align="center", font=('Arial', 24, 'normal'))

    def update_score(self, ball_x_position):
        # x position is negative then ball touches left so right score increase
        if ball_x_position < 0:
            self.right_score += 1
        else:
            self.left_score += 1
        self.write_score()