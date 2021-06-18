from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()


def on_close():
    global game_is_on
    game_is_on = False


root.protocol("WM_DELETE_WINDOW", on_close)

screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("medium orchid")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True

while game_is_on:
    if not game_is_on:
        break
    screen.update()
    time.sleep(snake.move_speed)
    snake.snake_move()
    # collision with food
    if snake.head.distance(food) < 17:
        snake.extend_snake()
        food.set_pos()
        scoreboard.increase_score()
    # collision with borders
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_turtle()
        snake.reset()
    # collision with body
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset_turtle()
            snake.reset()
