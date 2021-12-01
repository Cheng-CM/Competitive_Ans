T = int(input())
for t in range(T):
    n = int(input())
    s = list(input())
    poss = [chr(c) for c in range(ord('a'),ord('z')+1)]
    curr = set(c for c in s)
    found = 0
    j = 2
    while not found:
        for c in poss:
            if c not in curr:
                print(c)
                found = 1
                break
        if found: break
        poss = [chr(c)+p for c in range(ord('a'),ord('z')+1) for p in poss]
        curr = set(["".join(s[i:i+j]) for i in range(n-j+1)])
        j += 1


