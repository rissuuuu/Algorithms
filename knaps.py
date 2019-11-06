def knapsack(w,val,wt,n):
    k=[[0 for i in range(wt+1)]for j in range(n+1)]


    for i in range(n+1):
        for j in range(wt+1):
            if(i==0 or j==0):
                k[i][j]=0

            elif(w[i-1]<=j):
                k[i][j]=max(val[i-1]+k[i-1][j-w[i-1]],k[i-1][j])
            else:
                k[i][j]=k[i-1][j]

    print(k[n][wt])






w=[1,2,5,6]
val=[2,3,4,5]
n=len(w)
wt=8
knapsack(w,val,wt,n)