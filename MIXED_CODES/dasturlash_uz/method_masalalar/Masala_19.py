import math
def uch_yuza(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    else:
        return "Uchburchaklik shartini kiritgan sonlaringiz qanoatlantirmaydi!"

n=float(input())
m=float(input())
l=float(input())
print(uch_yuza(n,m,l))

