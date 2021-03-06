# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:02:08 2020

@author: dengcheng
"""
from RSfunction import*# fit, hfinder, calerror
import matplotlib.pyplot as plt

import cv2
capture = cv2.VideoCapture("D:\Data\RSvideo\RSvideo.mp4")

fps = capture.get(cv2.CAP_PROP_FPS) #30.0
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) #480
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) #640
fNUMS = int(capture.get(cv2.CAP_PROP_FRAME_COUNT)) #1163

temp=list(range(height))
colmatrix=[]
ret = True
if capture.isOpened():
    while ret:
        ret, frame = capture.read() #讀取完影片時，ret變更為False
        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray.sort()
            for i in range(height):
                temp[i]=gray[i][127]
        colmatrix.append(tuple(temp))
capture.release()
#del fNUMS, fps, frame, gray, height, width
del temp, ret, i

nf = 0 #幀數
colmatrix[nf] = list(colmatrix[nf])#把第x幀的colmatrix變成list
'''
#方便測試
height = 480 #height, nf, colmatrix都可刪
nf = 0
#nf = 0
colmatrix = [[31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 30, 30, 30, 26, 22, 13, 9, 2, 0, 1, 2, 8, 12, 20, 26, 30, 31, 32, 33, 33, 29, 20, 17, 13, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 9, 18, 25, 23, 23, 18, 9, 5, 4, 2, 3, 9, 13, 22, 33, 34, 34, 34, 34, 34, 32, 26, 18, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 8, 15, 16, 15, 10, 6, 8, 13, 22, 18, 6, 4, 11, 16, 18, 16, 8, 6, 16, 18, 22, 22, 23, 22, 22, 20, 18, 14, 10, 0, 0, 0, 0, 0, 0, 0, 0, 5, 16, 19, 24, 36, 43, 43, 43, 43, 43, 41, 41, 41, 41, 41, 40, 37, 31, 23, 15, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 17, 31, 37, 40, 40, 40, 41, 41, 41, 41, 43, 43, 41, 38, 34, 29, 24, 12, 6, 0, 0, 4, 13, 16, 27, 34, 33, 29, 19, 11, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 26, 31, 31, 30, 20, 11, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 15, 23, 29, 36, 40, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 44, 43, 36, 30, 26, 17, 10, 4, 5, 3, 9, 13, 18, 24, 35, 43, 42, 42, 42, 42, 36, 29, 16, 13, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2, 12, 25, 23, 26, 25, 20, 16, 10, 2, 0, 0, 4, 15, 23, 25, 33, 40, 39, 37, 40, 37, 30, 23, 18, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 10, 19, 19, 10, 6, 6, 15, 18, 18, 10, 8, 8, 11, 16, 15, 10, 6, 9, 15, 17, 18, 19, 20, 23, 23, 18, 10, 8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 15, 20, 24, 26, 31, 34, 36, 36, 36, 36, 34, 34, 33, 34, 32, 26, 17, 11, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 19, 22, 26, 30, 31, 31, 31, 31, 31, 31, 31, 31, 30, 27, 20, 18, 12, 8, 0, 0, 0, 0, 9, 15, 13, 13, 13, 13, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 11, 16, 15, 12, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 12, 16, 24, 25, 25, 26, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 25, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 21, 12, 9]]
#nf = 5
#colmatrix = [[8, 10, 12, 12, 11, 11, 8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 11, 16, 24, 26, 29, 31, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 31, 31, 31, 31, 31, 31, 30, 31, 29, 23, 16, 10, 4, 1, 1, 2, 5, 11, 18, 25, 30, 31, 32, 32, 32, 30, 23, 18, 15, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8, 13, 24, 24, 24, 20, 11, 6, 5, 2, 3, 6, 12, 18, 30, 33, 34, 33, 33, 33, 33, 29, 22, 16, 11, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 6, 12, 16, 16, 15, 9, 8, 11, 17, 19, 12, 4, 10, 13, 17, 18, 11, 6, 11, 18, 20, 22, 23, 23, 23, 22, 20, 16, 12, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 16, 19, 29, 37, 42, 42, 42, 42, 42, 41, 41, 41, 41, 40, 38, 33, 25, 17, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 12, 24, 34, 38, 40, 40, 40, 40, 40, 40, 42, 42, 40, 38, 33, 30, 24, 17, 9, 1, 0, 3, 10, 14, 20, 31, 32, 29, 19, 15, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 20, 30, 31, 30, 23, 11, 8, 3, 0, 0, 0, 0, 0, 0, 0, 0, 9, 20, 27, 31, 36, 39, 41, 41, 41, 41, 41, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 38, 32, 29, 24, 17, 10, 4, 4, 3, 6, 12, 16, 20, 32, 40, 40, 39, 39, 38, 33, 27, 16, 12, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 23, 23, 24, 24, 20, 15, 10, 2, 0, 0, 3, 11, 17, 23, 30, 38, 38, 36, 37, 37, 29, 22, 16, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 8, 17, 19, 11, 5, 6, 11, 16, 15, 11, 6, 5, 8, 13, 15, 11, 5, 7, 11, 15, 17, 18, 19, 22, 20, 17, 10, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 17, 22, 24, 26, 31, 32, 32, 32, 32, 32, 31, 31, 31, 29, 23, 17, 11, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 15, 19, 23, 25, 26, 27, 28, 29, 30, 30, 29, 29, 29, 25, 22, 16, 12, 8, 0, 0, 0, 0, 8, 11, 13, 13, 12, 12, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 10, 13, 13, 13, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 12, 18, 23, 24, 24, 24, 24, 24]]
'''

#進行fitting與篩選
colmatrix_0 = fit()
colmatrix_0.thresholding(list(range(height)),colmatrix[nf],2)
colmatrix_1 = fit()
colmatrix_1.thresholding(list(range(height)),colmatrix_0.getOutput(),0)
colmatrix_2 = fit()
colmatrix_2.thresholding(list(range(height)),colmatrix_1.getOutput(),1)

#畫圖
#plt.figure() # <Figure size 432x288 with 0 Axes>
#plt.plot(range(height),colmatrix_0.getInput(),lw=0.3) #原本的值
#plt.plot(range(height),colmatrix_0.getThreshold(),lw=0.3) #第一次fitting
#plt.plot(range(height),colmatrix_0.getOutput(),lw=0.3) #第一次篩選後
#plt.plot(range(height),colmatrix_1.getThreshold(),lw=0.3) #第二次fitting
#plt.plot(range(height),colmatrix_1.getOutput(),lw=0.3) #第二次篩選後
#plt.plot(range(height),colmatrix_2.getThreshold(),lw=0.3) #第三次fitting
#plt.plot(range(height),colmatrix_2.getOutput(),lw=0.3) #第三次篩選後
#plt.xlim(0,5)
#plt.ylim(-1,5)
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.title("The Title")
#plt.savefig("filename.png",dpi=300,format="png")


#尋找各種sample rate下的header
orilist = colmatrix_2.getOutput() #想找header的list

print(orilist)


sumlist = getSum(orilist)
header = getHeader(sumlist)
numlist = getnumList(sumlist,header)
checknumlist(sumlist,numlist,header)
payload = ToPayload(numlist)
#print(sumlist)
#print(header)
#print(numlist)


#讀取T和T1
import scipy.io as sio
matp = u"D:/Data/RSvideo/newrolling.mat"
matfile=sio.loadmat(matp)
print('---------------' + str(type(matfile["T"][0])))
T = matfile["T"][0] #len 78
T1 = matfile["T1"][0] #len 35

print('\nT (len='+str(len(T))+') = ' + str(T))
print('T1(len='+str(len(T1))+') = ' + str(T1))
print()

print('sumlist' + str(sumlist))
print('header' + str(header))
print(payload[1])
print(str(list(T1)))
print(calerror(payload[1],list(T1)))




