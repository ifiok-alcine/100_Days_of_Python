from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.go_to_start()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finished_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
