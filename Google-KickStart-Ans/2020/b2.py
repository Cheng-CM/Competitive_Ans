T = int(input())
for t in range(T):
    n,d = input().split(" ")
    n,d = int(n),int(d)
    arr = list(map(int,input().split(" ")))
    for i in range(n-1,-1,-1):
        if i < n-1:
            arr[i] = arr[i] * (arr[i+1]//arr[i])
        else:
            arr[i] *= d // arr[i]
    print("Case #"+ str(t+1) +":",str(min(arr)),flush=True)