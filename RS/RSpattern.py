# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:02:08 2020

@author: dengcheng
"""
from RSfunction import*# fit, sampling,findheader
import matplotlib.pyplot as plt
'''
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
height = 480 #height, nf, colmatrix都可刪
nf = 0
colmatrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]


#進行fitting與篩選
colmatrix_0 = fit()
colmatrix_0.thresholding(list(range(height)),colmatrix[nf],2)
colmatrix_1 = fit()
colmatrix_1.thresholding(list(range(height)),colmatrix_0.getOutput(),0)
colmatrix_2 = fit()
colmatrix_2.thresholding(list(range(height)),colmatrix_1.getOutput(),1)

plt.figure() # <Figure size 432x288 with 0 Axes>
#plt.plot(range(height),colmatrix[nf],lw=0.3) #原本的值
#plt.plot(range(height),colmatrix_0.getThreshold(),lw=0.3) #第一次fitting
#plt.plot(range(height),colmatrix_0.getOutput(),lw=0.3) #第一次篩選後
#plt.plot(range(height),colmatrix_1.getThreshold(),lw=0.3) #第二次fitting
#plt.plot(range(height),colmatrix_1.getOutput(),lw=0.3) #第二次篩選後
#plt.plot(range(height),colmatrix_2.getThreshold(),lw=0.3) #第三次fitting
#plt.plot(range(height),colmatrix_2.getOutput(),lw=0.3) #第三次篩選後
print('93->120: ' + str(colmatrix_2.getOutput()[93:120]))
print('320->347: ' + str(colmatrix_2.getOutput()[320:347]))


import scipy.io as sio
matp = u"D:/Data/RSvideo/newrolling.mat"
matfile=sio.loadmat(matp)
T = matfile["T"][0] #len 78
T1 = matfile["T1"][0] #len 35

'''
for i in range(len(T)):
    samwithT = samlist = sampling(orilist, len(T), i)
    fhresult = findheader(samwithT, header, len(T), i)
for i in range(len(T1)):
    samwithT1 = samlist = sampling(orilist, len(T1), i)
    fhresult = findheader(samwithT1, header, len(T1), i)
'''


#尋找各種sample rate下的header
orilist = colmatrix_2.getOutput() #想找header的list
header = [1,0,1,0,1,0,1,0] #想要找到的header

#找到samplerate最小參考值
h = hfinder()
findrange = h.getlim(orilist, header) #縮小查找範圍用的參數
print('limt = ' + str(h.getlim(orilist, header)))

#判斷header的index
for sl in [sl+1 for sl in range(findrange)]:
    for si in [sl for sl in range(findrange)]:
        if si<sl:
            h = hfinder()
            samlist = h.sampling(orilist, sl, si)
            fhresult = h.findheader(samlist, header, sl, si, 0.1)
            h.sumindex(fhresult[0])
            print('header index: ' + str(fhresult[0]) + ', ' + str(sl) + '-' + str(si) + '\n')
hindex = sorted(h.gethindex())
nhindex = {s:0 for s in set(hindex)}

#顯示各個headerindex出現的數量
for s in hindex:
    nhindex[s]+=1
'''
#刪除只出現過一次的
for i in nhindex.items():
    if i[1]<2:
        del nhindex[i[0]]
'''
        
print('Finished.' + str(nhindex))


print('\nT = ' + str(T))
print('len(T) = ' + str(len(T))+'\n')
print('T1 = ' + str(T1))
print('len(T1) = ' + str(len(T1)))


'''
#plt.xlim(0,5)
#plt.ylim(-1,5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")
#plt.savefig("filename.png",dpi=300,format="png")
plt.show()
'''




