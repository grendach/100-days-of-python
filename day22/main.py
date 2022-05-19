# 1. create a screen
from turtle import Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
# 2. Create and move  paddle #1
# 3. Create and move  paddle #2
# 4. Create the Ball and make it move
# 5. Detect collisioin with the wall and bounce
# 6. Detect collisioin with the ball
# 7. Detect when the paddle misses
# 8. Keep score
# 6. Game over
screen.listen()
screen.exitonclick()
