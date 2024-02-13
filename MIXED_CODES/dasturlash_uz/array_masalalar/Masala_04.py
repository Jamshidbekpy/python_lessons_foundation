n = int(input())
a=[]
for i in range(n):
    element=int(input("Element qo'shing:"))
    a.append(element)
b=float(input())
l="false"
for i in a:
    if i!=b:
        continue
    else:
        l="True"
print(l)




