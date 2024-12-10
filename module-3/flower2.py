import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cursor Flower Drawing")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Function to draw a flower at the cursor's location
def draw_flower(x, y):
    t.penup()
    t.goto(x, y)  # Move turtle to cursor position
    t.pendown()
    t.color("magenta", "yellow")
    
    for _ in range(12):  # Draw petals
        t.circle(20, steps=6)  # Small hexagon for petal
        t.right(30)  # Angle between petals

# Bind the mouse click event
screen.onscreenclick(draw_flower)

# Keep the window open
turtle.done()
