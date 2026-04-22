import turtle
import math

def draw_circular_text(text, radius):
    turtle.speed(1)
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()

    angle_per_char = 360 / len(text)

    for char in text:
        turtle.write(char, align="center", font=("Arial", 12, "normal"))
        turtle.forward(radius * math.pi / 180 * angle_per_char)
        turtle.right(angle_per_char)

    turtle.hideturtle()
    turtle.done()

text_to_display = "Jai Shree Ram"
radius_of_circle = 100
draw_circular_text(text_to_display, radius_of_circle)