import random
def disjoints(array1,array2):
    flag=0
    for i in array1:
        for j in array2:
            if(i==j):
                print(i,j)
                flag=1

    if (flag == 1):
        return 1
    else:
        return 0
array1=[]
array2=[]
for i in range(0,100):
    array1.append(random.randint(1,99))
    array2.append(random.randint(100,200))
val=disjoints(array1,array2)
if(val==1):
    print("The sets are not disjoint")
else:
    print("The sets are disjoint")