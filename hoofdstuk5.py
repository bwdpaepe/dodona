def precies_een_verschillend(woord1, woord2):
    if len(woord1) != len(woord2):
        return False
    aantal = 0
    for i in range(len(woord1)):
        if woord1[i] != woord2[i]:
            aantal += 1
    return aantal == 1

def maak_graaf(woorden):
    dict={woord: set() for woord in woorden}
    for i, woord1 in enumerate(woorden):
        for j in range(i+1, len(woorden)):
            if precies_een_verschillend(woord1, woorden[j]):
                dict[woord1].add(woorden[j])
                dict[woorden[j]].add(woord1)

    return dict

def kortste_pad(graaf, woord):
    D = {w: -1 for w in graaf}
    P = {w: None for w in graaf}
    D[woord] = 0
    P[woord] = woord
    Q = []
    Q.append(woord)
    while len(Q) > 0:
        v = Q.pop(0)
        for w in sorted(graaf[v]):
            if D[w] == -1:
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
    return P

def geef_pad(vorigeKnopen, doel):
    alleVorige = []
    huidige = doel
    vorige = vorigeKnopen[huidige]
    alleVorige.append(doel)
    while huidige != vorige:
        alleVorige.insert(0, vorige)
        huidige = vorige
        vorige = vorigeKnopen[huidige]

    return alleVorige

#def woordladder():
