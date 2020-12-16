import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
t.colormode(255)


def get_random_color():
    rgb_colors = [(239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]
    return random.choice(rgb_colors)


def draw_hirsh(number_of_dots):
    """
    10 x 10 spots
    size of the dot should be 20.
    dots should be spaced apart by 50.
    """
    tim.hideturtle()
    tim.penup()
    tim.setheading(330)
    tim.forward(300)
    tim.setheading(0)
    tim.pendown()
    for _ in range(number_of_dots):
        heading = tim.heading()
        if heading == 0:
            tim.setheading(180)
        else:
            tim.setheading(0)
        # Paint the horizontal dot
        for _ in range(number_of_dots):
            tim.dot(20, get_random_color())
            tim.penup()
            tim.forward(50)
        tim.backward(50)
        earlier_heading = tim.heading()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(earlier_heading)


draw_hirsh(10)
screen = Screen()
screen.exitonclick()
