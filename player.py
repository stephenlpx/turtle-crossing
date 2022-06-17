from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):
    #inheriting the functionality from the turtle class
    #creating our player to start at the bottom of the screen
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    



