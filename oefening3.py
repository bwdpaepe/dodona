import math
from collections import Counter


def getalladder():
    invoerGetal = int(input())
    if invoerGetal <= 9:
        for i in range(1, invoerGetal + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print("")

def apenEnKokosnoten():
    aantalPiraten = int(input())
    aantalKokosnoten = int(input())

    # loop over alle piraten
    for i in range(1, aantalPiraten + 1):
        restKokosnoten = aantalKokosnoten
        piraatKokosnoten = aantalKokosnoten // aantalPiraten
        aapKokosnoten = aantalKokosnoten % piraatKokosnoten
        if aapKokosnoten == 0:
            aapKokosnotenTekst = "geen noten"
        elif aapKokosnoten == 1:
            aapKokosnotenTekst = "1 noot"
        else:
            aapKokosnotenTekst = "{} noten".format(aapKokosnoten)
        aantalKokosnoten = aantalKokosnoten - piraatKokosnoten - aapKokosnoten

        print(f'{restKokosnoten} noten = {piraatKokosnoten} noten voor piraat#{i} en {aapKokosnotenTekst} voor de aap')
    piraatKokosnoten = aantalKokosnoten // aantalPiraten
    aapKokosnoten = aantalKokosnoten % piraatKokosnoten
    if aapKokosnoten == 0:
        aapKokosnotenTekst = "geen noten"
    elif aapKokosnoten == 1:
        aapKokosnotenTekst = "1 noot"
    else:
        aapKokosnotenTekst = "{} noten".format(aapKokosnoten)
    print(f'elke piraat krijgt {piraatKokosnoten} noten en {aapKokosnotenTekst} voor de aap')

def baselProbleem():
    # n = 100
    som = 0
    for i in range(1, 101):
        som = som + (1 / i**2)
    print(som)

    constantMetPi = (math.pi**2) / 6
    constantConditie = 1 / 100
    n = 1
    som = 1
    while abs(som - constantMetPi) > constantConditie:
        n = n + 1
        som = som + (1 / n**2)
    print(n)

def biljarttafel():
    hoogte = int(input())
    breedte = int(input())
    x = 0
    y = 0
    pockets = ((0, 0), (0, hoogte), (breedte, 0), (breedte, hoogte))
    richtingX = 1
    richtingY = 1
    unit = min(hoogte, breedte)
    start = True
    if hoogte <= breedte:
        while (start or (not((x, y) in pockets))):
            start = False
            x = x + (unit * richtingX)
            y = y + (unit * richtingY)
            if x == 0:
                richtingX = 1
                if y not in [0, hoogte]:
                    print("linkerband {}".format((x, y)))
                #unit = min(breedte, hoogte - y)
            elif y == 0:
                richtingY = 1
                if x not in [0, breedte]:
                    print("onderband {}".format((x, y)))
                #unit = min(hoogte, x)
            elif x == breedte:
                richtingX = -1
                if y not in [0, hoogte]:
                    print("rechterband {}".format((x, y)))
                #unit = min(breedte, y)
            elif y == hoogte:
                richtingY = -1
                if x not in [0, breedte]:
                    print("bovenband {}".format((x, y)))
                #unit = min(hoogte, breedte - x)
            if richtingX == 1:
                if richtingY == 1:
                    unit = min(breedte-x, hoogte-y)
                else:
                    unit = min(breedte-x, y)
            else:
                if richtingY == 1:
                    unit = min(x, hoogte-y)
                else:
                    unit = min(x, y)
        if (x, y) == (0, 0):
            print("linkeronderpocket {}".format((x, y)))
        elif (x, y) == (0, hoogte):
            print("linkerbovenpocket {}".format((x, y)))
        elif (x, y) == (breedte, 0):
            print("rechteronderpocket {}".format((x, y)))
        elif (x, y) == (breedte, hoogte):
            print("rechterbovenpocket {}".format((x, y)))

def blackjack():
    speel = True
    som = 0
    while speel:
        kaart = int(input())
        if kaart in range(1, 12):
            som = som + kaart
            if som == 21:
                print("Gewonnen!")
                speel = False
            elif som > 21:
                print(f'Verbrand ({som})')
                speel = False
        elif kaart == 0:
            print(f'Voorzichtig gespeeld ({som})')
            speel = False

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


def bevriendeGetallen():
    getal1 = int(input())
    getal2 = int(input())
    getal1DelersSom = 0
    getal2DelersSom = 0

    for deler in range(1, getal1//2 + 1):
        if getal1 % deler == 0:
            getal1DelersSom = getal1DelersSom + deler

    for deler in range(1, getal2//2 + 1):
        if getal2 % deler == 0:
            getal2DelersSom = getal2DelersSom + deler

    if getal1DelersSom == getal2 and getal2DelersSom == getal1:
        print(f'{getal1} en {getal2} zijn bevriende getallen')
    else:
        print(f'{getal1} en {getal2} zijn geen bevriende getallen')

def boeketRozen():
    rood_wit = int(input())
    blauw_wit = int(input())
    blauw_rood_VS_blauw_wit = input()

    if blauw_rood_VS_blauw_wit == "<":
        for x in range(2, min(rood_wit, blauw_wit)):
            rood = x
            wit = rood_wit - rood
            blauw = blauw_wit - wit
            if wit >= 2 and blauw >= 2 and blauw + rood < blauw + wit:
                print(blauw)
                print(wit)
                print(rood)
                break
    else:
        for x in range(2, max(rood_wit, blauw_wit)):
            rood = x
            wit = rood_wit - rood
            blauw = blauw_wit - wit
            if wit >= 2 and blauw >= 2 and blauw + rood > blauw + wit:
                print(blauw)
                print(wit)
                print(rood)
                break



def drieWijzen():
    totaalfloat = float(input())
    totaal = round(totaalfloat*100)
    print(totaal)
    a = 0
    b = 0
    c = 0
    while a < totaal:
        a = a + 1
        b = a
        while b < totaal:
            c = totaal - a - b
            if a == 6 and b == 2750:
                print(totaal)
                print(a)
                print(b)
                print(c)
            if c < b:
                b = b + 1
                continue
            else:
                if a == 6 and b == 2750:
                    print(c)
                    print(round(a/100,2) * round(b/100,2) * (c/100))
                    print(round(totaal/100,2))
                if math.isclose(round(a/100,2) * round(b/100,2) * (c/100), round(totaal/100,2)):
                    print(f'€{format(a / 100, ".2f")} + €{format(b / 100, ".2f")} + €{format(c / 100, ".2f")} = €{format(a / 100, ".2f")} x €{format(b / 100, ".2f")} x €{format(c / 100, ".2f")} = €{format(totaal / 100, ".2f")}')
                    break
                else:
                    b = b + 1
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
