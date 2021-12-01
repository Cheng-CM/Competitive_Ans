T = int(input())
for t in range(T):
    n = int(input())
    dp = [[float('inf') for _ in range(4)] for i in range(n)]
    arr = list(map(int,input().split(" ")))
    for i in range(4):
        dp[0][i] = 0
    
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            for j in range(4):
                for k in range(4):
                    dp[i][j] = min(dp[i][j],dp[i-1][k] + (0 if j > k else 1))
        elif arr[i] < arr[i-1]:
            for j in range(4):
                for k in range(4):
                    dp[i][j] = min(dp[i][j],dp[i-1][k] + (0 if j < k else 1))
        else:
            for j in range(4):
                    dp[i][j] = min(dp[i][j],dp[i-1][j])
            for j in range(4):
                for k in range(4):
                    if j != k:
                        dp[i][j] = min(dp[i][j],dp[i-1][k] + 1)
    for x in dp:
        print(*x, sep=" ")
    ans = float('inf')
    for i in range(4):
        ans = min(ans,dp[n-1][i])
    print("Case #"+ str(t+1) +":",str(ans),flush=True)