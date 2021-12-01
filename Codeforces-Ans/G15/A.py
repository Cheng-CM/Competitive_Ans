T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    ss = sorted(s)
    for i,j in zip(s,ss):
        if i == j:
            n -= 1
    print(n)