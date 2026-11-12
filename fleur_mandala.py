"""
Atelier Turtle - L2
Dessin : une fleur "mandala" sous un ciel étoilé.
Idée personnelle : la fleur est faite de plusieurs couches de pétales
(de la plus grande à la plus petite). Chaque couche a sa couleur,
calculée automatiquement (dégradé) avec le module colorsys.
"""

import turtle
import random
import colorsys   # NOUVEAU : permet de calculer des couleurs (dégradé)

# ---------- 1. Préparation de la fenêtre et de la tortue ----------
ecran = turtle.Screen()
ecran.bgcolor("yellowgreen")
ecran.title("Fleur mandala")
ecran.tracer(0)          # NOUVEAU : on désactive l'animation (dessin instantané)

t = turtle.Turtle()
t.hideturtle()           # on cache la flèche de la tortue
t.speed(0)
t.pensize(1)


# ---------- 2. Fonctions ----------
def aller_a(x, y):
    """Déplace la tortue en (x, y) sans dessiner."""
    t.penup()
    t.goto(x, y)
    t.pendown()


def etoiles(nombre):
    """Dessine des étoiles (points blancs) à des positions aléatoires."""
    for _ in range(nombre):
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        aller_a(x, y)
        t.dot(random.randint(2, 4), "white")  # étoile = point jaune de taille aléatoire


def petale(rayon, couleur):
    """Dessine un pétale rempli avec la couleur donnée.
    Un pétale = 2 arcs de cercle de 60° (comme dans l'exemple 1)."""
    t.fillcolor(couleur)
    t.begin_fill()              # NOUVEAU : début du remplissage
    t.circle(rayon, 60)
    t.left(120)
    t.circle(rayon, 60)
    t.left(120)
    t.end_fill()                # NOUVEAU : fin du remplissage


def couche(nb_petales, rayon, teinte):
    """Dessine une couche : nb_petales pétales répartis autour du centre.
    'teinte' (0 à 1) fixe la couleur de départ de la couche."""
    angle = 360 / nb_petales    # angle entre deux pétales
    for i in range(nb_petales):
        # la couleur change un peu à chaque pétale -> effet dégradé
        r, g, b = colorsys.hsv_to_rgb(teinte + i / nb_petales * 0.15, 0.8, 1)
        t.pencolor("black")  # contour noir
        petale(rayon, (r, g, b))
        t.left(angle)


# ---------- 3. Programme principal ----------
etoiles(80)                     # le ciel

aller_a(0, 0)
t.setheading(0)

NB_COUCHES = 5              # paramètre à modifier
NB_PETALES = 15            # paramètre à modifier

for k in range(NB_COUCHES):
    rayon = 200 - k * 20       # chaque couche est plus petite que la précédente
    couche(NB_PETALES, rayon, k * 0.12)
    t.left(200 / NB_PETALES)    # décalage : les pétales de la couche suivante
                                # se placent entre ceux de la couche précédente

# centre de la fleur
aller_a(0, 0)
t.dot(30, "gold")

ecran.update()                  # on affiche d'un coup tout le dessin
turtle.done()