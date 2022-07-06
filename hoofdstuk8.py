import sys


def afstand2(punt1, punt2):
    """ Gekwadrateerde Euclidische afstand tussen de twee tupels punt1 en punt2
    """
    #punt1 = (x, y, z, ..)
    #punt2 = (x, y, z, ..)
    afstand = 0
    for i, x1 in enumerate(punt1):
        x2 = punt2[i]
        afstand += (abs(x1 - x2))**2

    return afstand


def index_dichtste(punt, centroids):
    """ Geef de index (vanaf 0) van de centroid die het dichtste bij punt gelegen is.
    """
    #punt = (x, y)
    #centroids = [(x, y), (x, y), ..., (x, y)]
    besteIndex = 0
    besteAfstand = sys.maxsize
    for k, v in enumerate(centroids):
        if afstand2(punt, v) < besteAfstand:
            besteIndex = k
            besteAfstand = afstand2(punt, v)


    return besteIndex


def cluster_assignatie(punten, centroids):
    #  Geef geef voor elk punt de index van de dichtste centroïde(vanaf 0) van de centroide die het dichtste bij punt gelegen is.
    clusterAssignatieRij = [-1]*len(punten)
    for k, v in enumerate(punten):
        indexDichtste = index_dichtste(v, centroids)
        clusterAssignatieRij[k]=indexDichtste


    return clusterAssignatieRij


def bereken_centroid(punten):
    # bereken het zwaartepunt van de gegeven punten
    centroid = list(punten[0])
    for punt in punten[1:]:
        for index, coord in enumerate(punt):
            centroid[index] += coord
    centroid = [c / len(punten) for c in centroid]
    return tuple(centroid)


def update_centroids(punten, assignatie, aantal_clusters):
    # bepaal de nieuwe zwaartepunten gegeven de punten, de assignatie en het aantal clusters
    # punten = [(x, y), (x, y), ..., (x, y)]
    # assignatie = [1, 3, .., 2]
    # aantal_cluster = 3
    centroids = []
    for k in range(aantal_clusters):
        centroids.append(bereken_centroid([p for i, p in enumerate(punten) if assignatie[i] == k]))
    return centroids

def k_gemiddelden(punten, centroids):
    # implementeer het k-gemiddelden algoritme op een rij van punten en de centroides als argumenten. Retourneer de centroids nadat het algoritme geconvergeerd is

    hasChanged = True
    while hasChanged:
        assignatie = cluster_assignatie(punten, centroids)
        nCentroids = update_centroids(punten, assignatie, len(centroids))
        hasChanged = False
        for i,c in enumerate(centroids):
            if c != nCentroids[i]:
                hasChanged = True
        centroids = nCentroids
    return centroids






