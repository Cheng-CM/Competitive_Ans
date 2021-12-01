T = int(input())
for t in range(T):
    n,k = list(map(int,input().split(" ")))
    s = input()
    limit = [ord(c)-ord('a')+1 for c in s]
    if n != 1:
        if len(limit) % 2 == 0:
            limit = limit[:len(limit)//2]
        else:
            limit = limit[:len(limit)//2+1]
        ans = 0
        for i in range(len(limit)):
            if i < len(limit)-1:
                if limit[i] > 1:
                    ans += (limit[i]-1) * k 
            else:
                if limit[i] != 1:
                    ans += limit[i]
    else:
        ans = limit[-1]-1
    print("Case #"+ str(t+1) +":",str(ans),flush=True)