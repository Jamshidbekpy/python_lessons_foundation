a=int(input())
n=int(input())
had=0
sum=0
for i in range(0,n):
    had+=a*(10**i)
    sum+=had
print(sum)
