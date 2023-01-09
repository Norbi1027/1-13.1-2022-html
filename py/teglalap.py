class Téglalap:
   def __init__(self, a = 0, b = 0):
      self.a = a
      self.b = b
   
   def SetA(self, a):
      self.a = a
   def SetB(self, b):
      self.b = b
   def SetAB(self, a, b):
      self.a = a
      self.b = b
   
   def GetA(self):
      return self.a
   def GetB(self):
      return self.b
   def GetKerület(self):
      return 2 * (self.a + self.b)
   def GetTerület(self):
      return self.a * self.b

class négyzet:
    def __init__(self,a = 0):
        self.a = a

    def SetA(self,a):
        self.a = a
    def GetA(self,a):
        self.a = a
    def GetKerület(self):
        return 4*(self.a)
    def GetTerület(self):
        return self.a*self.a
class kör:
    def __init__(self,r = 0):
        self.r = r

    def Setr(self,r):
        self.r = r
    def getr(self,r):
        self.r = r
    def getkerület(self):
        return 2*(self.r)*3.14
    def getterület(self):
        return ((3.14)*(2*self.r))/4

class téglalap_hasab():
    def __init__(self,a = 0,b = 0,m = 0,):
        self.a = a
        self.b = b
        self.m = m
    def seta(self,a):
        self.a =a
    def setb(Self,b):
        self.b = b
    def setm(self,m):
        self.m = m

    def geta(self):
        return self.a
    def getb(Self):
        return self.b
    def getm(self):
        return self.m
    
    def getfelület(self):
        return ((self.a*self.b)+(self.a*self.m)+(self.b*self.m))*2
    def gettérfogat(self):
        return self.a*self.b*self.m
    