from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        


    def update_scoreboard(self):
        self.clear()
        self.goto(-200,160)
        self.write(self.l_score, font=("Courier", 80, "normal"))
        self.goto(200,160)
        self.write(self.r_score, font=("Courier", 80, "normal"))


    def l_point(self):
        self.l_score += 1   
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
