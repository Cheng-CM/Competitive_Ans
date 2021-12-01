T = int(input())
for _ in range(T):
    s = input()
    e = [[],[]]
    for i,v in enumerate(s):
        if i % 2 == 0 and v == '?':
            e[0].append('1')
            e[1].append('0')
        elif i % 2 != 0 and v == '?':
            e[0].append('0')
            e[1].append('1')
        else:
            e[0].append(v)
            e[1].append(v)
    ans = 10
    for row in e:
        f,se,c1,c2 = 0,0,5,5
        for i in range(len(s)):
            if row[i] == '1':
                if i % 2 == 0:
                    f += 1
                else:
                    se += 1
            if i % 2 == 0:
                c1 -= 1
            else:
                c2 -= 1
            if f-se > c2 or se-f > c1:
                ans = min(ans,i+1)
                break
    print(ans)