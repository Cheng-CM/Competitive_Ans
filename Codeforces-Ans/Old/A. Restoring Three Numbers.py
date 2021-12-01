n = input().split(" ")
n = sorted(list(map(int,n)))
print(n[3]-n[0],n[3]-n[1],n[3]-n[2],flush=True)