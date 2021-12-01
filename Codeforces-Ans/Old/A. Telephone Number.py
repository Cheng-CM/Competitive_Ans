T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    for i,val in enumerate(s):
        if val == "8" and len(s)-i >= 11:
            print("YES")
            break
        if len(s)-i < 11:
            print("NO")
            break