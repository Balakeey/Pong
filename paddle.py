from turtle import Turtle

POSITIONS = [(350, 0), (-350, 0)]

class Paddle():
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def go_up(self):
            if self.paddle.xcor() < 0:
                new_y = self.paddle.ycor() + 20
                self.paddle.goto(-350, new_y)
            else:
                new_y = self.paddle.ycor() + 20
                self.paddle.goto(350, new_y) 

    def go_down(self):
            if self.paddle.xcor() < 0:
                new_y = self.paddle.ycor() - 20
                self.paddle.goto(-350, new_y)
            else:
                new_y = self.paddle.ycor() - 20
                self.paddle.goto(350, new_y)
