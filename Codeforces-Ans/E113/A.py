T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    if n > 1:
        flag = 1
        for i in range(n-1):
            if s[i] != s[i+1]:
                flag = 0
                print(i+1,i+2)
                break
        if flag: print('-1 -1')
    else:
        print('-1 -1')