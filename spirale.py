import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

couleurs = ["cyan", "magenta", "yellow", "orange"]

def spirale(angle, nb_repetitions, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(nb_repetitions):
        t.color(couleurs[i % len(couleurs)])
        t.pensize(1 + i / 30)      # le trait devient plus épais
        t.forward(i * 1.2)
        t.left(angle)

spirale(59, 120, -200, 0)
spirale(121, 120, 200, 0)
turtle.done()