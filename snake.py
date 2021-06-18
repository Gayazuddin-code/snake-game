from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = list()
        self.x_pos = 20
        self.create_snake()
        self.head = self.snake_body[0]
        self.move_speed = 0.1

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("cyan")
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.move_speed = 0.1

    def extend_snake(self):
        self.add_snake(self.snake_body[-1].position())
        self.move_speed *= 0.9

    def snake_move(self):
        for square_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[square_num - 1].xcor()
            new_y = self.snake_body[square_num - 1].ycor()
            self.snake_body[square_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def move_up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
