n=int(input())
for i in range(n):
    print((n-i-1)*" ",end="")
    for j in range(n):
        print("*",end="")
    print()