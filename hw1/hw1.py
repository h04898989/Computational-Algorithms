# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:27:47 2020

@author: dengcheng
"""
import math

with open("assn1_input.txt", "r", encoding = 'cp950') as f:
    numlist=[]
    slist=[]
    temp=[]
    fixed=[]
    for line in f:
        line = line.strip('\n')
        for s in line.split("%"):
            if s.isdigit():
                numlist.append(int(s))
            else:
                if s=="zerba":
                    s="zebra"
                slist.append(s)
            temp.append(s)
        fixed.append("%".join(temp) + "\n")
        temp=[]

numlist.sort(reverse=True) #Need transfer the String to int before sorting.
#print(set(slist)) #Show kinds of objects in file
#{'dog', 'zebra', 'tiger', 'corn', 'zerba', 'monkey', 'carrot', 'tomato'}

sset = set(slist)
numani = {s:0 for s in sset}
for s in slist:
    numani[s]+=1
    
del numani["corn"]
del numani["carrot"]
del numani["tomato"]

allani = {"total_count":sum(numani.values())}

fanimals = open("animals.out", "w")
fanimals.write(str(numlist) + "\n") # the list of numbers
fanimals.write("%.2e" %(math.log(sum(numlist))) + "\n") # the sum of numbers
fanimals.write(str(numani) + "\n") # the numer of each kind of animals
fanimals.write(str(allani)) # the numer of animals
fanimals.close()

ffixed = open("fixed.out", "w")
ffixed.writelines(fixed)
ffixed.close()
