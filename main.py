import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Catch The Turtle Game")
screen.bgcolor("black")
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [15, 5, -5, -15]
turtle_list = []
score = 0
score_turtle = Turtle()
time_turtle = Turtle()
game_over = False


def score_turtles():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("#ffb310")
    score_turtle.goto(0, (screen.window_height() / 2) * 0.9)
    score_turtle.write(arg="Score 0", move=False, align="center", font=("Arial", 18, "bold"))


def count_time(time):
    global game_over
    time_turtle.hideturtle()
    time_turtle.penup()
    time_turtle.color("#ffb310")
    time_turtle.goto(0, (screen.window_height() / 2) * 0.8)
    time_turtle.clear()
    if time > 0:
        time_turtle.clear()
        time_turtle.write(arg=f"Time {time}", move=False, align="center", font=("Arial", 18, "bold"))
        screen.ontimer(lambda: count_time(time - 1), 1000)
    else:
        game_over = True
        time_turtle.clear()
        hide_turtle()
        time_turtle.write(arg="Game Over", move=False, align="center", font=("Arial", 18, "bold"))


def make_turtle(x, y):
    t = Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score {score}", move=False, align="center", font=("Arial", 18, "bold"))

    t.onclick(handle_click)
    t.penup()
    t.color("#ff0000")
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x*10, y*10)
    turtle_list.append(t)


def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtle():
    for t in turtle_list:
        t.hideturtle()


def show_turtle():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle, 500)


def start():
    turtle.tracer(0)
    score_turtles()
    setup_turtle()
    hide_turtle()
    show_turtle()
    count_time(10)
    turtle.tracer(1)


start()

screen.mainloop()
