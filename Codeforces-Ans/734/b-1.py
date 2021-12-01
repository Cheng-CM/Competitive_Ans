from collections import Counter
T = int(input())
for _ in range(T):
    s = input()
    c = Counter(s)
    r,g = 0,0
    for i in c:
        if c[i] >= 2:
            r,g = r+1,g+1
        elif r > g:
            g += 1
        else:
            r += 1
    print(min(r,g))