T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    d = {'B':'R','R':'B', '?':'B'}
    arr = []
    for i,c in enumerate(s):
        arr.append(c)
        if c != '?':
            j = i-1
            while j >= 0 and s[j] == '?':
                arr[j] = d[arr[j+1]]
                j -= 1
    for i,c in enumerate(arr):
        if c == '?':
            arr[i] = d[arr[i-1]]
    print(''.join(arr))
