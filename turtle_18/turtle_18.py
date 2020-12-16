import turtle as t
from turtle import Screen

import random
tim = t.Turtle()
t.colormode(255)

# tim.shape("turtle")
# tim.color("red")
#
# #Moving
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
DEGREES = 360


def draw_shape(num_of_sides : int):

    degree_angle = DEGREES / num_of_sides
    for i in range(0, num_of_sides):
        tim.right(degree_angle)
        tim.forward(100)

color_scheme = ['red', 'green', 'blue', 'black', 'brown']

# for side in range(3, 11):
#     tim.color(random.choice(color_scheme))
#     draw_shape(side)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk(iterations: int):
    tim.speed(0)
    for _ in range(iterations):
        direction = [0, 90, 180, 270]
        tim.pensize(5)
        # tim.color(random.choice(color_scheme))
        tim.color(get_random_color())
        # tim.right(random.choice(walk_angle))
        tim.setheading(random.choice(direction))
        tim.forward(20)


# random_walk(100)

def draw_circle(radius):
    tim.speed(0)
    tim.color(get_random_color())
    tim.circle(radius)


number_of_circles = 80
degree_angle = DEGREES / number_of_circles
for i in range(0, number_of_circles):
    tim.setheading(tim.heading() + degree_angle)
    draw_circle(100)



screen = Screen()
screen.exitonclick()