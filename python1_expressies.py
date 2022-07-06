def boeken_bestellen():
    boek_prijs = 24.95
    korting = 40    # percent
    verschepen_eerste = 3
    verschepen_rest = 0.75
    aantal_boeken = 60
    prijs = 0
    prijs += boek_prijs - (boek_prijs * korting) / 100
    prijs += verschepen_rest
    prijs *= 60
    prijs += verschepen_eerste - verschepen_rest
    return prijs

def som_van_twee_getallen():
    getal1 = int(input())
    getal2 = int(input())
    return getal1 + getal2

def krekel_fahrenheit(invoer):
    return(50 + ((invoer - 40) / 4))

def krekel_celsius(invoer):
    return(10 + ((invoer - 40) / 7))

def de_krekel_als_thermometer():
    invoer = int(input())
    temp_fahrenheit = krekel_fahrenheit(invoer)
    temp_celsius = krekel_celsius(invoer)
    print('temperatuur (Fahrenheit):', temp_fahrenheit,'\ntemperatuur (Celsius):', temp_celsius)

def isbn():
    count = 1
    resultaat = 0
    while count <= 9:
        invoer = int(input())
        invoer *= count
        resultaat += invoer
        count += 1
    resultaat %= 11
    return resultaat

def the_pudding_guy():
    aantal_stuks = int(input())
    kostprijs_stuk = float(input())
    aantal_codes = int(input())
    aantal_mijlen = int(input())

    spendeerde = aantal_stuks * kostprijs_stuk

    totaal_mijlen = (aantal_stuks // aantal_codes) * aantal_mijlen

    print(f'Phillips spendeerde ${spendeerde:.1f} voor {totaal_mijlen} frequent flyer mijlen.')

def eentweedrie():
    list = []
    while len(list) < 3:
        list.append(int(input()))
    temp = list[0]
    list[0] = list[2]
    list[2] = temp
    for item in list:
        print(item, end=" ")

def appels_schikken():
    aantal_appels = int(input())
    kist = 20
    pallet = 35

    # paletten
    aantal_paletten = aantal_appels // (kist * pallet)

    # kisten
    rest = aantal_appels % (kist * pallet)
    aantal_kisten = rest // (kist)

    # appels
    appels = rest % kist
    print(f'{aantal_paletten}\n{aantal_kisten}\n{appels}')


