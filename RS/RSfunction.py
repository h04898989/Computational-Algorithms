# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 07:20:24 2020

@author: dengcheng
"""
from scipy import optimize

class fit:
    '''
    用於對一組資料fitting，並以此做thresholding
    '''
    def fitfunction(self,x,a,b,c):
        return a*pow(x,2)+b*x+c
    
    def __init__(self):
        self.threshold = []
        self.ydata = []
    
    def thresholding(self,xdata,ydata,method):
        self.ydata = ydata
        #para, para_covarience = optimize.curve_fit(fit函數, x資料, y資料, p0=初始參數)
        para, para_covarience = optimize.curve_fit(self.fitfunction, xdata, ydata, p0=[0,0,0])
        self.threshold = [self.fitfunction(x,para[0],para[1],para[2]) for x in range(len(xdata))]
        if method == 0:
            for i, m in enumerate(ydata):
                if ydata[i]<self.threshold[i]:
                    self.ydata[i]=0
        elif method == 1:
            for i, m in enumerate(ydata):
                if ydata[i]>self.threshold[i]:
                    self.ydata[i]=1
        else:
            for i, m in enumerate(ydata):
                if ydata[i]>self.threshold[i]:
                    self.ydata[i]=self.threshold[i]
        
    def getThreshold(self):
        return self.threshold
    
    def getOutput(self):
        return self.ydata

class hfinder:
    hindex = []
    @classmethod
    def sumindex(cls, hindex):
        cls.hindex += hindex
        
    @classmethod
    def gethindex(cls):
        return cls.hindex
    
    def sampling(self,orilist,sl,si):
        '''
        用於以不同間距取樣原始資料陣列
        '''
        temp=[]
        for i in range(len(orilist)): #split a list with n slice length
            if (i+si)%sl==0 and i+si<len(orilist): #選擇取樣點
                temp.append(orilist[i])
        return temp
    
    def getlim(self,orilist,header):
        h = hfinder()
        hresult = h.findheader(orilist,header,1,0,0)
        notzero = []
        dist = []
        j = 0
        for i,j in enumerate(hresult[1]):
            if j!=0:
                notzero.append(i)
        for i in range(len(notzero)):
            if i>0:
                dist.append(notzero[i]-notzero[i-1])
        ndist = {s:0 for s in set(dist)}
        for s in dist:
            ndist[s]+=1
        for i in ndist.items():
            if i[1]>5:
                return i[0]
    
    def findheader(self,orilist,header,sl,si,error): # sl=取樣間隔, si=取樣起始點
        '''
        用於在list中搜尋一個連續的list
        '''
        self.difference = []
        self.density = []
        self.hindex = []
        
        for i in range(len(orilist)-1):
            if orilist[i]!=orilist[i+1]:
                self.difference.append(1)
            else:
                self.difference.append(0)
        for i in range(len(orilist)):
            if i<=len(orilist)-len(header)+1:
                self.density.append(sum(self.difference[i:i+len(header)-2]))
        for i,j in enumerate(self.density):
            if self.density[i]==max(self.density) and max(self.density)>5:
                self.hindex.append(i*sl+si)
        return [self.hindex, self.difference, self.density]









