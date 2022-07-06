def zoekBinair(rij, zoekItem):
    l = 0
    r = len(rij) - 1
    while l != r:
        print(f"{l}, {r}")
        m = (l + r) // 2
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m

    if rij[l] == zoekItem:
        return l
    else:
        return -1

def selection_sort_vooraan(a):
    for i in range(len(a) - 1):
        positie = i
        minimum = a[i]
        for j in range(i + 1, len(a)):
            if a[j] < minimum:
                positie = j
                minimum = a[j]
        a[positie] = a[i]
        a[i] = minimum
        print(a)

def bubble_sort(a):
    counter = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            counter += 1
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]
        print(a)
    print(f"Voor een rij van lengte {len(a)} werd het if-statement {counter} keer uitgevoerd")

