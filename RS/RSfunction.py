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
            if (i-si)%sl==0 and i-si>=0: #選擇取樣點
                temp.append(orilist[i])
        return temp
    
    def getlim(self,orilist,header):
        h = hfinder()
        hresult = h.findheader(orilist,header,1,0)
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
    
    def findheader(self,orilist,header,sl,si): # sl=取樣間隔, si=取樣起始點
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
                self.density.append(sum(self.difference[i:i+len(header)-1]))
        for i,j in enumerate(self.density):
            if self.density[i]>=max(self.density)-1 and max(self.density)>5:
                self.hindex.append(i*sl+si)
        if len(self.hindex)>1:
            for i in range(len(self.hindex)):
                self.hindex[i]+=1*sl
        return [self.hindex, self.difference, self.density]
        #[找到的header的起始index(以原始陣列為參考), 
        # 變換位置的index, 
        # 以後8項的變換頻率]
    
    def goodslsi(self,index):
        b = False
        for i in range(len(index)):
            if i>0 and abs(index[i]-index[i-1])>100:
                return (b or True)
            
    def selectindex(self,orilist,header,sl,si,length):
        h = hfinder()
        hresult = h.findheader(orilist,header,sl,si)
        index = hresult[0]
        sindex = []
        sumdensity = 0
        totaldensity = []
        for i in range(len(index)):
            for j in range(len(index)-1):
                for k in range(len(index)):
                    if i-j>=0 and ((index[i]-index[i-j])/sl-8)/(k+1)==length:
                        sindex.append((index[i], index[i-j], k+1))
                        #[header1的index, header2的index, samplerate]
        for i in range(len(sindex)):
            for j in range(len(sindex[i])):
                sumdensity += hresult[2][int((sindex[i][j]-si)/sl-1)]
            totaldensity.append(sumdensity)
            sumdensity = 0
        for i in range(len(totaldensity)):
            if totaldensity[i]==max(totaldensity):
                print('totaldensity = '+str(totaldensity))
                return [sindex[i],sindex,i,totaldensity]
                #[總和變換頻率最高的headerindex, 
                # 長度符合的headerindex, 
                # 總和變換頻率最高的index, 
                # 長度符合的headerindex各自之總和變換頻率]







