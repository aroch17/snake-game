from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# stops animation on the screen
# we do this so that the main body of the snake is built as a whole and not piece by piece
screen.tracer(0)

# initialising objects of main classes
food = Food()
snake = Snake()
score = Score()

# starts listening for events
screen.listen()

# moving the snake
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    # we will use this method to update the screen whenever required
    screen.update()
    # we use this so that the animation slows down a bit
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.new_pos()
        snake.extend()
        score.update_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        score.reset_score()
        snake.reset()

    # Detecting snake head collision with tail
    for part in snake.body_parts[1:]:  # head is not checked(list slicing)
        if snake.head.distance(part) < 10:
            # game_is_on = False
            score.reset_score()
            snake.reset()


screen.exitonclick()
