def BubbleSort(A):
    n=len(A)


    for i in range(n):
        for j in range(0,n-i-1):
            if(A[j]>A[j+1]):
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp

    print(A)

A=[12,32,54,11,23,65,14,16]
BubbleSort(A)
for i in A:
    print(i)