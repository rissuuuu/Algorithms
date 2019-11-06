def Mode(array,length):
    a=[]
    b=[]
    for i in array:
        count=array.count(i)
        a.append(i)
        b.append(count)
    return a,b

a=[1,1,2,4,5,4,6,3,4,6,6,2,3,4,6,7,5]
c,d=Mode(a,len(a))
lists=c
b=d
print(lists)
print(d)

maximum=max(d)
aa=[]
bb=[]

for i,j in zip(lists,b):
    if(maximum==j):
        aa.append([i,j])
print(aa)

for i in aa:
     if i not in bb:
         bb.append(i)

print(bb)

for i in bb:
    print(i[0], "is mode")