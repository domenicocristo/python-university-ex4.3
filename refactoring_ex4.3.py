# Potremmo generalizzare poligono in modo che riceva un angolo come terzo argomento,
# ma allora poligono non sarebbe più un nome appropriato! Invece, creiamo una funzione 
# più generale chiamata polilinea:

import turtle, math
bob = turtle.Turtle()

def polilinea(t, n, lunghezza, angolo):
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)

polilinea(bob, 0, 0, 0)

# Ora possiamo riscrivere poligono e arco in modo che usino polilinea:

def poligono(t, n, lunghezza):
    angolo = 360.0 / n
    polilinea(t, n, lunghezza, angolo)

poligono(bob, 10, 100)

def arco(t, r, angolo):
    arco_lunghezza = 2 * math.pi * r * angolo / 360
    n = int(arco_lunghezza / 3) + 1
    passo_lunghezza = arco_lunghezza / n
    passo_angolo = float(angolo) / n
    polilinea(t, n, passo_lunghezza, passo_angolo)

arco(bob, 100, 180)

# Infine riscriviamo cerchio in modo che usi arco:

def cerchio(t, r):
    arco(t, r, 360)

cerchio(bob, 100)