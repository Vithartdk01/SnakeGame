from turtle import Turtle
score=0
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}",align='center',
                   font=("CamSan",12,"normal"))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}", align='center',
                   font=("CamSan", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",align='center',
                   font=("Arial", 18, "normal"))

    def add_score(self):
           self.score+=1
           self.clear()
           self.update_score()