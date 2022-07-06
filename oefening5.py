import collections
import math
import numbers
import sys

sys.tracebacklimit = 1


def alfabetisch(input):
    inputList = str.split(input)
    sortedList = sorted(inputList)
    output = sortedList[0]
    sortedList.pop(0)
    for item in sortedList:
        output = output + ' ' + item
    return output

def driehoek(aantalRijen):
    try:
        if not isinstance(aantalRijen, numbers.Number) or aantalRijen < 0 or (not isinstance(aantalRijen, int)):
            raise AssertionError('ongeldig aantal rijen')
        driehoek = []
        for i in range (1,aantalRijen+1):
            if i == 1:
                rij = [1]
                driehoek.append(rij)
            else:
                rij = []
                referentie = collections.deque(driehoek[i-2])
                referentie.appendleft(0)
                referentie.append(0)
                for j in range (i):
                    rij.append(referentie[j] + referentie[j+1])
                driehoek.append(rij)
        return driehoek
    except AssertionError:
        raise


def zeshoek(rij, kolom):
    try:
        if kolom < 2 or kolom > rij - 1:
            raise AssertionError('ongeldig interne positie')

        mijnhoek = driehoek(rij + 1)
        output = []
        coordinaten = [(rij-1, kolom-1), (rij-1, kolom), (rij, kolom+1), (rij+1, kolom+1), (rij+1, kolom), (rij, kolom-1)]
        for item in coordinaten:
            rij, kolom = item
            output.append(mijnhoek[rij-1][kolom-1])
        return output
    except AssertionError:
        raise

def kwadraat(rij, kolom):
    try:
        mijnhoek = zeshoek(rij, kolom)
        product = 1
        for item in mijnhoek:
            product *= item

        vierkantswortel = math.sqrt(product)
        vierkantswortel = int(vierkantswortel)

        return (
            f'{mijnhoek[0]} x {mijnhoek[1]} x {mijnhoek[2]} x {mijnhoek[3]} x {mijnhoek[4]} x {mijnhoek[5]} = {product} = {vierkantswortel} x {vierkantswortel}')

    except AssertionError:
        raise


def zeef(invoer):
    getalLijst = [getal for getal in range(2, invoer + 1)]
    basis = getalLijst[0]
    optimalisatie = eratosthenes_optimalisatie(basis)
    while optimalisatie <= invoer:
        basis = doorloopLijst(basis, invoer, getalLijst)
        optimalisatie = eratosthenes_optimalisatie(basis)
    return getalLijst

def doorloopLijst(basis, invoer, getalLijst):
    factor = 2
    veelvoud = basis * factor
    while veelvoud <= invoer:
        if veelvoud in getalLijst:
            eratosthenes_schrappen(getalLijst, veelvoud)
        factor += 1
        veelvoud = basis * factor
    return getalLijst[getalLijst.index(basis) + 1]

def eratosthenes_optimalisatie(basis):
    return basis ** 2

def eratosthenes_schrappen(getalLijst, veelvoud):
    getalLijst.remove(veelvoud)

def zien(lijstHoedOpHoofd):
    aantalRode = 0
    lijstHoedInGeheugen=[]
    for i in range(len(lijstHoedOpHoofd)):
        if aantalRode % 2 != 0:
            lijstHoedInGeheugen.append('R')
        else:
            lijstHoedInGeheugen.append('B')
        if lijstHoedOpHoofd[i] == 'R':
            aantalRode += 1
    return tuple(lijstHoedInGeheugen)

def zeggen(lijstHoedInGeheugen):
    switch = False
    lijstHoedGezegd=[]
    if isinstance(lijstHoedInGeheugen, str) or isinstance(lijstHoedInGeheugen, tuple):
        lijstString = [s for s in lijstHoedInGeheugen]
        lijstHoedInGeheugen = lijstString
    lijstHoedInGeheugen.reverse()
    for i in range(len(lijstHoedInGeheugen)):
        lijstHoedGezegd.append(lijstHoedInGeheugen[i])
        if lijstHoedInGeheugen[i] == 'R':
            switch = True
            for j in range(i+1,len(lijstHoedInGeheugen)):
                if lijstHoedInGeheugen[j] == 'R':
                    lijstHoedInGeheugen[j] = 'B';
                else:
                    lijstHoedInGeheugen[j] = 'R';
    lijstHoedGezegd.reverse()
    return tuple(lijstHoedGezegd)

def isZigZag(lijst):
    boolZigZag = True
    for i in range(len(lijst)):
        #referentie = lijst[i]
        if i != 0:
            sequentie = i % 2
            if sequentie != 0:
                # kleiner dan
                if lijst[i] > referentie:
                    boolZigZag = False
                    break
                referentie = lijst[i]
            else:
                # groter dan
                if lijst[i] < referentie:
                    boolZigZag = False
                    break
                referentie = lijst[i]
        else:
            referentie = lijst[i]
    return boolZigZag

def zigzagTraag(lijst):
    lijst.sort()
    if len(lijst) % 2 == 0:
        limit = len(lijst)
    else:
        limit = len(lijst) - 1
    for i in range(0, limit, 2):
        x = lijst[i]
        y = lijst[i + 1]
        lijst[i] = y
        lijst[i + 1] = x

def zigzagSnel(lijst):
    voorgaande = None
    volgende = None
    if len(lijst) % 2 == 0:
        limit = len(lijst)
    else:
        limit = len(lijst) - 1
    for i in range(0, len(lijst), 2):
        if i > 0:
            voorgaande = lijst[i - 1]
        huidige = lijst[i]
        if not voorgaande is None:
            if huidige < voorgaande:
                x = lijst[i-1]
                y = lijst[i]
                lijst[i-1] = y
                lijst[i] = x
        if i < len(lijst) - 1:
            volgende = lijst[i + 1]
        huidige = lijst[i]
        if not volgende is None:
            if huidige < volgende:
                x = lijst[i]
                y = lijst[i + 1]
                lijst[i] = y
                lijst[i + 1] = x
        voorgaande = None
        volgende = None

def eerste(hidato):
    for i in range(len(hidato)):
        rij = hidato[i]
        for j in range(len(rij)):
            if rij[j] == 1:
                return (i, j)

def ende(hidato, waarde,y, x):
    if x == 0:
        minimum_x = 0
        maximum_x = 1
    elif x == len(hidato[0]) - 1:
        minimum_x = len(hidato[0]) - 2
        maximum_x = len(hidato[0]) - 1
    else:
        minimum_x = x - 1
        maximum_x = x + 1

    if y == 0:
        minimum_y = 0
        maximum_y = 1
    elif y == len(hidato) - 1:
        minimum_y = len(hidato) - 2
        maximum_y = len(hidato) - 1
    else:
        minimum_y = y - 1
        maximum_y = y + 1

    for i in range(minimum_y, maximum_y + 1):
        rij = hidato[i]
        for j in range(minimum_x, maximum_x + 1):
            if rij[j] == waarde:
                return (i, j)
    #return (None, None)
    return (y, x)

def opvolger(hidato, y, x):
    waarde = hidato[y][x]
    if waarde == len(hidato) * len(hidato[0]):
        return (None, None)
    else:
        coordinaten_opvolger = ende(hidato, waarde + 1, y, x)
        if coordinaten_opvolger == (y, x):
            return (None, None)
        else:
            return coordinaten_opvolger

def laatste(hidato):
    dimensie = len(hidato) * len(hidato[0])
    counter = 1
    coordinaten = eerste(hidato)
    while counter < dimensie and coordinaten != (None, None):
        coordinaten_voorlaatste = coordinaten
        coordinaten = opvolger(hidato, coordinaten[0], coordinaten[1])
        counter += 1
    if counter < dimensie and coordinaten == (None, None):
        coordinaten = coordinaten_voorlaatste
    return coordinaten

def hidato(hidato):
    coordinaten = laatste(hidato)
    if coordinaten == (None, None):
        return False
    waarde = hidato[coordinaten[0]][coordinaten[1]]
    if waarde == len(hidato) * len(hidato[0]):
        return True
    else:
        return False

def beweeg(startPositie, richting):
    startLijst = list(startPositie)
    if richting == '<':
        startLijst[0] -= 1
    elif richting == '>':
        startLijst[0] += 1
    elif richting == '^':
        startLijst[1] += 1
    elif richting == 'v':
        startLijst[1] -= 1
    return tuple(startLijst)

def teruggekeerd(richtingLijst):
    richtingTuple = tuple(richtingLijst)
    if richtingTuple == ('<', '>') or richtingTuple == ('>', '<') or richtingTuple == ('^', 'v') or richtingTuple == ('v', '^'):
        return True
    else:
        return False

def laatst_levende_positie(richtingLijst):
    coordinaten = (0, 0)
    for i in range(len(richtingLijst) - 1):
        richting1 = richtingLijst[i]
        richting2 = richtingLijst[i + 1]
        richtingLijstje = [richting1, richting2]
        coordinaten = beweeg(coordinaten, richting1)
        if teruggekeerd(richtingLijstje):
            return i + 1, coordinaten[0], coordinaten[1]
    coordinaten = beweeg(coordinaten, richting1)
    return i + 2, coordinaten[0], coordinaten[1]

def nieuw_kaartspel(kleurlijst, waardelijst):
    resultaatijst = []
    for i in range(len(kleurlijst)):
        for j in range(len(waardelijst)):
            resultaatijst.append(kleurlijst[i]+waardelijst[j])
    return resultaatijst

def splits_kaartspel(inputlijst):
    boek1 = inputlijst[:len(inputlijst)//2]
    boek2 = inputlijst[len(inputlijst)//2:]
    return boek1, boek2

def faro_shuffle(boek1, boek2):
    outputlijst = []
    limiet = len(boek1) if len(boek1) < len(boek2) else len(boek2)
    for i in range(limiet):
        outputlijst.append(boek1[i])
        outputlijst.append(boek2[i])
    if len(boek1) != len(boek2):
        if limiet == len(boek1):
            outputlijst.append(boek2[-1])
        else:
            outputlijst.append(boek1[-1])
    return outputlijst
