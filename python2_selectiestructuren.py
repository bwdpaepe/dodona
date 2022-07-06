import math


def isbn_isGeldig(isbn_lijst):
    resultaat = 0
    controle = isbn_lijst.pop()
    for i,v in enumerate(isbn_lijst,1):
        resultaat += i * v
    resultaat %= 11
    resultaat = True if resultaat == controle else False
    return resultaat

def isbn():
    isbn_lijst = []
    for i in range(10):
        ongeldigeInvoer = True
        while ongeldigeInvoer:
            invoer = int(input())
            ongeldigeInvoer = False if invoer >= 0 and invoer <= 9 else True
        isbn_lijst.append(invoer)
    if isbn_isGeldig(isbn_lijst):
        print("OK")
    else:
        print("FOUT")

def blad_steen_schaar_resultaat(gebaar1, gebaar2):
    if gebaar1 == gebaar2:
        return 0
    elif gebaar1 == "blad":
        return 1 if gebaar2 in ["steen", "Spock"] else 2

def blad_steen_schaar():
    spel_lijst = []
    for i in range(2):
        ongeldigeInvoer = True
        while ongeldigeInvoer:
            invoer = input()
            if invoer in ("blad", "steen", "hagedis", "Spock", "schaar"):
                ongeldigeInvoer = False
                spel_lijst.append(invoer)

    if blad_steen_schaar_resultaat(spel_lijst[0], spel_lijst[1]) == 0:
        print("gelijkspel")
    elif blad_steen_schaar_resultaat(spel_lijst[0], spel_lijst[1]) == 1:
        print("speler 1 wint")
    else:
        print("speler 2 wint")

def apgar():
    apgar_lijst = []
    omschrijving_lijst = [["geen", "zwak", "goed doorhuilen"], None, ["slap", "enige flexie", "actieve beweging"], ["blauw", "bleek", "extremiteiten", "roze"], ["geen", "enige beweging", "krachtig huilen"]]
    for i in range(5):
        apgar_lijst.append(input())
        if i != 1 and apgar_lijst[i] not in omschrijving_lijst[i]:
            return "ongeldige invoer"
        elif i == 1 and (math.isnan(int(apgar_lijst[i])) or int(apgar_lijst[i]) < 0):
            return "ongeldige invoer"
    score = 0
    #ademhaling
    score += omschrijving_lijst[0].index(apgar_lijst[0])
    #pols
    if int(apgar_lijst[1]) > 0 and int(apgar_lijst[1]) < 100:
        score += 1
    elif int(apgar_lijst[1]) >= 100:
        score += 2
    #spier
    score += omschrijving_lijst[2].index(apgar_lijst[2])
    #aspect
    if(apgar_lijst[3] in omschrijving_lijst[3][2:]):
        score += 1 + omschrijving_lijst[3][2:].index(apgar_lijst[3])
    #reactie
    score += omschrijving_lijst[4].index(apgar_lijst[4])

    print(score) if score >= 4 else "alarm"









