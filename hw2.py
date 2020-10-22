class Point:
    #class variables define min/max coords
    n=0
    sumP = []
    Pcentroid = None
    
    @classmethod
    def sumpoints(cls, pList=[]):
        try:
            if cls.n==0:
                cls.sumP = pList
            else:
                cls.sumP = [a+b for a,b in zip(cls.sumP,pList)]
        except IndexError:
            print('Caught dismatch matrices!')
        except:
            print('Caught an exception!')
        cls.n+=1
        cls.calcentroid(cls.sumP)
        
    @classmethod
    def calcentroid(cls, pList=[]):
        cls.Pcentroid = [k/cls.n  for k in pList]
    
    @classmethod
    def centroid(cls, pList=[]):
        return Point(cls.Pcentroid)
    
    def make_P(self,l):
        return Point(l)
    
    def __init__(self, *coords):
        self.coords = self.pTolist(coords)
        self.sumpoints(self.coords)
        
    #move the point by x,y
    def moveBy(self,*x):
        for i in range(len(x)):
            self.coords[i]+=x[i]
            
    #move the point to x,y
    def moveTo(self,*x):
        for i in range(len(x)):
            self.coords[i]=x[i]
            
    def distanceTo(self, *p2):
        temp = 0
        try:
            for i in range(len(self.pTolist(p2))):
                temp+=abs(int(self.coords[i])-self.pTolist(p2)[i])**2
            return temp**0.5
        except IndexError:
            print('Caught dismatch matrices!')
        except:
            print('Caught an exception!')
            
    def pTolist(self,tup):
        s = str(tup)
        for i in s:
            if not (i.isdigit() or i==","):
                s = s.replace(i,"")
        s = s.rstrip(",")
        return [int(i) for i in s.split(",")]
        
    def __add__(self, other):
        return [a+b for a,b in zip(self.coords, other.coords)]
        
    def __sub__(self, other):
        return [a-b for a,b in zip(self.coords, other.coords)]
        
    def __mul__(self, other):
        return [i*other for i in self.coords]
            
    def __rmul__(self, other):
        return [i*other for i in self.coords]
        
    def __gt__(self, other):
        b = True
        for i in range(len(self.coords)):
            b = b and self.coords[i]>other.coords[i]
        return b
        
    def __eq__(self, other):
        b = True
        for i in range(len(self.coords)):
            b = b and self.coords[i]==other.coords[i]
        return b
        
    def __getitem__(self, key):
        return int(self.coords[key])
    
    def __setitem__(self, key, value):
        self.coords[key] = value
    
    def __str__(self):
        return str(self.coords)
    
    def __repr__(self):
        return str(self.coords)
