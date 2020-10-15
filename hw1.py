# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:27:47 2020

@author: dengcheng
"""
import math

with open("assn1_input.txt", "r", encoding = 'cp950') as f:
    numlist=[]
    slist=[]
    for line in f:
        line = line.strip('\n')
        for s in line.split("%"):
            if s.isdigit():
                numlist.append(int(s))
            else:
                if s=="zerba":
                    s="zebra"
                slist.append(s) #put statements in "else:" into for loop if the requirements of homework is to write all correct contents(containing numbers) out to the file "fixed.out"

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
fanimals.write("%.2e" %(math.log(sum(numlist))) + "\n") # the sum of numbers, result: 1.57e+01
fanimals.write(str(numani) + "\n") # the numer of each kind of animals, result: {'dog': 3736, 'zebra': 7779, 'tiger': 6815, 'monkey': 8323}
fanimals.write(str(allani)) # the numer of animals, result: {'total_count': 26653}
fanimals.close()

ffixed = open("fixed.out", "w")
ffixed.write(str(slist)+"\n")
ffixed.close()
