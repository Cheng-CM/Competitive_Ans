T = int(input())
for t in range(T):
    f,s = list(map(int,input().split(" ")))
    for i in range(f,s+1):
        print(i,"{0:b}".format(i))
        print(i ^ int("1010101010101010101",2))
    print("Case #"+ str(t+1) +":",str(),flush=True)