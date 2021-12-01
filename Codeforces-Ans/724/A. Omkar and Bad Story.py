T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int,input().split(" ")))
    b = set(a)
    nice = 0
    while len(a) <= 300:
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if abs(a[i]-a[j]) not in b:
                    b.add(abs(a[i]-a[j]))
        if set(a) == b:
            nice = 1
            print("Yes")
            print(len(b))
            print(" ".join(list(map(str,b))))
            break
        a = list(b)
    if not nice:
        print("No")