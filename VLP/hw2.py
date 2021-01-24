# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:39:38 2021

@author: DengCheng
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


path = 'D:\Data\hw2_VLP\Condition_lamp off_raw-data_t.xlsx'
d = pd.read_excel(path)
d = d.drop([0], axis=0)
d = d.sort_values(by=['座標點(cm)', 'Unnamed: 3'])

p = d.iloc[0:,2:4]
p_sort = p.drop_duplicates()
t = d.iloc[0:,2:4]
#t = np.zeros((1,2))
phi = np.zeros((1,10))
for i in d.values:
    #t = np.append(t, [i[2:4]], axis=0)
    phi = np.append(phi, np.array([[1, i[7], i[8], i[9], i[7]*i[8], i[8]*i[9], i[7]*i[9], i[7]*i[7], i[8]*i[8], i[9]*i[9]]]), axis=0)
#t = np.delete(t, 0, 0)
phi = np.delete(phi, 0, 0)


Wml = np.linalg.inv(phi.T@phi)@phi.T@t # 也可寫成np.transpose(phi)
f = phi@Wml

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)
ax.grid(True)
ax.axis([-10,60,-10,50])
scat1 = ax.scatter(p_sort.iloc[:,0], p_sort.iloc[:,1],color='b')
scat2 = ax.scatter(p_sort.iloc[:,0], p_sort.iloc[:,1],color='',marker='o',edgecolor='green',s=1000)
#scat = ax.scatter(f.iloc[:,0], f.iloc[:,1],color='',marker='o',edgecolor='green',s=1000)

delta_r = (ax.transData.transform(f.astype('float64'))-ax.transData.transform(p.astype('float64')))
r = np.sqrt(np.sum(delta_r**2, axis=1))
size_pt = (2*r/fig.dpi*72)**2
scat2.set_sizes(size_pt)

plt.savefig('D:\Data\hw2_VLP\output.png',dpi=300,format="png")

plt.show()
