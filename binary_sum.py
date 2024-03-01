import sys
number_char=sys.argv[1:]
number=[]
for every in number_char:
    every=int(every)
    i=0
    temp=0
    while i<13:
        i=i+1
        if every//(10**(13-i))==1:
            temp=temp+2**(13-i)
        every=every%(10**(13-i))
    number.append(temp)
result=0
for every_num in number:
    result=result+every_num
print(bin(result)[2:])