A = [1, 2,19, 5, -7, 8,9, 3]
print("Main List->",A)
B=[]
C=[]
for i in A:
    if(i<0):
        break
    B.append(i)
for i in A:
    if(i<0):
        continue
    if i not in B:
        C.append(i)
print("1st half before negative numner->",B)
print("2nd half after negative number->",C)
sum1=0
sum2=0
for i in B:
    sum1=sum1+i
for i in C:
    sum2=sum2+i;
print(sum1," and ",sum2)
if(sum1>sum2):
    print(B,"is maximum and superior")
else:
    print(C,"is maximum and Superior")