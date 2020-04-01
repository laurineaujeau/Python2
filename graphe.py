from noeud import noeud
from lien import lien
class graphe:

    def __init__ (self,idGraphe):
        self._idGraphe=idGraphe
        self._nbNoeud=0
        self._dicoNoeuds={}
        self._dicoLiens={}

    def getNbNoeud(self,nbNoeud):
        return self._nbNoeud

    def ajoutNoeud(self,nomNoeud):
        idNoeud=nomNoeud.getIdNoeud()
        self._nbNoeud+=1
        self._dicoNoeuds[idNoeud]=nomNoeud

    def ajoutLien(self, xtremite1id, extremite2id, distance):
        noeud1 = self._dicoNoeuds[int(xtremite1id)]
        noeud2 = self._dicoNoeuds[int(extremite2id)]
        lien1 = lien(noeud1,noeud2, float(distance))
        lien1id = lien1.getId()
        self._dicoLiens[lien1id]=lien1
        noeud1.ajoutIdentifiantLien(lien1id)
        noeud2.ajoutIdentifiantLien(lien1id)

    #def obtenirProchainsNoeud(self):

    def __str__(self):
        print(noeud.listNoeuds)
        print(noeud.listLiens)
