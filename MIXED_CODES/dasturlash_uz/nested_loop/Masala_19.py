n=int(input())
for i in range(n):
    print((n-i-1)*" ",end="")
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("*",end="")
        else:
            print(" ", end="")
    print()