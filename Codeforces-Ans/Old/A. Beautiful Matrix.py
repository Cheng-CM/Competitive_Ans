matrix = []
x,y = 2,2
mx,my = 0,0
for i in range(5):
    arr = input().split(" ")
    arr = list(map(int,arr))
    for j in range(5):
        if arr[j] == 1:
            mx,my = i,j
            break
print(abs(x-mx)+abs(y-my))