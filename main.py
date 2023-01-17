import turtle
import random
import time

screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(height = 700, width= 700)
screen.tracer(0)
turtle.bgcolor('black')
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 300)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()

snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('cyan')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

food= turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('light green')
food.penup()
food.goto(30, 30)

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 300)
score.write('Score :', align="center", font=("Courier", 24, "bold"))

def snake_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

screen.listen()
screen.onkeypress(snake_up, "Up")
screen.onkeypress(snake_down, "Down")
screen.onkeypress(snake_left, "Left")
screen.onkeypress(snake_right, "Right")

point = 0
delay = 0.1
old_fruit = []

while True:
    screen.update()
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        score.clear()
        point += 1
        score.write("Score :{}".format(point), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('light green')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('black')
        score.goto(0, 0)
        score.write("Game Over. \n Your Score is: {}".format(point), align="center", font=("Courier", 24, "bold"))
    for food1 in old_fruit:
        if food1.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('black')
            score.goto(0, 0)
            score.write("Game Over. \n Your Score is: {}".format(point), align="center", font=("Courier", 24, "bold"))
            
    time.sleep(delay)

turtle.Terminator()