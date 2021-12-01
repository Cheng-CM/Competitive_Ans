T = int(input())
for t in range(T):
    n,k = list(map(int,input().split(" ")))
    s = input()
    score = sum(s[i] != s[-i-1] for i in range(n//2))
    score = abs(k - score)
    print("Case #"+ str(t+1) +":",str(score),flush=True)