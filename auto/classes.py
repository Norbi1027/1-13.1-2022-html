import math

class Menetlevél:
    def __init__(self, rendszam):
        self.rendszam = rendszam
    def setMegtettkm(self, megtettkm):
        self.megtettkm = megtettkm
    def setÖsszÜzemanyag(self, ÖsszÜzemanyag):
        self.ÖsszÜzemanyag = ÖsszÜzemanyag

    def atlagfogyasztas(self):
        atlag = self.összüzemanyag / (self.megtettkm /100)  
        return math.round(atlag, 2)
    def getrendszam(self):
        return self.rendszam