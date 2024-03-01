import sys
a=int(sys.argv[1])
b=int(sys.argv[2])+1
num_list=[]
#记录区间内素数
num=0
#记录区间内素数个数
key=True
#判断是否为素数
for value in range(a,b):
    if value==1:
        continue
    else:
        for every in range(1,value):
            if every ==1:
                continue
            else:
                if (value % every)==0:
                    key=False
                else:
                    continue
        if key==True:
            num+=1
            num_list.append(value)
        else:
            key=True
with open("output.txt","w") as p:
    p.write(f"{num}")
    p.write("\n")
    message=f"{num_list}".replace(" ","")
    p.write(message[1:-1])
p.close()