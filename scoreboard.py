from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)



    def increase_score(self):
        self.score += 1
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", font=FONT)