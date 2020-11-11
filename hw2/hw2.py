
class Point:
    sumP = None
    Pcentroid = None
    
    @classmethod
    def centroid(cls, pList=[]):
        cls.sumP = Point([0 for i in range(len(pList[0]))])
        for i in range(len(pList)):
            cls.sumP = cls.sumP + pList[i]
            cls.Pcentroid = cls.sumP*(1/len(pList))
        return cls.Pcentroid
    
    def __init__(self, *coords):
        self.coords = self.pTolist(coords)
        
    def moveBy(self,*x):
        for i in range(len(x)):
            self.coords[i]+=x[i]
            
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
        pList=[]
        s = str(tup)
        for i in s:
            if not (i.isdigit() or i=="," or i=="." or i=="-"):
                s = s.replace(i,"")
        s = s.rstrip(",")
        for i in s.split(","):
            if str(i).split(".")[-1]=='0' or len(str(i).split("."))==1:
                pList.append(int(float(i)))
            else:
                pList.append(float(i))
        return pList
    
    def __add__(self, other):
        return Point([a+b for a,b in zip(self.coords, other.coords)])
        
    def __sub__(self, other):
        return Point([a-b for a,b in zip(self.coords, other.coords)])
        
    def __mul__(self, other):
        return Point([i*other for i in self.coords])
            
    def __rmul__(self, other):
        return Point([i*other for i in self.coords])
        
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
    
    def __len__(self):
        return len(self.coords)
