def vertalingToevoegen(key, value, dictionary):
    dictionary[key] = value

def vertaling(key, dictionay):
    if key in dictionay:
        return dictionay[key]
    else:
        return '???'

def overzicht(inputlijst):
    d = {'Engelstalige landen': 0,
        'Franstalige landen': 0,
        'Duitstalige landen': 0,
        'Japan': 0,
        'Russischtalige landen': 0,
        'China': 0,
        'Overige landen': 0,
        'Fouten': 0 }
    for i in range(len(inputlijst)):
        # valideer
        eancode = inputlijst[i]
        if valideer(eancode):
            if eancode[3] in ['0','1']:
                d['Engelstalige landen'] += 1
            if eancode[3] == '2':
                d['Franstalige landen'] += 1
            if eancode[3] == '3':
                d['Duitstalige landen'] += 1
            if eancode[3] == '4':
                 d['Japan'] += 1
            if eancode[3] == '5':
                d['Russischtalige landen'] += 1
            if eancode[3] == '7':
                d['China'] += 1
            if eancode[3] in ['6','8','9']:
                d['Overige landen'] += 1

        else:
            d['Fouten'] += 1
    for k, v in d.items():
        print(f'{k}: {v}')

def valideer(eancode):
    if eancode[:3] == '978' or  eancode[:3] == '979':
        o = 0
        for s in range(0, len(eancode) - 1, 2):
            o += int(eancode[s])
        e = 0
        for s in range(1, len(eancode) - 1, 2):
            e += int(eancode[s])
        x13 = (10 - (o + (3 * e)) % 10) % 10
        if x13 == int(eancode[-1]):
            return True
        else:
            return False
    else:
        return False

def ontleding(akkoord):
    if '#' in akkoord:
        grondnoot = akkoord[:2]
        type = akkoord[2:]
    else:
        grondnoot = akkoord[0]
        type = akkoord[1:]
    return grondnoot, type

def noten(grondnoot, toonintervallen):
    toonladder = [
        'C',
        'C#',
        'D',
        'D#',
        'E',
        'F',
        'F#',
        'G',
        'G#',
        'A',
        'A#',
        'B'
    ]
    output = []
    for interval in toonintervallen:
        index = toonladder.index(grondnoot)
        if interval + index < len(toonladder):
            output.append(toonladder[interval + index])
        else:
            index = interval + index - len(toonladder)
            output.append(toonladder[index])
    return output

def akkoord(akkoord, akkoordtypes, akkoordsymbolen):
    grondnoot, type = ontleding(akkoord)
    symbool = akkoordsymbolen[type]
    muzieknoten = akkoordtypes[symbool]
    return (tuple(noten(grondnoot, muzieknoten)))


def letterfrequenties(inputstring):
    alfabetfrequentie={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    alfabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for item in inputstring:
        loweritem = item.lower()
        if loweritem in alfabetlist:
            alfabetfrequentie[loweritem] += 1
    returnfrequentie = alfabetfrequentie.copy()
    for k, v in alfabetfrequentie.items():
        if v == 0:
            del returnfrequentie[k]
    return returnfrequentie

def letterposities(inputstring):
    alfabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    alfabetpositielist = {}
    for letter in alfabetlist:
        positielist = []
        for i in range(len(inputstring)):
            loweritem = inputstring[i].lower()
            if loweritem == letter:
                positielist.append(i)
        alfabetpositielist[letter] = set(positielist)
    returnpositielist = alfabetpositielist.copy()
    for k, v in alfabetpositielist.items():
        if not v:
            del returnpositielist[k]
    return returnpositielist

def omgekeerd(inputsleutel):
    returnsleutel = {}
    for k, v in inputsleutel.items():
        returnsleutel[v] = k
    return returnsleutel

def code39(inputstring, sleutel):
    outputstring = ''
    for kar in inputstring:
        outputstring += sleutel[kar.upper()]
        outputstring += 's'
    return outputstring[:-1]

def decode39(gecodeerd, sleutel):
    outputstring = ''
    # take 9 characters
    for i in range(0, len(gecodeerd), 10):
        code = gecodeerd[i:i+9]
        outputstring += omgekeerd(sleutel)[code]
    return outputstring

def dubbel(inputlist):
    inputset = set(inputlist)
    for item in inputset:
        if inputlist.count(item) > 1:
            return item

def dubbels(inputlist):
    inputset = set(inputlist)
    wel_dubbels = []
    geen_dubbels = []
    for item in inputset:
        if inputlist.count(item) > 1:
            wel_dubbels.append(item)
        else:
            geen_dubbels.append(item)
    return set(geen_dubbels), set(wel_dubbels)


def samenvoegen(glijbanen, ladders):
    try:
        samengevoegd = {}
        dubbel = checkDubbel(glijbanen, ladders)
        glijbanenOK = checkGlijbanen(glijbanen)
        laddersOK = checkLadders(ladders)
        if dubbel or checkGlijbanen(glijbanen) or checkLadders(ladders):
            raise AssertionError('ongeldige opstelling')
        for k,v in glijbanen.items():
            samengevoegd[k] = (k - v) * -1
        for k,v in ladders.items():
            samengevoegd[k] = v - k
        return samengevoegd
    except AssertionError:
        raise

def vakjes(worpen, glijbanen, ladders):
    try:
        mijnVakjes = []
        positie = 0
        dubbel = checkDubbel(glijbanen, ladders)
        glijbanenOK = checkGlijbanen(glijbanen)
        laddersOK = checkLadders(ladders)
        if dubbel or checkGlijbanen(glijbanen) or checkLadders(ladders):
            raise AssertionError('ongeldige opstelling')
        samengevoegd = samenvoegen(glijbanen,ladders)
        for worp in worpen:
            positie += worp
            if positie > 100:
                positie -= worp
            if positie in samengevoegd:
                positie += samengevoegd[positie]
            mijnVakjes.append(positie)
        return mijnVakjes
    except AssertionError:
        raise

def checkDubbel(glijbanen, ladders):
    glijbanenSet = set(glijbanen)
    laddersSet = set(ladders)
    return glijbanenSet & laddersSet

def checkGlijbanen(glijbanen):
    for k, v in glijbanen.items():
        if v >= k:
            return True
    return False

def checkLadders(ladders):
    for k, v in ladders.items():
        if k >= v:
            return True
    return False