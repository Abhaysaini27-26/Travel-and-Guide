import turtle
import random

def draw_colored_text(text):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    font_style = ("Arial", 24, "bold")

    turtle.color(random.choice(colors))
    turtle.write(text, align="center", font=font_style)

def animate_bouncing_text(text):
    turtle.speed(2)
    turtle.penup()
    turtle.goto(0, 0)

    x_speed = 10
    y_speed = 20

    for _ in range(200):
        turtle.clear()
        draw_colored_text(text)
        turtle.forward(x_speed)
        turtle.right(90)
        turtle.forward(y_speed)
        turtle.left(90)

        x_speed *= 0.005  # Increase speed gradually
        y_speed *= 0.005

        turtle.update()

    turtle.hideturtle()
    turtle.done()

text_to_display = "Jai Shree Ram"
turtle.Screen().tracer(0)
animate_bouncing_text(text_to_display)