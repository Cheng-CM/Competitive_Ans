T = int(input())
for t in range(T):
    cnt = 0
    n = int(input())
    arr = list(map(int,input().split(" ")))
    for i in range(4,n,4):
        piano = arr[i-4:i]
        if max(piano) == piano[-1] and arr[i] > piano[-1] or min(piano) == piano[-1] and arr[i] < piano[-1]:
            cnt += 1
    print("Case #"+ str(t+1) +":",str(cnt),flush=True)