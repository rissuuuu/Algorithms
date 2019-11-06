def knapsack(w,wt,val,n):
    k=[[0 for x in range(w+1)]for x in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                print("if",i,j )
                k[i][j]=0
                print("__________")
            elif wt[i-1]<=j:
                print("elif")
                print("before",(i,j),k[i][j])
                k[i][j]=max(val[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
                print("after ",(i, j), k[i][j])
                print("__________")
            else:
                print("else")
                print("before", (i, j), k[i][j])
                k[i][j]=k[i-1][j]
                print("after ", (i, j), k[i][j])
                print("__________")

    return k[n][w]

val=[100,200,300,400]
wt=[2,3,4,5]
w=8
n=len(val)
print(knapsack(w,wt,val,n))