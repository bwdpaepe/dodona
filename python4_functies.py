def lawaaidoofheid(geluidsniveau):
    if geluidsniveau < 80:
        return -1
    elif 80 <= geluidsniveau < 83:
        return 28800.0
    else:
        ondergrens = 83
        bovengrens = ondergrens + 3
        deler = 2.0
        tijdslimiet = 28800.0
        while geluidsniveau < ondergrens or geluidsniveau >= bovengrens:
            ondergrens = bovengrens
            bovengrens = ondergrens + 3
            deler *= 2
        return tijdslimiet / deler


def bovensteboven(getal):
    stringGetal = str(getal)
    if '2' in stringGetal or '3' in stringGetal or '4' in stringGetal or '5' in stringGetal or '7' in stringGetal:
        return False
    else:
        getalList = [int(d) for d in stringGetal]
        midden = len(getalList) // 2
        getalList1 = getalList[0:midden]
        if len(getalList) % 2 == 0:
            getalList2 = getalList[midden:len(getalList)]
        else:
            if str(getalList[midden]) in '6, 9':
                return False
            getalList2 = getalList[midden+1:len(getalList)]
        getalList2.reverse()
        check = True
        for k,v in enumerate(getalList1):
            if str(getalList1[k]) in '0, 1, 8' and getalList2[k] != getalList2[k]:
                check = False
                break
            if getalList1[k] == 6 and getalList2[k] != 9:
                check = False
                break
            if getalList1[k] == 9 and getalList2[k] != 6:
                check = False
                break
        return check

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

def csom(getal):
    while getal // 10 != 0:
        getal = csom_recursive(getal)
    else:
        return getal

def csom_recursive(input):
    som = 0
    while input // 10 != 0:
        # do something
        som += (input % 10)
        input //= 10
    else:
        som += input % 10
    return som