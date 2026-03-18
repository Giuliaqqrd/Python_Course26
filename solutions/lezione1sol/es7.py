import math
import matplotlib.pyplot as plt

def assegna_punto(punto, centroide1, centroide2):
    """Restituisce a quale centroide appartiene il punto (1 o 2)."""
    distanza1 = math.dist(punto, centroide1)
    distanza2 = math.dist(punto, centroide2)
    if distanza1 <= distanza2:
        return 1
    else:
        return 2

def crea_cluster(punti, centroide1, centroide2):
    """Costituisce i due cluster assegnando ogni punto al centroide più vicino."""
    cluster1 = []
    cluster2 = []
    for punto in punti:
        if assegna_punto(punto, centroide1, centroide2) == 1:
            cluster1.append(punto)
        else:
            cluster2.append(punto)
    return cluster1, cluster2

def visualizza_cluster(cluster1, cluster2, centroide1, centroide2):
    """Visualizza i due cluster."""
    x1, y1 = zip(*cluster1)
    x2, y2 = zip(*cluster2)
    plt.scatter(x1, y1, color='blue', label='Cluster 1')
    plt.scatter(x2, y2, color='red', label='Cluster 2')
    plt.scatter(*centroide1, color='cyan', marker='X', s=200, label='Centroide 1')
    plt.scatter(*centroide2, color='magenta', marker='X', s=200, label='Centroide 2')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Visualizzazione dei Cluster')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    punti = [(1, 2), (2, 1), (6, 5), (7, 8), (1, 0), (8, 7)]
    centroide1 = (0, 0)
    centroide2 = (7, 7)
    cluster1, cluster2 = crea_cluster(punti, centroide1, centroide2)
    visualizza_cluster(cluster1, cluster2, centroide1, centroide2)

if __name__ == "__main__":    
    main()