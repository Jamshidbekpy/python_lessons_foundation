a=int(input())
b=int(input())
c=int(input())
if a==b and b!=c:
    print(c)
elif c==b and b!=a:
    print(a)
elif a==c and b!=a:
    print(b)
else:
    print(0)