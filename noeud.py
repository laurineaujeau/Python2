from lien import lien
class noeud :
    id=0

    def __init__(self):
        noeud.id=noeud.id+1
        self.__id=noeud.id
        self.__listLiens=list()

    def ajoutIdentifiantLien(self,idLien):
        self.__listLiens.append(idLien)

    def getIdNoeud(self):
        return self.__id

    def __str__(self):
        print(self.__id)

