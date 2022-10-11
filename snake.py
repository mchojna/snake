import turtle


class Snake:

    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        x_cor = 0
        y_cor = 0
        for _ in range(3):
            segment = turtle.Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setpos(x=x_cor, y=y_cor)
            self.body.append(segment)
            x_cor -= 20

    def reset(self):
        for segment in self.body:
            segment.hideturtle()
        self.body.clear()
        self.create()
        self.head = self.body[0]

    def extend(self):
        segment = turtle.Turtle(shape="square")
        segment.penup()
        segment.setposition(self.body[-1].position())
        segment.color("white")
        self.body.append(segment)

    def move(self):
        for segment_index in range(len(self.body) - 1, 0, -1):
            new_x_cor = self.body[segment_index - 1].xcor()
            new_y_cor = self.body[segment_index - 1].ycor()
            self.body[segment_index].goto(new_x_cor, new_y_cor)
        self.body[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
