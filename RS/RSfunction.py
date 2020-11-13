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


def findheader(orilist,want_to_find,n,start): # n=取樣間隔, start=取樣起始點
    '''
    用於在list中搜尋一個連續的list
    '''
    headerindex=[]
    temp=[]
    for i in range(len(orilist)): #split a list with n slice length
        if (i+start)%n==0 and i+start<len(orilist): #選擇取樣點
            temp.append(orilist[i+start])    
    for i in range(len(temp)): # 找header
        if i<=len(temp)-8 and temp[i:i+8]==want_to_find:
            headerindex.append(i)
            print('--> Find header, index = ' + str(i) + ', slice length = ' + str(n) + ', start position = ' + str(start))
    return [headerindex,temp,n,start]




