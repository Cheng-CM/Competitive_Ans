T = int(input())
arr = []
i = 1
cnt = 1
while cnt <= 1000:
    arr.append(i)
    i += 1
    while  i % 3 == 0 or str(i)[-1] == '3':
        i += 1
    cnt += 1
for _ in range(T):
    k = int(input())
    print(arr[k-1])