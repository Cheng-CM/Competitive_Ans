s = input()
h = 'hello'
i = 0
flag = 0
for c in s:
    if c == h[i]:
        i += 1
    if i == 5:
        print('YES')
        flag = 1
        break
if not flag:
    print('NO')