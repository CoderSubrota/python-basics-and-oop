import turtle

# Set up the turtle screen
turtle.bgcolor("black")  # Background color
t = turtle.Turtle()
t.speed(10)  # Speed of drawing
t.color("magenta")  # Petal color

# Draw the flower
for i in range(36):
    t.circle(100)  # Radius of each petal
    t.left(10)  # Angle between each petal

# Draw the center of the flower
t.penup()
t.goto(0, -10)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(10)
t.end_fill()

# Finish and keep the window open
t.hideturtle()
turtle.done()
