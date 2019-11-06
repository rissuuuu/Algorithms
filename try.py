a=[[2,4,1,5,7,3,5,11,17,8],[5,4,2,3,5,6,2,1,9,10]]

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)-i-1):
            if(a[j][k]>a[j][k+1]):
                a[j][k],a[j][k+1]=a[j][k+1],a[j][k]


print(a)



