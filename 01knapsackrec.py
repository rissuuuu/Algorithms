def knapsack(w,wt,val,n):
    #base case
    if n==0 or w==0:
        return 0

    #if weight of the nth itm is more than knapsack of capacity
    #w, then this item cannot be included in the optimal solution
    if(wt[n-1]>w):
        return knapsack(w,wt,val,n-1)

    #return the maximum of two cases:
    # 1. nth item included
    # 2. not included
    else:
        return max(val[n-1]+knapsack((w-wt[n-1]),wt,val,n-1),knapsack(w,wt,val,n-1))

val=[1,2,5,6]
wt= [2,3,4,5]
w=8
n=len(val)
print(knapsack(w,wt,val,n))
