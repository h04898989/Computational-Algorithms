#
# An n-Dimensional Point class (represents a coordinate in n-D space)
#
class Point:

    #class method to compute centroid from list of points
    @classmethod
    def centroid(cls,pList):
        if len(pList) < 1: raise Exception('centroid function requires at least one point!')
        dim=pList[0].dim
        centroid=Point([0]*dim)
        for pt in pList:
            pt.checkDim(dim)
            centroid=centroid+pt
        centroid=centroid*(1.0/len(pList))
        return centroid
        
    # __init__ function is the constructor
    def __init__(self,coords=[0,0]):
        self.coords=list(coords)  #list(...) should raise TypeError if coords not iterable
        if(len(coords) == 0):
            raise Exception() #no 0-d points allowed
        
    #__len__ returns dimensionality of the point
    def __len__(self):
        return len(self.coords) 
    
    #get coordinate value
    def __getitem__(self,i):
        return self.coords[i]

    #set coordinate value
    def __setitem__(self,i,val):
        self.coords[i]=val     
        
    #add two points    
    def __add__(self,other):
        self.checkDim(other.dim)
        
        tmp=[0]*self.dim    
        for i in range(self.dim):
            tmp[i]=self[i]+other[i]
            
        return Point(tmp)

    #subtract two points
    def __sub__(self,other):
        self.checkDim(other.dim)
        tmp=[0]*self.dim       
        for i in range(self.dim):
            tmp[i]=self[i]-other[i]
        return Point(tmp)
   
    #multiply scalar and point (p*scalar)
    def __mul__(self,scalar):
        tmp=[0]*self.dim
        for i in range(self.dim):
            tmp[i]=self[i]*scalar
        return Point(tmp)

    #multiply scalar and point (scalar*point)
    def __rmul__(self,scalar):
        return self.__mul__(scalar)
    
    #check if a point is greater-than another
    def __gt__(self,other):
        self.checkDim(other.dim)
        for i in range(self.dim):
            if self[i] <= other[i]: return False
        else:
            return True

    #check if two points are equal
    def __eq__(self,other):
        self.checkDim(other.dim)
        if self.coords == other.coords: return True
        else: return False
        
    #property to return the dimensionality of the point
    @property
    def dim(self):
        return len(self)

    #check point dimensionality
    def checkDim(self,dim):
        if self.dim != dim:
            raise Exception('Point dimensionality mismatch, {} != {}'.format(self.dim,dim))
        return True
     
    #move the point by delta 
    def moveBy(self,delta):
        self.checkDim(len(delta))
        for i in range(self.dim):
            self[i]+=delta[i]

    #move the point to specific coord
    def moveTo(self,coord):
        self.coords=Point(coord).coords

    #calculate Hamming distance between two points   
    def distanceTo(self, other):
        distance=0
        for i in range(self.dim):
            distance+=abs(self[i] - other[i])
        return distance
        
    # __str__ generates string representation of objects   
    def __str__(self):
        return 'Point: ' + str(self.coords)

import unittest
class TestPointClass(unittest.TestCase):
    def test_centroid(self):
        a = Point([1,2,3])
        b = Point([3,2,1])
        c = Point([-1,-1,-1])
        cen = Point.centroid([a,b,c])
        self.assertEqual(str(cen), 'Point: [1.0, 1.0, 1.0]')
    def test_len(self):
        a = Point([1,2,3])
        self.assertEqual(len(a),3)
    def test_get(self):
        a = Point([1,2,3])
        self.assertEqual(a[0],1)
    def test_set(self):
        a = Point([1,2,3])
        a[0]=3
        self.assertEqual(a[0],3)
    def test_add(self):
        a = Point([1,2,3])
        b = Point([1,2,2])
        self.assertEqual(str(a+b),'Point: '+'[2, 4, 5]')
    def test_sub(self):
        a = Point([1,2,3])
        b = Point([1,2,2])
        self.assertEqual(str(a-b),'Point: '+'[0, 0, 1]')
    def test_mul(self):
        a = Point([1,2,3])
        b = 2
        self.assertEqual(str(a*b),'Point: '+'[2, 4, 6]')
    def test_gl(self):
        a = Point([-1,2,3])
        b = Point([-2,-1,2])
        self.assertEqual(a>b,True)
    def test_eq(self):
        a = Point([1,2,3])
        b = Point([1,2,3])
        self.assertEqual(a==b,True)
    def test_checkDim(self):
        a = Point([1,2,3,4,5])
        self.assertEqual(a.checkDim(5),True)
    def test_moveBy(self):
        a = Point([1,2,3])
        a.moveBy([1,2,2])
        self.assertEqual(str(a),'Point: '+'[2, 4, 5]')
    def test_moveTo(self):
        a = Point([1,2,3])
        a.moveTo([1,2,2])
        self.assertEqual(str(a),'Point: '+'[1, 2, 2]')
    def test_distanceTo(self):
        a = Point([1,2,3])
        self.assertEqual(a.distanceTo([1,2,2]),1)
    def test_str(self):
        a = Point([1,2,3])
        self.assertEqual(str(a),'Point: '+'[1, 2, 3]')
    
if __name__ == '__main__':
    unittest.main()
    
