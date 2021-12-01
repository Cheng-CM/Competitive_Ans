T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    ans = []
    cond = {}
    for i in range(n):
        row = []
        flag = 1
        won = 0
        for j in range(n):
            if i == j: row.append('X')
            elif (i,j) in cond:
                if s[i] == '2' and cond[(i,j)] == '+': won = 1
                row.append(cond[(i,j)])
            elif s[i] == '1' and s[j] == '1': 
                row.append('=')
                cond[(j,i)] = '='
            elif s[i] == '1' and s[j] == '2': 
                row.append('+')
                cond[(j,i)] = '-'
            elif s[i] == '2' and s[j] == '1': 
                row.append('-')
                cond[(j,i)] = '+'
            elif s[i] == '2' and s[j] == '2':
                if won == 0:
                    row.append('+')
                    cond[(j,i)] = '-'
                    won = 1
                else:
                    row.append('-')
                    cond[(j,i)] = '+'
        if s[i] == '2' and won == 0:
            flag = 0
            print('NO')
            break
        ans.append(row)
    if flag:
        print('YES')
        for row in ans:
            print(''.join(row))