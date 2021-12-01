T = int(input())
for t in range(T):
    cnt = 0
    n = int(input())
    arr = list(map(int,input().split(" ")))
    curr = arr[0] - arr[1]
    ans = 0
    temp = 1
    for i in range(1,n-1):
        if curr == arr[i] - arr[i+1]:
            temp += 1
        else:
            ans = max(ans,temp+1) 
            temp = 1
            curr = arr[i] - arr[i+1]
    ans = max(ans,temp+1)
    print("Case #"+ str(t+1) +":",str(ans),flush=True)