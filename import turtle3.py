import turtle
import math
import random

def draw_colored_circular_text(text, radius):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.speed(2)
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()

    angle_per_char = 360 / len(text)

    for char in text:
        color = random.choice(colors)
        turtle.color(color)
        turtle.write(char, align="center", font=("Arial", 14, "bold"))
        turtle.forward(radius * math.pi / 180 * angle_per_char)
        turtle.right(angle_per_char)

def animate_colored_circular_text(text, radius):
    for _ in range(360):
        turtle.clear()
        draw_colored_circular_text(text, radius)
        turtle.right(1)
        turtle.update()

    turtle.hideturtle()
    turtle.done()

text_to_display = "Jai Shree Ram"
radius_of_circle = 100
turtle.Screen().tracer(0)
animate_colored_circular_text(text_to_display, radius_of_circle)