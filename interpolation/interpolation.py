import pandas as pd

path = 'D:\Data\interpolation\ITRI0827'

data = []
# 讀取0,4,6,10,12,16,20,22,26,28,32,34,38,42
for turn in range(2):
    for base in [0,4,6,10,12,16,20]:
        i = base + turn*22
        filepath = path+'\\'+str(i)+'.xlsx'
        d = pd.read_excel(filepath)
        data.append(d)
        print(filepath + ' is readed.')
# 讀取44,48,50,54,55,59,61,65,66,70,72,76,77,81,83,87
for turn in range(4):
    for base in [44,48,50,54]:
        i = base + turn*11
        filepath = path+'\\'+str(i)+'.xlsx'
        d = pd.read_excel(filepath)
        data.append(d)
        print(filepath + ' is readed.')
# 讀取89,93,97,99,103,105,109,111,115,119,121,125,127,131
for turn in range(2):
    for base in [89,93,97,99,103,105,109]:
        i = base + turn*22
        filepath = path+'\\'+str(i)+'.xlsx'
        d = pd.read_excel(filepath)
        data.append(d)
        print(filepath + ' is readed.')
#---------------------------------------------------------------
# 內插出2,8,14,18,24,30,36,40
for turn in range(2):
    for base in [1,4,7,9]:
        j = base + turn*11
        filepath = path+'\\'+str(j*2)+'.xlsx'
        datas = (data[j-1].values**2 + data[j].values**2)/2
        indexs = data[j].index
        columns = data[j].columns
        dnew = pd.DataFrame(datas, columns=columns, index=indexs)
        data.insert(j,dnew)
        dnew.to_excel(filepath)
        print(filepath + ' is done.')
# 內插出46,52,57,63,68,74,79,85
for turn in range(4):
    for base in [23,26]:
        j = base + turn*6
        filepath = path+'\\'+str(j*2-turn)+'.xlsx'
        datas = (data[j-1].values**2 + data[j].values**2)/2
        indexs = data[j].index
        columns = data[j].columns
        dnew = pd.DataFrame(datas, columns=columns, index=indexs)
        data.insert(j,dnew)
        dnew.to_excel(filepath)
        print(filepath + ' is done.')
# 內插出91,95,101,107,113,117,123,129
for turn in range(2):
    for base in [47,49,52,55]:
        j = base + turn*11
        filepath = path+'\\'+str(j*2-3)+'.xlsx'
        datas = (data[j-1].values**2 + data[j].values**2)/2
        indexs = data[j].index
        columns = data[j].columns
        dnew = pd.DataFrame(datas, columns=columns, index=indexs)
        data.insert(j,dnew)
        dnew.to_excel(filepath)
        print(filepath + ' is done.')
