a=int(input())
b=int(input())
sum=0
count=0
for i in range(b,a+1):
    if i%3==0:
        sum+=i
        count+=1
print(sum," ",count)