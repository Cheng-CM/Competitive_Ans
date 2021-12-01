T = int(input())
for _ in range(T):
    s = input()
    t = input()
    n,m = len(s),len(t)
    start = [i for i,v in enumerate(s) if v == t[0]]
    if start == -1:
        print('NO')
    else:
        flag = 0
        for i in start:
            j,k = i,0
            while j < n and k < m and s[j] == t[k]:
                j += 1
                k += 1
            k -= 1
            j -= 1
            while j >= 0 and k < m and s[j] == t[k]:
                j -= 1
                k += 1
            if k == m:
                print('YES')
                flag = 1
                break
        if flag == 0:
            print('NO')
                