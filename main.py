import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen SETUP
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False) #locks the window for resizing
screen.bgcolor("black")
screen.tracer(0)

#object construction
snake = Snake()
food = Food()
score = Scoreboard()


#movement controls
screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")

is_game_over= False

while not is_game_over:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detecting collision with food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        snake.change_snake_color(food.food_color())
        food.refresh()
        score.add_score()

    #Detecting collision with wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -285 or
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        score.restart()
        snake.reset_snake()
        food.refresh()

    #Detecting collision with tail
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.restart()
            snake.reset_snake()
            food.refresh()


screen.exitonclick()