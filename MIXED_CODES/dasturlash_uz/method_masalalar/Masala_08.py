def convertToString(n):
    c=[]
    for i in range(0,n):
        l=input("Qo'shmoqchi bo'lgan harfingiz:")
        c.append(l)
    s=""
    for i in c:
        s += i
    return s

m=int(input())

print(convertToString(m))

