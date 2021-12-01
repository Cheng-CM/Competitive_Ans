def checkgrid(grid,i,j):
    h,w = len(grid),len(grid[0])
    if 0 <= i < h and 0 <= j < w:
        if grid[i][j] == 0:
            return True
    else:
        return True

T = int(input())
for _ in range(T):
    h,w = list(map(int,input().split()))
    grid = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                if all([checkgrid(grid,i+1,j),checkgrid(grid,i-1,j),checkgrid(grid,i,j+1),checkgrid(grid,i,j-1),checkgrid(grid,i+1,j+1),checkgrid(grid,i-1,j+1),checkgrid(grid,i-1,j-1),checkgrid(grid,i+1,j-1)]):
                    grid[i][j] = 1
    for row in grid:
            print(*row,sep='')

