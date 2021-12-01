T = int(input())
for _ in range(T):
    a = input()
    b = input()
    n,m = len(a),len(b)
    i,j = 0,0
    ndel = 0
    stack = []
    if m > n:
        print('NO')
    else:
        while i < n:
            if j < m and a[i] == b[j]:
                j += 1
                stack.append(a[i])
            elif j == m:
                print('YES')
                break
            else:
                if stack and ndel > 0:
                    ndel -= 1
                elif stack and ndel == 0:
                    stack.pop()
            i += 1
        print(stack)
            
                