def maximale_blootstelling(geluidsniveau):
    if geluidsniveau < 80:
        return -1.0
    elif geluidsniveau < 83 and geluidsniveau >= 80:
        return 28800.0
    else:
        ondergrens = 83
        bovengrens = ondergrens + 3
        deler = 2.0 # halveren
        tijdslimiet = 28800.0 # 8 x 3600
        while geluidsniveau < ondergrens or geluidsniveau >= bovengrens:
            ondergrens = bovengrens
            bovengrens = ondergrens + 3
            deler = deler * 2
        return tijdslimiet / deler

def bovensteboven(getal):
    stringGetal = str(getal)
    if '2' in stringGetal or '3' in stringGetal or '4' in stringGetal or '5' in stringGetal or '7' in stringGetal:
        return False
    else:
        getalList = [int(d) for d in stringGetal]
        midden = len(getalList) // 2

        getalList1 = getalList[0:midden]
        if len(getalList) % 2 == 0:  # even
            getalList2 = getalList[midden:len(getalList)]
        else:
            if str(getalList[midden]) in '6, 9':
                return False
            getalList2 = getalList[midden+1:len(getalList)]
        getalList2.reverse()
        check = True
        for i in range(len(getalList1)):
            if str(getalList1[i]) in '0, 1, 8' and getalList2[i] != getalList1[i]:
                check = False
                break
            if getalList1[i] == 6 and getalList2[i] != 9:
                check = False
                break
            if getalList1[i] == 9 and getalList2[i] != 6:
                check = False
                break
        return check

def volgende(getal):
    getal = getal + 1
    while not bovensteboven(getal):
        getal = getal + 1
    return getal

def waardering(prijs_big_mac_land, reele_wisselkoers):
    prijs_big_mac_dollar = 4.07
    bm_wisselkoers = prijs_big_mac_land / prijs_big_mac_dollar
    waardering = ((bm_wisselkoers - reele_wisselkoers) / reele_wisselkoers) * 100
    if waardering <= -25:
        waarderingTekst = 'sterk ondergewaardeerd'
    elif waardering > -25 and waardering <= -5:
        waarderingTekst = 'ondergewaardeerd'
    elif waardering > -5 and waardering <= 5:
        waarderingTekst = 'ongeveer gelijk'
    elif waardering > 5 and waardering <= 25:
        waarderingTekst = 'overgewaardeerd'
    else:
        waarderingTekst = 'sterk overgewaardeerd'
    return waarderingTekst

def wisselkoersanalyse(prijs_big_mac_land_string, reele_wisselkoers):
    splitindex = str.index(prijs_big_mac_land_string, ' ')
    prijs_big_mac_land = float(prijs_big_mac_land_string[0:splitindex])
    munteenheid = prijs_big_mac_land_string[splitindex+1:len(prijs_big_mac_land_string)]
    return "De {} is {} ten opzichte van de dollar.".format(munteenheid, waardering(prijs_big_mac_land, reele_wisselkoers))


def evenOneven(invoer):

    """
    >>> evenOneven(886328712442992)
    (10, 5)
    >>> evenOneven(10515)
    (1, 4)
    >>> evenOneven(145)
    (1, 2)
    """

    evenOnevenList = [int(d) for d in str(invoer)]
    evenList = []
    onevenList = []
    for getal in evenOnevenList:
        if getal % 2 == 0:
            evenList.append(getal)
        else:
            onevenList.append(getal)

    return (len(evenList), len(onevenList))





def volgende(getal):

    """
    >>> volgende(886328712442992)
    10515
    >>> volgende(10515)
    145
    >>> volgende(145)
    123
    """

    volgendeTuple = evenOneven(getal)
    even = volgendeTuple[0]
    oneven = volgendeTuple[1]
    totaal = even + oneven
    getalString = str(even) + str(oneven) + str(totaal)
    volgende = int(getalString)
    return volgende


def stappen(getal):

    """
    >>> stappen(886328712442992)
    3
    >>> stappen(1217637626188463187643618416764317864)
    4
    >>> stappen(0)
    2
    >>> stappen(1)
    5
    >>> stappen(2)
    2
    >>> stappen(3)
    5
    """
    i = 0
    while getal != 123:
        getal = volgende(getal)
        i += 1

    return i