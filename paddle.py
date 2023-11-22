from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position = "left") -> None:
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        if position == "left":
            self.goto(-350,0)
        elif position == "right":
            self.goto(350,0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        