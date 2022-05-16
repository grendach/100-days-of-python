##### Snake game ##########
from turtle import Turtle, Screen
from snake import Snake
import time

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# 1. Create sname body using class Snake object
snake = Snake()
# 2. Move the snake using arrow buttons

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

# 3. Create snake food
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail



screen.exitonclick()
