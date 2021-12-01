T = int(input())
for t in range(T):
    n,k,s = list(map(int,input().split(" ")))
    fc = k + (k - s) + (n - s)
    sc = k + n
    print("Case #"+ str(t+1) +":",str(min(fc,sc)),flush=True)