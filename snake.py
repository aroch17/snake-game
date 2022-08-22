from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_parts = []
        self.create_body()
        self.head = self.body_parts[0]

    def create_body(self):
        # creates the main body of the snake
        x_cor = 0
        for _ in range(3):
            self.add_part(x_cor)
            x_cor -= 20

    def add_part(self, x_position, y_position=0):
        # adds one new part to the snake body
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(x_position, y_position)
        self.body_parts.append(new_part)

    def extend(self):
        # creates a new part of the snake at the last part's location
        x_position = self.body_parts[-1].xcor()
        y_position = self.body_parts[-1].ycor()
        self.add_part(x_position, y_position)

    def move(self):
        # we move the snake by position swapping
        # the last body piece gets the position of th second last and so on
        # we use this method so that it is easier to turn our snake
        for body_part in range(len(self.body_parts) - 1, 0, -1):  # range does not include 0
            new_x_cor = self.body_parts[body_part - 1].xcor()
            new_y_cor = self.body_parts[body_part - 1].ycor()
            self.body_parts[body_part].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        # Sends the dead snake off the screen
        for part in self.body_parts:
            part.goto(1000, 1000)
        self.body_parts.clear()
        self.create_body()
        self.head = self.body_parts[0]

    def up(self):
        # we use this logic so that the snake does not turn back on itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
