# Snake Game - Main File
# ----------------------
# This file runs the main game loop and connects all components:
# Snake, Food, and Scoreboard.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup the game screen
screen = Screen()
screen.setup(width=600, height=600)   # Window size
screen.bgcolor("black")               # Background color
screen.title("Snake Game")            # Window title
screen.tracer(0)                      # Turn off auto updates (manual control)

# Create game objects
snake = Snake()
food = Food()
score_board = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkey(fun=snake.up , key="Up")
screen.onkey(fun=snake.down , key="Down")
screen.onkey(fun=snake.left , key="Left")
screen.onkey(fun=snake.right , key="Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()                   # Refresh screen
    time.sleep(0.1)                   # Control game speed
    snake.move()                      # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()                # Move food to a new random location
        snake.extend()                # Add a new segment to the snake
        score_board.clear()           # Clear previous score
        score_board.increase()        # Update the score

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score_board.game_over()
        game_is_on = False

    # Detect collision with self
    for segments in snake.snake_segments:
        if snake.head.distance(segments) < 10 and segments != snake.head:
            game_is_on = False
            score_board.game_over()

# Exit on mouse click
screen.exitonclick()
