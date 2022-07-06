import heapq


class AchtPuzzel:
    BUREN = {0: {("R", 1), ("O", 3)}, 1: {("L", 0), ("R", 2), ("O", 4)}, 2: {("L", 1), ("O", 5)},
             3: {("B", 0), ("R", 4), ("O", 6)}, 4: {("B", 1), ("L", 3), ("R", 5), ("O", 7)},
             5: {("B", 2), ("L", 4), ("O", 8)},
             6: {("B", 3), ("R", 7)}, 7: {("B", 4), ("L", 6), ("R", 8)}, 8: {("B", 5), ("L", 7)}
             }

    def __init__(self, bord='123456780'):
        assert set(bord) == set("012345678"), "geen correct bord"
        # self.bord = [int(d) for d in bord]
        self.bord = bord

    def __str__(self):
        return self.bord[:3] + "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"

    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False

    def __hash__(self):
        return hash(self.bord)

    def opvolgers(self):
        positieVanHetGat = self.bord.index("0")
        tupelsVanActieMetNieuwePositie = AchtPuzzel.BUREN[positieVanHetGat]
        resultaat = set()
        for kandidaatActie in tupelsVanActieMetNieuwePositie:
            actie = kandidaatActie[0]
            nieuwePositie = kandidaatActie[1]
            nieuwbord = self.bord
            temp = nieuwbord[nieuwePositie]
            nieuwbord = self.bord.replace(temp, "9")
            nieuwbord = nieuwbord.replace("0", temp)
            nieuwbord = nieuwbord.replace("9", "0")
            resultaat.add((actie, AchtPuzzel(nieuwbord)))

        return resultaat

    def aantal_verkeerd(self, andere_puzzel):
        aantal_verkeerd = 0
        for k, v in enumerate(self.bord):
            if v != "0" and self.bord[k] != andere_puzzel.bord[k]:
                aantal_verkeerd += 1
        return aantal_verkeerd

    def manhattan_heuristiek(self, andere_puzzel):
        totaal = 0
        for k, v in enumerate(self.bord):
            if v != "0":
                rij_bord = k // 3
                kolom_bord = k % 3

                andere_index = andere_puzzel.bord.index(v)

                rij_andere = andere_index // 3
                kolom_andere = andere_index % 3

                manhattan = abs(rij_andere - rij_bord) + abs(kolom_andere - kolom_bord)

                totaal += manhattan

        return manhattan


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand
        self.voorganger = voorganger
        self.actie = actie
        self.kost = kost
        self.h_waarde = h_waarde

    ## Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        self.f = self.kost + self.h_waarde
        other_f = other.kost + other.h_waarde

        return self.f < other_f

    def geef_actie_sequentie(self):
        resultaat = []
        huidigplan = self
        while huidigplan.voorganger != None:
            resultaat.append(huidigplan.actie)
            huidigplan = huidigplan.voorganger

        resultaat = resultaat[::-1]
        return resultaat

def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost= lambda s,a : 1):
    fRij = []
    closedRij = set()
    heapq.heappush(fRij, Plan(start_toestand))
    while len(fRij) > 0:
        plan = heapq.heappop(fRij)
        toestand = plan.toestand
        if is_doel(toestand):
            return (plan.geef_actie_sequentie(), plan.kost)
        else:
            # doel nog niet bereikt
            # volgende 2 rijen zijn voor graafgebaseerd
            if toestand not in closedRij:
                closedRij.add(toestand)
                for (actie, nieuweToestand) in sorted(toestand.opvolgers()):
                    heapq.heappush(fRij, Plan(nieuweToestand, plan, actie, plan.kost + kost(toestand, actie),
                                              heuristiek(nieuweToestand)))
    return None
