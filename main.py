from snake import Snake
from screen import Screen
from food import Food
from scoreboard import ScoreBoard

import time

with open("highest_score.txt") as file1:
    highest_score = int(file1.read())

screen = Screen()
screen.create()

snake = Snake()
food = Food()
score_board = ScoreBoard(highest_score)
score_board.show_score()

screen.listen()
screen.move(key="Up", fun=snake.up)
screen.move(key="Down", fun=snake.down)
screen.move(key="Left", fun=snake.left)
screen.move(key="Right", fun=snake.right)


def reset():
    score_board.reset()
    score = score_board.highest()
    with open("highest_score.txt", mode="w") as file2:
        if score > highest_score:
            file2.write(str(score))
        else:
            file2.write(str(highest_score))

    score_board.game_over()
    time.sleep(0.75)
    score_board.show_score()
    snake.reset()
    food.refresh()


snake_game = True
while snake_game:
    time.sleep(0.075)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        score_board.get_point()
        score_board.show_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        reset()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            reset()

screen.exit()
