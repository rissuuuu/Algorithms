def subset(A,n):
    elements=[]
    sum=0
    print(A)

    for i in range(len(A)):
            for j in range(len(A)):
                if((A[i],A[j]) or (A[j],A[i]) not in elements):
                    elements.append((A[i],A[j]))


    print(sum)
    print(elements)

A=[1,2,3]
subset(A,13)