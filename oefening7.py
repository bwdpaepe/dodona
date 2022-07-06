import re
import sys
sys.tracebacklimit = 1
class BankRekening:

    def __init__(self, naam, nummer, bedrag = 0):
        self.naam = naam
        self.nummer = nummer
        self.bedrag = bedrag

    def __str__(self):
        return (f'{self.naam}, {self.nummer}, bedrag: {self.bedrag}')

    def __repr__(self):
        rep = self.__class__.__name__ + "('" + self.naam + "', '" + str(self.nummer) + "', " + str(self.bedrag) + ")"
        return (rep)

    def storten(self, n):
        self.bedrag += n

    def afhalen(self, n):
        self.bedrag -= n

class Kaart:

    alleRang = ["aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer"]
    alleKleur = ["klaveren", "ruiten", "harten", "schoppen"]

    def __init__(self, rang, kleur):
        try:
            if not rang in Kaart.alleRang or not kleur in Kaart.alleKleur:
                raise AssertionError('ongeldige kaart')
            self.rang = rang
            self.kleur = kleur
        except AssertionError:
            raise

    def __repr__(self):
        rep = self.__class__.__name__ + "(rang='" + self.rang + "', kleur='" + str(self.kleur) + "')"
        return (rep)

    def __str__(self):
        return (f'{self.kleur} {self.rang}')

    def __lt__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnRang < andereRang:
            return True
        elif mijnRang > andereRang:
            return False
        else:
            if mijnKleur < andereKleur:
                return True
            else:
                return False

    def __gt__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnRang > andereRang:
            return True
        elif mijnRang < andereRang:
            return False
        else:
            if mijnKleur > andereKleur:
                return True
            else:
                return False

    def __le__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnRang < andereRang:
            return True
        elif mijnRang > andereRang:
            return False
        else:
            if mijnKleur <= andereKleur:
                return True
            else:
                return False

    def __ge__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnRang > andereRang:
            return True
        elif mijnRang < andereRang:
            return False
        else:
            if mijnKleur >= andereKleur:
                return True
            else:
                return False

    def __eq__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnKleur == andereKleur and mijnRang == andereRang:
            return True
        else:
            return False

    def __ne__(self, other):
        mijnRang = Kaart.alleRang.index(self.rang)
        mijnKleur = Kaart.alleKleur.index(self.kleur)
        andereRang = Kaart.alleRang.index(other.rang)
        andereKleur = Kaart.alleKleur.index(other.kleur)
        if mijnKleur != andereKleur or mijnRang != andereRang:
            return True
        else:
            return False

def vijfdeKaart(kaartenlijst):
    verborgenKleur = kaartenlijst[0].kleur
    if kaartenlijst[1] < kaartenlijst[2]:
        if kaartenlijst[2] < kaartenlijst[3]:
            volgorde = 1
        elif kaartenlijst[3] < kaartenlijst[1]:
            volgorde = 4
        else:
            volgorde = 2
    elif kaartenlijst[1] < kaartenlijst[3]:
        volgorde = 3
    else:
        if kaartenlijst[3] < kaartenlijst[2]:
            volgorde = 6
        else:
            volgorde = 5
    nieuweRang = Kaart.alleRang.index(kaartenlijst[0].rang) + volgorde
    if nieuweRang > 12:
        nieuweRang = nieuweRang % 13
    return Kaart(Kaart.alleRang[nieuweRang], verborgenKleur)

class Bifid:
    def __init__(self, n, codetabel):
        try:
            if n < 2 or n > 10:
                raise AssertionError('er moet gelden dat 2 <= n <= 10')
            if len(codetabel) != n**2:
                raise AssertionError('aantal symbolen komt niet overeen met grootte van het rooster')
            self.n = n
            self.codetabel = codetabel
        except AssertionError:
            raise

    def symbool(self, rij, kolom):
        try:
            if rij > self.n - 1  or kolom > self.n - 1 or rij < 0 or kolom < 0:
                raise AssertionError('ongeldige positie in rooster')
            return (self.codetabel[rij * self.n + kolom])
        except AssertionError:
            raise

    def positie(self, zoekterm):
        try:
            if len(zoekterm) != 1:
                raise AssertionError('symbool moet uit 1 karakter bestaan')
            if not zoekterm in self.codetabel:
                raise AssertionError(f"onbekend symbool: '{zoekterm}'")
            termIndex = self.codetabel.index(zoekterm)
            rij = termIndex // self.n
            kolom = termIndex % self.n
            return (rij, kolom)
        except AssertionError:
            raise

    def codeer(self, input):
        rijlijst = []
        kolomlijst = []
        for item in input:
            rijlijst.append(self.positie(item)[0])
            kolomlijst.append(self.positie(item)[1])
        rijlijst.extend(kolomlijst)
        code = ""
        for i in range(0, len(rijlijst), 2):
            code += self.symbool(rijlijst[i], rijlijst[i+1])
        return code

    def decodeer(self, input):
        positielijst = []
        for item in input:
            itempositie = self.positie(item)
            positielijst.append(itempositie[0])
            positielijst.append(itempositie[1])
        rijlijst = positielijst[:len(positielijst)//2]
        kolomlijst = positielijst[len(positielijst)//2:]
        decode = ""
        for i in range(len(rijlijst)):
            decode += self.symbool(rijlijst[i], kolomlijst[i])
        return decode

class Geohash36:
    klassieke_alfabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, geohash_code_string, alfabet = "23456789bBCdDFgGhHjJKlLMnNPqQrRtTVWX"):
        self.geohash_code_string = geohash_code_string
        self.geohash_code_origineel = geohash_code_string
        self.alfabet_string = alfabet
        self.u_lambda = 180.0
        self.l_lambda = -180.0
        self.u_phi = 90.0
        self.l_phi = -90.0
        try:
            alfabet_set = set(self.alfabet_string)
            geohash_code_checksum = False
            if len(self.alfabet_string) != 36 or len(alfabet_set) != len(self.alfabet_string) or not re.match('^\w*$', self.alfabet_string):
                raise AssertionError('ongeldig alfabet')
            if '-' in self.geohash_code_string:
                geohash_code_checksum = self.geohash_code_string[-1]
                self.geohash_code_string = self.geohash_code_string[:-2]
            cs = 0
            for geohash_code_karakter in self.geohash_code_string:
                if not geohash_code_karakter in self.alfabet_string:
                    raise AssertionError('ongeldige code')

            if '-' in self.geohash_code_origineel:
                if geohash_code_checksum != self.checksum():
                    raise AssertionError('ongeldige code')

        except AssertionError:
            raise

    def __str__(self):
        cs = self.checksum()
        return (f'{self.geohash_code_string}-{cs}')

    def __repr__(self):
        rep = self.__class__.__name__ + "('" + str(self) + "')"
        if self.alfabet_string != "23456789bBCdDFgGhHjJKlLMnNPqQrRtTVWX":
            rep = rep.rstrip(")")
            rep = rep + ", alfabet='" + self.alfabet_string + "')"
        return rep

    def checksum(self):
        cs = 0
        for i in range(len(self.geohash_code_string)):
            geohash_code_karakter = self.geohash_code_string[i]
            positie_in_string = len(self.geohash_code_string) - i
            positie_in_alfabet = self.alfabet_string.index(geohash_code_karakter)
            factor = positie_in_string * positie_in_alfabet
            cs += factor
        cs = cs % 26
        return Geohash36.klassieke_alfabet[cs]

    def positie(self, t):
        try:
            if not t in self.alfabet_string:
                raise AssertionError('ongeldig teken')
            positie_string = self.alfabet_string.index(t)
            rij = positie_string // 6
            rij = 5 - rij
            kolom = positie_string % 6
            return rij, kolom
        except AssertionError:
            raise

    def lengtegraad(self):
        for geohash_code_karakter in self.geohash_code_string:
            karakter_positie = self.positie(geohash_code_karakter)
            u = self.u_lambda
            l = self.l_lambda
            self.l_lambda = self.get_l_lambda(u, l, karakter_positie[1])
            self.u_lambda = self.get_u_lambda(u, l, karakter_positie[1])
        return (self.l_lambda, self.u_lambda)

    def breedtegraad(self):
        for geohash_code_karakter in self.geohash_code_string:
            karakter_positie = self.positie(geohash_code_karakter)
            u = self.u_phi
            l = self.l_phi
            self.l_phi = self.get_l_phi(u, l, karakter_positie[0])
            self.u_phi = self.get_u_phi(u, l, karakter_positie[0])
        return (self.l_phi, self.u_phi)

    def get_l_lambda(self, u, l, kolom):
        return l + (kolom * ((u-l) / 6))

    def get_u_lambda(self, u, l, kolom):
        return l + ((kolom + 1) * ((u-l) / 6))

    def get_l_phi(self, u, l, rij):
        return l + (rij * ((u - l) / 6))

    def get_u_phi(self, u, l, rij):
        return l + ((rij + 1) * ((u - l) / 6))

    def coordinaat(self):
        lengte_tup = self.lengtegraad()
        breedte_tup = self.breedtegraad()
        lengte = (lengte_tup[0] + lengte_tup[1]) / 2
        breedte = (breedte_tup[0] + breedte_tup[1]) / 2
        return (lengte, breedte)

