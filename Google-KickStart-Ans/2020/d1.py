T = int(input())
for t in range(T):
    cnt = 0
    n = int(input())
    arr = list(map(int,input().split(" ")))
    m = float("-inf")
    for i in range(n):
        if arr[i] > m:
            if i != n-1 and arr[i] > arr[i+1]:
                cnt += 1
            elif i == n-1:
                cnt += 1
        m = max(m,arr[i])
    print("Case #"+ str(t+1) +":",str(cnt),flush=True)