# 1. Scrivete una funzione di nome quadrato che richieda un parametro di nome t, che è
# una tartaruga. La funzione deve usare la tartaruga per disegnare un quadrato.
# Scrivete una chiamata alla funzione quadrato che passi bob come argomento, ed
# eseguite nuovamente il programma.

# 2. Aggiungete a quadrato un nuovo parametro di nome lunghezza. Modificate il corpo 
# in modo che la lunghezza dei lati sia pari a lunghezza, quindi modificate la chiamata 
# alla funzione in modo da fornire un secondo argomento. Eseguite di nuovo il 
# programma e provatelo con vari valori di lunghezza.

import turtle, math
bob = turtle.Turtle()

def quadrato(t, lunghezza):
    for i in range(4):
        t.fd(lunghezza)
        t.lt(90)

quadrato(bob, lunghezza=100)

# 3. Fate una copia di quadrato e cambiate il nome in poligono. Aggiungete un altro
# parametro di nome n e modificate il corpo in modo che sia disegnato un poligono 
# regolare di n lati.

def poligono(t, n, lunghezza):
    angolo = 360 / n
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)

poligono(bob, n=7, lunghezza=100)

# 4. Scrivete una funzione di nome cerchio che prenda come parametri una tartaruga, t,
# e un raggio, r, e che disegni un cerchio approssimato chiamato poligono con una 
# appropriata lunghezza e numero di lati. Provate la funzione con diversi valori di r.

def cerchio(t, r):
    circonferenza = 2 * math.pi * r
    n = int(circonferenza / 3) + 3
    lunghezza = circonferenza / n
    poligono(t, n, lunghezza)

cerchio(bob, 100)

# 5. Create una versione più generale della funzione del cerchio, di nome arco che richieda 
# un parametro aggiuntivo angolo, il quale determina la porzione di cerchio da disegnare.
# Angolo è espresso in gradi, quindi se angolo=360, arco deve disegnare un cerchio completo.

def arco(t, r, angolo):
    arco_lunghezza = 2 * math.pi * r * angolo / 360
    n = int(arco_lunghezza / 3) + 1
    passo_lunghezza = arco_lunghezza / n
    passo_angolo = angolo / n

    for i in range(n):
        t.fd(passo_lunghezza)
        t.lt(passo_angolo)

arco(bob, 50, 180)