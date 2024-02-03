from turtle import Screen
from Food import food
import time
from Snake import Snake
from Scoregaurd import scoregaurd

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off animation
screen.tracer(0)

# Create the Snake, Food, and Scoregaurd objects
snake = Snake()
Food = food()
Scoregaurd = scoregaurd()

# Listen for key events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()

    # Pause for a short duration to control the speed of the game
    time.sleep(0.1)

    # Move the snake
    snake.move()

    # Check if the snake has eaten the food
    if snake.head.distance(Food) < 15:
        Food.refresh()
        snake.extend()  # Extend the snake
        Scoregaurd.increase_score()

    # Detecting wall collision
    if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
    ):
        game_is_on = False
        Scoregaurd.game_over()

    # Check for collision with the body segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Scoregaurd.game_over()

# Close the turtle graphics window when the game ends
screen.exitonclick()
