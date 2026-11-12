import turtle

t = turtle.Turtle()
t.speed(6)
turtle.bgcolor("lightblue")
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

def arbre(longueur, niveau, angle, ratio):
    if niveau == 0:  # cas de base
        return
    t.pensize(niveau)
    t.color("saddlebrown" if niveau > 2 else "green")
    t.forward(longueur)
    t.left(angle)
    arbre(longueur * ratio, niveau - 1, angle, ratio)
    t.right(2 * angle)
    arbre(longueur * ratio, niveau - 1, angle, ratio)
    t.left(angle)
    t.penup()
    t.backward(longueur)
    t.pendown()

arbre(100, 8, 25, 0.75)
turtle.done()