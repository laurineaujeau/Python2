class lien :
    id=0
    def __init__(self,extremite1, extremite2, distance):
        lien.id=lien.id+1
        self.__extremite1 = extremite1
        self.__extremite2 = extremite2
        self.__distance = distance
        self.__id=lien.id

    def __str__(self):
        print(lien.id)

    def getExtremite1(self):
        return self.__extremite1

    def getExtremite2(self):
        return self.__extremite2

    def getDistance(self):
        return self.__distance

    def getId(self):
        return self.__id


