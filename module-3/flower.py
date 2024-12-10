import turtle

# Setup screen and turtle
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")  # Background color

# Color setup
num_petals = 36
colors = ["magenta", "cyan", "yellow", "orange", "lime"]

# Draw the flower
for i in range(num_petals):
    t.color(colors[i % len(colors)])  # Cycle through colors
    t.circle(100)  # Draw a petal
    t.left(360 / num_petals)  # Rotate for the next petal

# Add a center circle
t.penup()
t.goto(0, -10)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
