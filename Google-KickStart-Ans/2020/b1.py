T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    count = 0
    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1
    print("Case #"+ str(t+1) +":",str(count),flush=True)