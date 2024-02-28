def output(obj):
    import json
    print(json.dumps(obj))
    
import sys
with open(sys.argv[1],'r',newline='') as f:
    read_lines=f.read()
read_lines=read_lines.replace('.','')
read_lines=read_lines.replace('?','')
read_lines=read_lines.replace('!','')
read_lines=read_lines.replace('\n',' ')
read_lines=read_lines.replace('\r','')
read_lines=read_lines.lower()
source=read_lines.split(' ')

result={}
for everyword in source:
    if everyword.isalpha()==True:
        if everyword in result:
            result[everyword]+=1
        else:
            result[everyword]=1
    else:
        continue

obj=result
output(obj)