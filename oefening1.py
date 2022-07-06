def boekenBestellen():
    boekprijs = 24.95
    inkoopkorting = 40
    verscheepskostBoek1 = 3
    verscheepskostOverigeBoeken = 0.75
    totaalGoederenPrijs = 60 * (boekprijs - (boekprijs * (inkoopkorting / 100)))
    totaalVerzendingPrijs = (1 * verscheepskostBoek1) + ((60 - 1) * verscheepskostOverigeBoeken)
    totaal = totaalGoederenPrijs + totaalVerzendingPrijs
    print(f'{totaal:.2f}')

def somVanTweeGetallen():
    getal1 = int(input())
    getal2 = int(input())
    print(getal1 + getal2)

def krekelAlsThermometer():
    aantalTjirpsPerMinuut = int(input())
    fahrenheit = 50 + ((aantalTjirpsPerMinuut - 40) / 4)
    celcius = 10 + ((aantalTjirpsPerMinuut - 40) / 7)
    print('temperatuur (Fahrenheit):', fahrenheit)
    print('temperatuur (Celsius):', celcius)

def isbn():
    a = 1
    som = 0
    while(a <=9):
        x = int(input())
        som = som + (x * a)
        a = a + 1
    controlecijfer = som % 11
    print(controlecijfer)

def thePuddingGuy():
    aantalGekochteStuks = int(input())
    prijsPerStuk = float(input())
    aantalBarcodesVoorFrequentFlyerCoupon = int(input())
    aantalMijlenPerFrequentFlyerCoupon = int(input())

    totaleAankoopprijs = aantalGekochteStuks * prijsPerStuk
    totaalAantalCoupons = aantalGekochteStuks // aantalBarcodesVoorFrequentFlyerCoupon
    totaalAantalMijlen = aantalMijlenPerFrequentFlyerCoupon * totaalAantalCoupons

    print(f'Phillips spendeerde ${totaleAankoopprijs} voor {totaalAantalMijlen} frequent flyer mijlen.')

def eentweedriedrietweeeen():
    getal1 = int(input())
    getal2 = int(input())
    getal3 = int(input())
    lijst = [getal1, getal2, getal3]
    lijst.reverse()
    for getal in lijst:
        print(getal, end=' ')

def appelsSchikken():
    aantalAppels = int(input())
    aantalKisten = aantalAppels // 20
    restAppels = aantalAppels % 20
    aantalPaletten = aantalKisten // 35
    restPaletten = aantalKisten % 35
    print(aantalPaletten)
    print(restPaletten)
    print(restAppels)

def autoverhuur():
    kilometertellerBegin = float(input())
    kilometertellerEinde = float(input())
    literBenzine = float(input())
    kilometers = kilometertellerEinde - kilometertellerBegin
    literPerHonderd = (literBenzine / kilometers) * 100
    print(literPerHonderd)

