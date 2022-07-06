class BinaryHeap:

    def __init__(self, max_size=10):
        self.arr = [None]*max_size
        self.max_lengte = max_size
        self.aantal_elementen = 0

    def empty(self):
        return self.aantal_elementen == 0

    def get_min_elem(self):
        assert not self.empty(), 'the are no items in this binary heap'
        return self.arr[0]

    def insert_elem(self, item):
        assert self.aantal_elementen < self.max_lengte, 'binary heap is full'
        currentindex = self.aantal_elementen
        self.arr[currentindex] = item
        self.aantal_elementen += 1
        # parent
        parentindex = (currentindex - 1) // 2
        while currentindex > 0 and self.arr[currentindex] < self.arr[parentindex]:
            temp = self.arr[currentindex]
            self.arr[currentindex] = self.arr[parentindex]
            self.arr[parentindex] = temp
            currentindex = parentindex
            parentindex = (currentindex - 1) // 2

    def remove_min_elem(self):
        assert not self.empty(), 'the are no items in this binary heap'
        currentindex = 0
        result = self.arr[currentindex]
        self.arr[currentindex] = self.arr[self.aantal_elementen - 1]
        self.arr[self.aantal_elementen - 1] = None
        self.aantal_elementen -= 1
        # links
        linksindex = 1
        # rechts
        rechtsindex = 2

        while (linksindex < self.aantal_elementen and self.arr[linksindex] < self.arr[currentindex]) or (rechtsindex < self.aantal_elementen and self.arr[rechtsindex] < self.arr[currentindex]):
            if rechtsindex >= self.aantal_elementen:
                # wissel met links
                temp = self.arr[currentindex]
                self.arr[currentindex] = self.arr[linksindex]
                self.arr[linksindex] = temp
                currentindex = linksindex
            elif self.arr[linksindex] <= self.arr[rechtsindex]:
                # wissel met links
                temp = self.arr[currentindex]
                self.arr[currentindex] = self.arr[linksindex]
                self.arr[linksindex] = temp
                currentindex = linksindex
            else:
                #wissel met rechts
                temp = self.arr[currentindex]
                self.arr[currentindex] = self.arr[rechtsindex]
                self.arr[rechtsindex] = temp
                currentindex = rechtsindex
            linksindex = (2 * currentindex) + 1
            rechtsindex = (2 * currentindex) + 2
        return result

    def __str__(self):
        output = "["
        for i in range(self.aantal_elementen):
            output += str(self.arr[i]) + ', '
        if not self.empty():
            output = output[:-2]
        output += "]"
        return output