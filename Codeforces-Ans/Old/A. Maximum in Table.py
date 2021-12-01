n = int(input())
ans = 0

def elem(row, col):
    if row == 1 or col == 1:
        return 1
    return elem(row - 1, col) + elem(row, col - 1)

print(elem(n,n))