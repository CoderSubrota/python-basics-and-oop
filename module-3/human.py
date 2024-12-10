import turtle

# Set up turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Background color

# Initialize turtle
t = turtle.Turtle()
t.speed(5)

# Draw face (circle for the head)
t.penup()
t.goto(0, -100)  # Move to start position
t.pendown()
t.color("black", "peachpuff")  # Outline and fill color
t.begin_fill()
t.circle(100)  # Draw head
t.end_fill()

# Draw left eye
t.penup()
t.goto(-35, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw right eye
t.penup()
t.goto(35, 30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw pupils
t.color("black")
t.penup()
t.goto(-30, 35)
t.pendown()
t.circle(5)

t.penup()
t.goto(40, 35)
t.pendown()
t.circle(5)

# Draw nose
t.penup()
t.goto(0, 20)
t.setheading(-90)
t.pendown()
t.forward(30)

# Draw mouth
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.circle(40, 120)

# Finish drawing
t.hideturtle()
turtle.done()
