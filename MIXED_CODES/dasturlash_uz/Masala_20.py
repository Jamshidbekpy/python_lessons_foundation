a=int(input())
b=int(input())
c=int(input())
if a<b and b<c:
    print(1)
elif a>b and b>c:
    print(2)
elif b>a and b>c:
    print(b)
elif(a==b and b==c):
    print(5)
else :
    print(0)