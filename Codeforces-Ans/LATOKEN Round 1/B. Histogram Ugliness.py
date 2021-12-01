T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    cost = 0
    length = 0
    if n == 1:
        print(arr[0])
    else:
        for i in range(n):
            if i == 0:
                if arr[i] > arr[i+1]:
                    cost += arr[i] - arr[i+1]
                    arr[i] = arr[i+1]
                length += arr[i]
            elif i == n-1:
                if arr[i] > arr[i-1]:
                    cost += arr[i] - arr[i-1]
                    arr[i] = arr[i-1]
                length += arr[i]
            else:
                if arr[i-1] < arr[i] > arr[i+1]:
                    cost += arr[i] - max(arr[i-1],arr[i+1])
                    arr[i] -= arr[i] - max(arr[i-1],arr[i+1])
                if arr[i] > arr[i-1]:
                    length += (arr[i] - arr[i-1])
                if arr[i] > arr[i+1]:
                    length += (arr[i] - arr[i+1])
        print(length+cost)
