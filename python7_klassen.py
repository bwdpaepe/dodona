class Dog:
    dogCount = 0
    def __init__(self, name):
        self.name = name
        self.tricks = []
        Dog.dogCount += 1

    def add_trick(self, trick):
        self.tricks.append(trick)

    def bark(self):
        return "woof"

    def __str__(self):
        return(f"The dogs name is {self.name} and it barks like {self.bark()}")

    def __repr__(self):
        return ("Dog, name: {}, noise: {}".format(self.name, self.bark()))

class Bankrekening:

    def __init__(self, naamRekeninghouder, rekeningNummer, saldo=0):
        self.naamRekeninghouder = naamRekeninghouder
        self.rekeningNummer = rekeningNummer
        self.saldo = saldo

    def __str__(self):
        return (f"{self.naamRekeninghouder}, {self.rekeningNummer}, bedrag: {self.saldo}")

    def __repr__(self):
        rep = self.__class__.__name__ + "('" + self.naam + "', '" + str(self.nummer) + "', " + str(self.bedrag) + ")"
        return rep

    def afhalen(self, bedrag):
        self.saldo -= bedrag

    def storten(self, bedrag):
        self.saldo += bedrag

class Kaart:

    alleRangen = ["aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer"]
    alleKleuren = ["klaveren", "ruiten", "harten", "schoppen"]

    def __init__(self, rang, kleur):
        if rang not in Kaart.alleRangen or kleur not in Kaart.alleKleuren:
            raise AssertionError('ongeldige kaart')
        self.rang = rang
        self.kleur = kleur



