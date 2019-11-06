def fractionalknapsack(p,w,ratio,size):
    print(p,w,ratio,size)
    p1,w1,ratio1=p,w,ratio
    sum=0
    while(size>0):
        i=ratio1.index(max(ratio1));
        if w[i]<=size:
            sum=sum+p1[i]
            size=size-w1[i]
            ratio1.pop(i)
            w1.pop(i)
            p1.pop(i)
        else:
            sum=sum+size*ratio1[i]
            size=0
    print(sum)

size=int(input("Enter total size"));
n=int(input("Enter no of items"));
p=[int(input("Enter profits")) for i in range(n)]
w=[int(input("Enter Weights"))for i in range(n)]
ratio=[p[i]/w[i] for i in range(n)]
fractionalknapsack(p,w,ratio,size)