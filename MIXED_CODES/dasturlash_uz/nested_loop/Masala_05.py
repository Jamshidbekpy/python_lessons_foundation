n=int(input())
for i in range(0,n+1):
    for j in range(0,n+1):
        if j%2==0 or i==0 or i==n:
            print((i,j),end="")
        elif j%2==1:
            print("      ",end="")
    print()