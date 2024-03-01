import sys
import csv
import json
with open(sys.argv[1],'r') as jsonf:
    source=json.load(jsonf)
source=dict(sorted(source.items()))
#source原文件字典
scorelist=sorted(source.values(),reverse=True)
#scorelist成绩的数字排列列表
namelist=[]
#namelist成绩的名字排列列表
n=ord(sys.argv[2])-48
for i in range(0,n):
    for name,score in source.items():
        if score==int(scorelist[i]):
            namelist.append(name)
            del(source[name])
            break
        else:
            continue
#以成绩取名字排序
with open('output.csv','w',newline='') as csvf:
    writelist=csv.writer(csvf)
    writelist.writerow(namelist)
#将名字列表写入csv