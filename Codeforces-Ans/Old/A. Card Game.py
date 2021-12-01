T = int(input())
for t in range(T):
    n,f,s = input().split(" ")
    n,f,s = int(n), int(f), int(s)
    fc = input().split(" ")
    fc = list(map(int,fc))
    sc = input().split(" ")
    sc = list(map(int,sc))
    print("YES" if max(fc)> max(sc) else "NO")