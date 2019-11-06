def coin_change(coins, N):
    M = len(coins)  # number of coins
    Num = [[float('inf') for _ in range(N + 1)] for i in range(M + 1)]
    for m in range(M + 1):
        for n in range(N + 1):
            if m == 0 or n == 0:
                continue
            if n == coins[m - 1]:
                Num[m][n] = 1
            if coins[m - 1] <= n:
                Num[m][n] = min(Num[m][n], Num[m - 1][n], Num[m][n - coins[m - 1]] + 1)
            else:
                Num[m][n] = Num[m - 1][n]

    return -1 if Num[M][N] == float('inf') else Num[m][n]


a=[1,2,4,5,10]
n=28
print(coin_change(a,n))