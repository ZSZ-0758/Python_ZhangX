import sys
with open(sys.argv[1],'r') as f:
    read_data=f.read()
#读入json文件
    
Array={}
read_data=read_data.replace('[','')
read_data=read_data.replace(']','')
print(read_data)
my_list=list(read_data.split(","))
print(my_list)

for every in my_list:
    if every in Array.keys():
        Array[every]=Array[every]+1
    else:
        Array[every]=1
#统计每个字符出现次数，计入字典
print(Array)

m=0
for name1,times1 in Array.items():
    if times1>=m:
        m=times1
#计算字典中次数中的最大值 

maxlist=[]
for name2,times2 in Array.items():
    if times2==m:
        maxlist.append(name2)
#取出次数中的最大值

message=f"{maxlist}"[1:-1].replace(" ","")
message=message.replace("'",'')
with open("output.txt",'w') as p:
    p.write(message)