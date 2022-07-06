import sys

class HashSet:
    collectie = []
    grootte = -sys.maxsize - 1

    FLAG = -9999
    def __init__(self, max_size=10):
        self.grootte = max_size
        self.collectie = [None for i in range(max_size)]
        #self.collectie = [None]*max_size
        #aantal elementen in collectie
        self.nb = 0

    def add(self, item):
        if self.nb == self.grootte:
            raise ValueError()
        h = hash(item) % self.grootte
        while self.collectie[h] != None and self.collectie[h] != HashSet.FLAG:
            print(h)
            h = (h + 1) % self.grootte
        self.collectie[h] = item
        self.nb += 1
        return h


    def index_of(self, item):
        h = hash(item) % self.grootte
        returnWaarde = -1
        startH = h
        while(self.collectie[h] != item):
            if self.collectie[h] == None:
                return -1
            print(h)
            h = (h + 1) % self.grootte
            if startH == h:
                return -1
        return h


    def delete(self, item):
        plaats = self.index_of(item)
        if plaats == -1:
            return False
        else:
            self.collectie[plaats] = HashSet.FLAG
            self.nb -= 1
            return True


def twoSum(rij, doel):
    for i in range(len(rij) - 1):
        for j in range(i + 1,len(rij)):
            if rij[i] + rij[j] == doel:
                return (i, j)
    return None


def twoSumHash(rij, doel):
    maximum = max(rij) + 1
    hashTabel = [None]*maximum
    for i in range(len(rij)):
        zoek = doel - rij[i]
        if zoek >= 0 and hashTabel[zoek] != None:
            return(hashTabel[zoek],i)
        else:
            hashTabel[rij[i]] = i
    return None

