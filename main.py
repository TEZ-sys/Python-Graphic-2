import turtle
import random

# ----------------------Window-Setup------------------------
window = turtle.Screen()
window.setup(width=850, height=850)
window.bgcolor('black')

# ---------------------Border-Setup-------------------------
border = turtle.Turtle()
border.penup()
border.speed(0)
border.hideturtle()

# ---------------------Border-X-and-y-----------------------
border.color('white')
border.goto(400, 400)
border.pendown()
border.goto(400, -400)
border.goto(-400, -400)
border.goto(-400, 400)
border.goto(400, 400)

# ----------------------Random-movement---------------------
random_X = random.randint(-395, 395)
random_Y = random.randint(-395, 395)

# ----------------------Star-Setup--------------------------
star = turtle.Turtle()
star.speed(0)
star.hideturtle()
star.penup()
star.shape('circle')
star.color('white')

# ----------------------Star-Movement-----------------------
star.goto(random_X, random_Y)
star.speed(5)
star.showturtle()
dx = 3
dy = 4

while True:
    x, y = star.position()
    if x + dx >= 395 or x + dx <= -395:
        dx = -dx
    if y + dy >= 395 or y + dy <= -395:
        dy = -dy
    star.goto(x + dx, y + dy)


