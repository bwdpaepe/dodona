import numbers


def evalueer_postfix(expressie):
    stapel = []
    for element in expressie:
        if element.isnumeric():
            stapel.append(float(element))
        else:
            value1 = stapel.pop()
            value2 = stapel.pop()
            if element == '+':
                stapel.append(value1 + value2)
            elif element == '-':
                stapel.append(value2 - value1)
            elif element == '*':
                stapel.append(value1 * value2)
            elif element == '/':
                stapel.append(value2 / value1)
    return stapel.pop()

def infix_naar_postfix(expressie):
    uitvoer = []
    stapel = []
    for element in expressie:
        if element.isnumeric():
            uitvoer.append(element)
        else:
            if element == ")":
                bovenste = stapel.pop()
                while bovenste != "(":
                    uitvoer.append(bovenste)
                    bovenste = stapel.pop()
            elif len(stapel) == 0 or prioriteit(element) > prioriteit(stapel[len(stapel)-1]) or element in ["("]:
                stapel.append(element)
            else:
                while len(stapel) > 0 and prioriteit(element) <= prioriteit(stapel[len(stapel)-1]):
                    uitvoer.append(stapel.pop())
                stapel.append(element)
    while len(stapel) > 0:
        uitvoer.append((stapel.pop()))
    return uitvoer


def rekenmachine(s):
    infix_tokens = s.split()
    postfix = infix_naar_postfix(infix_tokens)
    return evalueer_postfix(postfix)

def prioriteit(x):
    if x == '-':
        x = '+'
    if x == '/':
        x = '*'
    prioriteitsLijst = ['(', '+', '*']
    return prioriteitsLijst.index(x)

class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = None

    def empty(self):
        return True if self.top is None else False

    def push(self, data):
        hulp = self.Knoop(data, self.top)
        self.top = hulp

    def peek(self):
        return self.top.data

    def pop(self):
        x = self.top.data
        self.top = self.top.volgende
        return x

class QueueList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.kop = None
        self.staart = None

    def empty(self):
        return True if self.kop is None else False

    def enqueue(self, data):
        hulp = self.Knoop(data, None)
        if self.empty():
            self.kop = hulp
        else:
            self.staart.volgende = hulp
        self.staart = hulp

    def front(self):
        return self.kop.data

    def dequeue(self):
        x = self.kop.data
        if self.kop == self.staart:
            self.kop = None
            self.staart = None
        else:
            self.kop = self.kop.volgende
        return x

    def invert(self):
        vorige = None
        huidige = self.kop
        while huidige is not None:
            volgende = huidige.volgende
            huidige.volgende = vorige
            vorige = huidige
            huidige = volgende
        self.kop, self.staart = self.staart, self.kop



