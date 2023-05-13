from turtle import Turtle, Screen

screen = Screen()
screen.title("Cacth The Turtle Game")
screen.bgcolor("black")


def score_turtle():
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.color("#ffb310")
    t.goto(0, (screen.window_height() / 2) * 0.9)
    t.write(arg="Score 0", move=False, align="center", font=("Arial", 18, "bold"))


def make_turtle(x, y):
    t = Turtle()
    t.penup()
    t.color("#ffb310")
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x*10, y*10)


score_turtle()
make_turtle(-20, 20)

screen.mainloop()
