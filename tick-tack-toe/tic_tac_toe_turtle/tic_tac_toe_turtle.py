import turtle
import random
import time

window = turtle.Screen()

BOK = 800
X = -BOK/2
Y = BOK/2

window.setup(BOK, BOK)
window.title('Kółko i krzyżyk')
window.bgcolor('black')

xo = turtle.Turtle()
xo.color('white')
xo.speed(0)
xo.pensize(7)
xo.hideturtle()

tablica = [[None, None, None],
           [None, None, None],
           [None, None, None]]

kolej = random.choice(['X', 'O'])

odstep = int(BOK/3)

for a in [1, 2]:
    xo.penup()
    xo.goto(X + a * odstep, Y)
    xo.pendown()
    xo.goto(X + a * odstep, -Y)

    xo.penup()
    xo.goto(X, Y - a * odstep)
    xo.pendown()
    xo.goto(-X, Y - a * odstep)


def sprawdz():

    if tablica[0][0] == tablica[1][1] == tablica[2][2]:
        return tablica[2][2]
    if tablica[0][2] == tablica[1][1] == tablica[2][0]:
        return tablica[2][0]
    # w wierszu
    for w in range(3):
        if tablica[w][0] == tablica[w][1] == tablica[w][2]:
            return tablica[w][0]

    # w kolumnie
    for k in range(2):
        if tablica[0][k] == tablica[1][k] == tablica[2][k]:
            return tablica[0][k]

    return None


def click(x, y):
    global kolej
    print("click")

    # które pole klikną gracz
    kolumna = 0
    wiersz = 0

    if x < X + odstep:
        kolumna = 0
    elif x > X + 2 * odstep:
        kolumna = 2
    else:
        kolumna = 1

    if y > Y - odstep:
        wiersz = 0
    elif y < Y - 2 * odstep:
        wiersz = 2
    else:
        wiersz = 1

    # czy kliknięte pole jest wolne?

    if tablica[wiersz][kolumna] != None:
        return

    kolumna_srodek = (kolumna * odstep + odstep/2) - BOK/2
    wiersz_srodek = (-wiersz * odstep - odstep/2) + BOK/2

    xo.penup()
    xo.goto(kolumna_srodek - int(BOK/24), wiersz_srodek - int(BOK/24))
    if kolej == 'X':
        xo.write('X', font=('Arial', int(BOK / 12)))
    else:
        xo.write('O', font=('Arial', int(BOK / 12)))

    tablica[wiersz][kolumna] = kolej

    if kolej == 'O':
        kolej = 'X'
    else:
        kolej = 'O'

    if sprawdz() != None:
        xo.penup()
        xo.goto(int(-BOK/4), 0)
        time.sleep(1)
        xo.clear()
        xo.write('Wygały ' + sprawdz(), font=('Arial', int(BOK / 12)))
        


window.onclick(click)


window.listen()
window.mainloop()
