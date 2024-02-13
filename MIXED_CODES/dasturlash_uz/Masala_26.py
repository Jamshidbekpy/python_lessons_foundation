a=int(input())
b=int(input())
c=int(input())
if a%2==1 and b%2==1 and c%2==1:
    print(1)
elif a%2==0 and b%2==0 and c%2==0:
    print(2)
elif a%2==1 or b%2==1 or c%2==1:
    print(3)
else:
    print(0)