from noeud import noeud
from lien import lien
from graphe import graphe
import csv



def creationGraphe (idGraphe,url):
    kiki=graphe(idGraphe)
    with open(url) as f:
        f_csv = csv.reader(f)
        en_tete = next(f_csv) #on prends la premiere ligne et on l'ecarte pour n'avoir que les lignes de lien
        for _ in range(int(en_tete[0])):
            popo = noeud()
            kiki.ajoutNoeud(popo)
        for ligne in f_csv:
            ligne = str(ligne[0])
            ligne = ligne.split("\t")
            kiki.ajoutLien(ligne[0],ligne[1],ligne[2])
    return kiki

g1 = creationGraphe(1,"fileGraph2.csv")
print()

