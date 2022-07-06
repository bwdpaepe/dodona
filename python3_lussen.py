import math
from collections import Counter

def toevoegenachteraan():
    words = ['cat', 'window', 'defenestrate']
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)

    print(words)

def getalladder():
    foutieveInvoer = True
    while foutieveInvoer:
        getal = int(input())
        if getal > 0 and getal <= 9:
            foutieveInvoer = False

    for i in range(1,getal+1):
        for j in range(1,i+1):
            print(j, end="")
        print("")

def piratenEnKokosnoten():
    aapKokosnoten = 5
    aapKokosnotenTekst = "{} noten".format(aapKokosnoten)

def Euler():
    som = 0
    for i in range(1, 101):
        som += 1 / math.pow(i, 2)
    print(som)

def beleefdheid():
    getal = int(input())
    priemfactoren = []
    deler = 2
    while deler <= getal:
        if getal % deler == 0:
            getal = getal / deler
            if deler != 2:
                priemfactoren.append(deler)
                deler = 2
        else:
            deler = deler + 1
    c = Counter(priemfactoren)
    beleefdheidsResultaat = 1
    for x in c:
        key = x
        value = c[key]
        beleefdheidsResultaat = beleefdheidsResultaat * (value + 1)
    beleefdheidsResultaat = beleefdheidsResultaat - 1
    print(beleefdheidsResultaat)

def bevriende_getallen():
    getal1 = int(input())
    getal2 = int(input())
    getal1DelersSom = 0
    getal2DelersSom = 0
    for deler in range(1, getal1 // 2 + 1):
        if getal1 % deler == 0:
            getal1DelersSom = getal1DelersSom + deler
    for deler in range(1, getal2 // 2 + 1):
        if getal2 % deler == 0:
            getal2DelersSom = getal2DelersSom + deler
    if (getal2 == getal1DelersSom) and (getal1 == getal2DelersSom):
        print(f'{getal1} en {getal2} zijn bevriende getallen')