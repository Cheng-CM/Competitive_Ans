n = int(input())
s = sum(list(map(int,input().split(' '))))
print(sum(range(1,n+1))-s)