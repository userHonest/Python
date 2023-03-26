# 18/03/23

from turtle import *
import random


def draw_square(x, y, s):
    penup()
    goto(x - s / 2, y - s / 2)
    pendown()
    fillcolor("black")
    begin_fill()
    for i in range(4):
        forward(s)
        left(90)
    end_fill()


def draw_grid():
    clear()  # clear the canvas

    # set up the turtle
    bgcolor("grey")
    pencolor("grey")
    width(2)
    hideturtle()
    tracer(False)

    # nested loop main grid
    noise = 5
    size = 100
    shrink = 15

    for x in range(-400 + size // 2, 400, size):
        for y in range(-400 + size // 2, 400, size):
            # main, this is to move the angles
            draw_square(x, y, size)

            # determining the offsets
            x_off = random.uniform(-noise, noise)
            y_off = random.uniform(-noise, noise)

            # drawing inner squares
            for i in range(6):
                draw_square(x + i * x_off, y + i * y_off, size - i * shrink)

    tracer(True)  # turn on animation
    update()  # update the screen


setup(600, 600)
draw_grid()  # draw the grid initially

# redraw function
def redraw():
    draw_grid()

# listen for key presses
onkeypress(redraw, "space")
listen()

exitonclick()
