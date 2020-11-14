# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:02:08 2020

@author: dengcheng
"""
from RSfunction import fit, sampling,findheader
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
plt.plot(range(height),colmatrix_2.getOutput(),lw=0.3) #第三次篩選後

#print(colmatrix_2.getOutput())

#尋找各種sample rate下的header
orilist = colmatrix_2.getOutput() #想找header的list
header = [1,0,1,0,1,0,1,0] #想要找到的header
findrange = int(len(orilist)/40) #縮小查找範圍用的參數

for sl in [sl+1 for sl in range(findrange)]:
    for si in [sl for sl in range(findrange)]:
        if si<sl:
            samlist = sampling(orilist, sl, si)
            fhresult = findheader(samlist, header, sl, si)
            headerindex = fhresult[0]
            array_at_some_samplerate = fhresult[1]
            #if headerindex!=[]:
                #print('\nheaderindex = ' + str(headerindex) + ', slice length = ' + str(fhresult[2]) + ', start position = ' + str(fhresult[3]))
                #print('Number of datapoints =' + str(len(array_at_some_samplerate))) #特定取樣率下的陣列大小
                #print('slice length = ' + str(fhresult[2])) #取樣的間距
                #print('start position = ' + str(fhresult[3])) #起始取值點
                #print('SignalArray at your sample rate =\n' + str(array_at_some_samplerate) + '\n')

print('Finished. findrange = ' + str(findrange))

'''
#plt.xlim(0,5)
#plt.ylim(-1,5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")
#plt.savefig("filename.png",dpi=300,format="png")
plt.show()
'''
