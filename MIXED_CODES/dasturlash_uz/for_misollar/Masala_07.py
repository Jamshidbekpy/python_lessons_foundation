a=int(input())
b=int(input())
sum=0
for i in range(b,a+1):
    if i%2==0:
        sum+=1
print(sum)