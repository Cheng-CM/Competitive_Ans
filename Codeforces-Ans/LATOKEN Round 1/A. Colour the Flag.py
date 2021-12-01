T = int(input())
for _ in range(T):
    n,m = map(int,input().split(' '))
    grid = [list(input()) for i in range(n)]
    valid = True
    def dfs(i,j,paint):
        if 0 <= i < n and 0 <= j < m:
            if grid[i][j] == '.':
                grid[i][j] = paint
                paint = 'R' if paint == 'W' else 'W'
                dfs(i+1,j,paint)
                dfs(i-1,j,paint)
                dfs(i,j+1,paint)
                dfs(i,j-1,paint)
            elif (grid[i][j] == 'R' and paint == 'W') or (grid[i][j] == 'W' and paint == 'R'):
                return False
        return True
                
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                if True and dfs(i+1,j,'W') and dfs(i-1,j,'W') and dfs(i,j+1,'W') and dfs(i,j-1,'W'):
                    pass
                else:
                    valid = 0
                    break
            elif grid[i][j] == 'W':
                if True and dfs(i+1,j,'R') and dfs(i-1,j,'R') and dfs(i,j+1,'R') and dfs(i,j-1,'R'):
                    pass
                else:
                    valid = 0
                    break
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                dfs(i,j,'R')
    if valid:
        print('YES')
        for row in grid:
            print(''.join(row))
    else:
        print('NO')