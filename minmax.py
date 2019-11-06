a=[1,3,9,5,7]
c=[]
b=[]
sum=[]
min_sum=[]

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            break
        b.append([a[i],a[j]])

d=b[::-1]
for i,j in zip(b,d):
        if(i[0]!=j[1] or i[1]!=j[0]):
            c.append([i,j])
            b.remove(i)
            d.remove(j)

maximum=0
print("Disjoint set",c)

for i in c:
    maximum=max(i[0],i[1])
    sum.append(maximum)

print("Maximum subsets are",sum)
#print("Given set",a)
#print("Disjoint set",c)


minimum=min(sum)
min_sum.append(minimum)
for i in min_sum:
    print(i[0]+i[1],"is the minimum ")




