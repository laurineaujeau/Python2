from noeud import noeud
from lien import lien
from graphe import graphe
import csv



def creationGraphe (idGraphe,url):
    graph1=graphe(idGraphe)
    with open(url) as f:
        f_csv = csv.reader(f)
        en_tete = next(f_csv) #on prends la premiere ligne et on l'ecarte pour n'avoir que les lignes de lien
        for _ in range(int(en_tete[0])):
            n1 = noeud()
            graph1.ajoutNoeud(n1)
        for ligne in f_csv:
            ligne = str(ligne[0])
            ligne = ligne.split("\t")
            graph1.ajoutLien(ligne[0],ligne[1],ligne[2])
    return graph1

g1 = creationGraphe(1,"fileGraph1.csv")
g1.dijkstraAlgorithm(1, 4)#test
g1.dijkstra(1, 4)# original, ne fonctionne pas





