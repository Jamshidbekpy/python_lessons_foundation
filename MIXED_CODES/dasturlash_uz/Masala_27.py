a=int(input())
b=int(input())
c=int(input())
if a>0 and b>0 and c>0:
    if (a%2==0 and b%2==0) or (a%2==0 and c%2==0) or (b%2==0 and c%2==0):
        print(1)
    elif (a%2==1 and b%2==1) or (a%2==1 and c%2==1) or (b%2==1 and c%2==1):
        print(2)
    else :
        print(0)
else:
    print(0)