n=int(input())
for i in range(0,n+1):
    for j in range(0,n+1):
        if i==0 or i==n or j==0:
            print((i,j),end="")
    print()