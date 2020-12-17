from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
    # tim.setheading(0)
    # tim.forward(10)


def move_backwards():
    tim.backward(10)
    # tim.setheading(180)
    # tim.forward(10)


def clear_drawing():
    tim.reset()


def move_clockwise():
    current_heading = tim.heading()
    current_heading += 10
    tim.setheading(current_heading)


def move_counter_clockwise():
    current_heading = tim.heading()
    current_heading -= 10
    tim.setheading(current_heading)


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counter_clockwise)

screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()