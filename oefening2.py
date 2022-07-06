import math


def isbn():
    a = 1
    som = 0
    while a <= 10:
        if a < 10:
            x = int(input())
            som = som + (a * x)
        else:
            controle = som % 11
            x = int(input())
            print('OK') if controle == x else print('FOUT')
        a = a + 1

def blad_steen_schaar():
    speler1 = input()
    speler2 = input()
    if speler1 == speler2:
        print("gelijkspel")
    elif speler1 == 'blad':
        print("speler 1 wint") if speler2  in ['steen', 'Spock'] else print("speler 2 wint")
    elif speler1 == 'steen':
        print("speler 1 wint") if speler2 in ['hagedis', 'schaar'] else print("speler 2 wint")
    elif speler1 == 'hagedis':
        print("speler 1 wint") if speler2  in ['Spock', 'blad'] else print("speler 2 wint")
    elif speler1 == 'Spock':
        print("speler 1 wint") if speler2 in ['schaar', 'steen'] else print("speler 2 wint")
    elif speler1 == 'schaar':
        print("speler 1 wint") if speler2 in ['blad', 'hagedis'] else print("speler 2 wint")

def apgar():
    ademhaling = ['geen', 'zwak', 'goed doorhuilen']
    pols = [0, 100, 100]
    tonus = ['slap', 'enige flexie', 'actieve beweging']
    aspect = [['blauw', 'bleek'], 'extremiteiten', 'roze']
    reactie = ['geen', 'enige beweging', 'krachtig huilen']
    invoerAdemhaling = input()
    invoerPols = int(input())
    invoerTonus = input()
    invoerAspect = input()
    invoerReactie = input()
    score = 0
    try:
        score = score + ademhaling.index(invoerAdemhaling)
        score = score + tonus.index(invoerTonus)
        score = score + reactie.index(invoerReactie)
    except ValueError:
        score = "ongeldige invoer"

    if score == "ongeldige invoer":
        print(score)
    else:
        if invoerPols == pols[0]:
            score = score + 0
        elif invoerPols < pols[1]:
            score = score + 1
        else:
            score = score + 2
        try:
            score = score + aspect.index(invoerAspect)
        except ValueError:
            aspectList = aspect[0]
            try:
                if invoerAspect in aspectList:
                    score = score + 0
            except:
                score = "ongeldige invoer"
        if score == "ongeldige invoer":
            print(score)
        elif score < 4:
            print("alarm")
        else:
            print(score)

def vierkantsvergelijking():
    a = float(input())
    b = float(input())
    c = float(input())

    delta = b**2 - (4 * a * c)

    if delta < 0:
        print('geen wortels')
    elif delta == 0:
        print('een wortel')
        wortel = -1 * (b / (2*a))
        print (wortel)
    else:
        print('twee wortels')
        wortelLijst = []
        wortelLijst.append(((-1 * b) - math.sqrt(delta)) / (2 * a))
        wortelLijst.append(((-1 * b) + math.sqrt(delta)) / (2 * a))
        wortelLijst.sort()
        print(wortelLijst[0])
        print(wortelLijst[1])

def vierkaarten():
    zijdeLijst = ['waarde', 'kleur']
    zijdeInvoer = input()
    if zijdeInvoer == zijdeLijst[0]:
        valueInvoer = int(input())
        antwoordInvoer = input()
        if valueInvoer % 2 != 0:
            print(f'Fout: kaarten met waarde {valueInvoer} moeten niet gedraaid worden.') if antwoordInvoer == "ja" else print(f'Juist: kaarten met waarde {valueInvoer} moeten niet gedraaid worden.')
        else:
            print(f'Juist: kaarten met waarde {valueInvoer} moeten gedraaid worden.') if antwoordInvoer == "ja" else print(f'Fout: kaarten met waarde {valueInvoer} moeten gedraaid worden.')
    else:
        valueInvoer = input()
        antwoordInvoer = input()
        if valueInvoer != "rood":
            print(f'Juist: kaarten met waarde {valueInvoer} moeten gedraaid worden.') if antwoordInvoer == "ja" else print(f'Fout: kaarten met waarde {valueInvoer} moeten gedraaid worden.')
        else:
            print(f'Fout: kaarten met waarde {valueInvoer} moeten niet gedraaid worden.') if antwoordInvoer == "ja" else print(f'Juist: kaarten met waarde {valueInvoer} moeten niet gedraaid worden.')

def valsmunterij():
    muntenLijst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    #groep123 = muntenLijst[0:3]
    #groep456 = muntenLijst[3:6]
    #groep789 = muntenLijst[6:9]

    # Eerst wegen we groep123 en groep456
    resultaatWeging = input()
    if resultaatWeging == "rechts":
        #groep123
        muntenSubLijst = muntenLijst[0:3]
    elif resultaatWeging == "links":
        #groep456
        muntenSubLijst = muntenLijst[3:6]
    else:
        #groep789
        muntenSubLijst = muntenLijst[6:9]

    # Dan wegen we munten 1 en 2 van de subLijst
    resultaatWeging = input()
    if resultaatWeging == "rechts":
        #munt1
        print(f'muntstuk #{muntenSubLijst[0]} is vervalst')
    elif resultaatWeging == "links":
        #munt2
        print(f'muntstuk #{muntenSubLijst[1]} is vervalst')
    else:
        #munt3
        print(f'muntstuk #{muntenSubLijst[2]} is vervalst')

def babysit():
    laagTarief = 2
    hoogTarief = 4
    beginUur = int(input())
    beginMinuut = int(input())
    beginTijdstip = beginUur + (beginMinuut / 60)
    eindUur = int(input())
    eindMinuut = int(input())
    eindTijdstip = eindUur + (eindMinuut / 60)
    bedragLaagTarief = 0
    bedragHoogTarief = 0
    if (beginUur < 18) or (eindTijdstip < beginTijdstip):
        print("ongeldige invoer")
    else:
        if beginTijdstip < 21.5:
            if eindTijdstip > 21.5:
                # laagtarief
                minutenLaagTarief = (21.5 - beginTijdstip) * 60.0
                bedragLaagTarief = (minutenLaagTarief / 60.0) * laagTarief
                # hoogtarief
                minutenHoogTarief = (eindTijdstip - 21.5) * 60.0
                bedragHoogTarief = (minutenHoogTarief / 60.0) * hoogTarief
            else:
                # laagtarief
                minutenLaagTarief = (eindTijdstip - beginTijdstip) * 60.0
                bedragLaagTarief = (minutenLaagTarief / 60.0) * laagTarief
        else:
            # hoogtarief
            minutenHoogTarief = (eindTijdstip - beginTijdstip) * 60.0
            bedragHoogTarief = (minutenHoogTarief / 60.0) * hoogTarief
        print(bedragLaagTarief + bedragHoogTarief)

def botsing():
    rechthoek1 = []
    rechthoek2 = []

    rechthoek1_x1 = int(input())
    rechthoek1_y1 = int(input())
    rechthoek1_x2 = int(input())
    rechthoek1_y2 = int(input())
    rechthoek2_x1 = int(input())
    rechthoek2_y1 = int(input())
    rechthoek2_x2 = int(input())
    rechthoek2_y2 = int(input())
    botsing_x = False
    botsing_y = False

    if rechthoek1_x1 < rechthoek1_x2:
        for i in range(rechthoek1_x1, rechthoek1_x2 + 1):
            if ((i > rechthoek2_x1) and (i < rechthoek2_x2)) or ((i < rechthoek2_x1) and (i > rechthoek2_x2)):
                botsing_x = True
                break
    else:
        for i in range(rechthoek1_x2, rechthoek1_x1 + 1):
            if ((i > rechthoek2_x1) and (i < rechthoek2_x2)) or ((i < rechthoek2_x1) and (i > rechthoek2_x2)):
                botsing_x = True
                break

    if rechthoek1_y1 < rechthoek1_y2:
        for i in range(rechthoek1_y1, rechthoek1_y2 + 1):
            if ((i > rechthoek2_y1) and (i < rechthoek2_y2)) or ((i < rechthoek2_y1) and (i > rechthoek2_y2)):
                botsing_y = True
                break
    else:
        for i in range(rechthoek1_y2, rechthoek1_y1 + 1):
            if ((i > rechthoek2_y1) and (i < rechthoek2_y2)) or ((i < rechthoek2_y1) and (i > rechthoek2_y2)):
                botsing_y = True
                break

    if botsing_x and botsing_y:
        print('botsing')
    else:
        print('geen botsing')