T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        s = str(input())
        s = s.split(" ")
        arr.append(list(map(int,s)))
    ans = 0
    for i in range(0,n):
        temp = 0
        for j in range(0,n-i):
            temp += arr[j][j+i]
        ans = max(ans,temp)
    for i in range(1,n):
        temp = 0
        for j in range(0,n-i):
            temp += arr[j+i][j]
        ans = max(ans,temp)
    print("Case #"+ str(t+1) +":",str(ans),flush=True)