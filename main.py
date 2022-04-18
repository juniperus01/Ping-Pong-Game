'''
Objectives:
1. Create the screen
2. Create two paddles
3. Move the two paddles
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score
'''
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 1. create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# To draw the dashed line net
tim = Turtle()
tim.right(90)

for _ in range(14):
    tim.color("white")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.hideturtle()
tim.penup()
tim.goto(0, 0)
tim.left(180)
for _ in range(14):
    tim.color("white")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.hideturtle()

# 2. Create two paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 3. Move the paddles
screen.listen()
# for r_paddle we choose up and down arrow keys to go up and down
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# for l_paddle we choose w and s keys to go up and down
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# 4. Create the ball
ball = Ball()

# 8. Keep scores
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # 4. Making ball move
    ball.move()

    # 5. Detect collision with wall and move
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 6. Detect collision of ball with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 55:
        ball.bounce_x()
        
    if ball.xcor() < -320 and ball.distance(l_paddle) < 55:
        ball.bounce_x()

    # 7. Detect if r_paddle misses the ball
    if ball.xcor() > 410: # goes completely out of the frame
        ball.reset_position()
        scoreboard.l_point()
    # 7. Detect if l_paddle misses the ball
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()