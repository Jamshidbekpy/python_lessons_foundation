a=int(input())
b=int(input())
c=int(input())
if (a<b+c and b<a+c and c<a+b) and (a>0 and b>0 and c>0):
    if a==b and b==c:
        print("equilateral")
    elif a==b or b==c or a==c:
        print("isosceles")
    else :
        print('scalene')
else:
    print(None)