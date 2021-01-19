import pandas as pd

path = 'D:\Data\interpolation\ITRI0827'

data = []
for filen in range(33):
        filepath = path+'\\'+str(filen*4)+'.xlsx'
        d = pd.read_excel(filepath)
        data.append(d)
        print(filepath + ' is readed.')

for i in [k+1 for k in range(32)]:
    datas = (data[2*i-2].values + data[2*i-1].values)/2
    indexs = data[0].index
    columns = data[0].columns
    dnew = pd.DataFrame(datas, columns=columns, index=indexs)
    data.insert(i,dnew)
