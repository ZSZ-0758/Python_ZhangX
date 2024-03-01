import sys
with open(sys.argv[1],'r') as f:
    read_data=f.read()
#读入input字符串
    
string=[]
for every in read_data:
    if (ord(every)>=65 and ord(every)<=90)\
    or (ord(every)>=97 and ord(every)<=122):
        string.append(every.lower())
    else:
        continue
check_message=string[:]
string.reverse()
#获取纯小写字母以及回文

output_str={}
temp_str=f"{check_message}".replace("[","")
temp_str=temp_str.replace("]","")
temp_str=temp_str.replace(",","")
temp_str=temp_str.replace("'","")
temp_str=temp_str.replace(" ","")
if check_message==string:
    output_str["palindrome"]='true'
else:
    output_str["palindrome"]='false'
output_str["result"]=temp_str
#结果存入字典
with open("output.json","w") as p:
    p.write(f"{output_str}".replace("'",'"'))
