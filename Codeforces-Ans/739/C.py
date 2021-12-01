import math
T = int(input())
for _ in range(T):
    k = int(input())
    ans = math.ceil(math.sqrt(k))
    res = int(math.sqrt(k))
    res *= res
    if k-res == 0: print(ans,1)
    elif k-res <= ans: print(k-res,ans)
    else:
        a = ans*ans
        print(ans,a-k+1)

    
