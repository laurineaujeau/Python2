from noeud import noeud
from lien import lien
class graphe:

    def __init__ (self,idGraphe):
        self._idGraphe=idGraphe
        self._nbNoeud=0
        self._dicoNoeuds={}
        self._dicoLiens={}

    def getNbNoeud(self):
        return self._nbNoeud

    def ajoutNoeud(self,nomNoeud):
        idNoeud=nomNoeud.getIdNoeud()
        self._nbNoeud+=1
        self._dicoNoeuds[idNoeud]=nomNoeud

    def ajoutLien(self, extremite1id, extremite2id, distance):
        noeud1 = self._dicoNoeuds[int(extremite1id)]
        noeud2 = self._dicoNoeuds[int(extremite2id)]
        lien1 = lien(noeud1,noeud2, float(distance))
        lien1id = lien1.getId()
        self._dicoLiens[lien1id]=lien1 # j'ajoute le lien créé dans le dico des Liens
        noeud1.ajoutIdentifiantLien(lien1id)
        noeud2.ajoutIdentifiantLien(lien1id)

    def obtenirProchainsNoeuds(self,idNoeud):
        dicoAdjacents={} # self c'est que pour les variables de la classe
                        # la, je créé mon dico seulement dans cette fonction, il n'apparait pas dans un classe donc pas de self

        noeud1 = self._dicoNoeuds[idNoeud]
        listeLiens = noeud1.getList() # pour faire qlc.fonction il faut que qlc soit un objet créé

        for idLien in listeLiens:
            lien1 = self._dicoLiens[idLien]
            if (idNoeud==lien1.getExtremite1().getIdNoeud()): # je compare id recu en parametre avec l'un des noeuds
                                                        # du lien si c'est bien lui, je mets son extrémité dans le dico
                dicoAdjacents[lien1.getExtremite2()] = lien1.getDistance()
                #  dico[cle] = valeur
                # ici, j'associe le noeud suivant à la distance enre celui la et le noeud actuel
            else:
                dicoAdjacents[lien1.getExtremite1()] = lien1.getDistance()

        return dicoAdjacents

    def dijkstra (self,depart, arrivee):
        noeudsVisites ={}
        distanceMin={}
        for idNoeud in self._dicoNoeuds:
            distanceMin[idNoeud]=1000
        while len(noeudsVisites) != self.getNbNoeud():
            noeud1=self._dicoNoeuds[depart]
            idNoeud1=noeud1.getIdNoeud()
            if not (idNoeud1 in noeudsVisites):
                noeudsVisites[idNoeud1]=0
                if idNoeud1==arrivee:
                    break
                else:
                    poids= self.obtenirProchainsNoeuds(depart) # poids = dicoAdjacent de départ
                    distanceMin[idNoeud1]= min(distanceMin[idNoeud1],distanceMin[depart]+poids[idNoeud1]) #poids[idNoeud1] = distance de depart à idNoeud1
                    depart = idNoeud1 #j'avance dans mon graphe
        return noeudsVisites,distanceMin

    def dijkstraAlgorithm(self, depart, arrivee):
         prochainsNoeuds = self.obtenirProchainsNoeuds(depart)
         print()





