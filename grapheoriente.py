from graphe import graphe
class grapheoriente(graphe):
    def obtenirProchainsNoeuds(self,idNoeud):
        dicoAdjacents={}
        noeud1 = self._dicoNoeuds[idNoeud]
        listeLiens = noeud1.getList()
        for idLien in listeLiens:
            lien1 = self._dicoLiens[idLien]
            if (idNoeud==lien1.getExtremite1().getIdNoeud()):
                dicoAdjacents[lien1.getExtremite2()] = lien1.getDistance()

            #ici pas de else car le lien est unidirectionnel

        return dicoAdjacents
