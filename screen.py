import turtle


class Screen:

    def __init__(self):
        self.screen = turtle.Screen()

    def create(self):
        self.screen.setup(width=750, height=750)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()

    def move(self, key, fun):
        self.screen.onkey(key=key, fun=fun)

    def exit(self):
        self.screen.exitonclick()
