import sys
with open(sys.argv[1],'r',encoding='utf-8',newline='') as f:
    read_lines=f.read()
print(read_lines)
result=[]
for everychar in read_lines:
    if ord(everychar)>=48 and ord(everychar)<=57:
        result.append(everychar)
    else:
        continue

n=len(result)
m=(int)(n/9)
p=0
#记录当前写入的位置
with open(sys.argv[2],'w') as f:
    for i in range(0,m):
        for j in range(0,3):
            for k in range(0,3):
                f.write(result[p])
                p+=1

            if j==2:
                break
            else:
                f.write("-")
        if i==m-1:
            break
        else:
            f.write("\n")