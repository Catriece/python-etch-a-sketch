from turtle import Turtle, Screen

joe = Turtle ()
screen = Screen()


def move_forwards():
    joe.forward(10)


def move_backwards():
    joe.backward(10)


def move_clockwise():
    joe.right(10)


def move_counter_clockwise():
    joe.left(10)


def clear_screen():
    joe.clear()
    joe.penup()
    joe.speed("fastest")
    joe.home()
    joe.pendown()





screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()