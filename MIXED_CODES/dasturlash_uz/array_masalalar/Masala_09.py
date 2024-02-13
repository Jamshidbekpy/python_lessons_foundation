l=[]
m=int(input())
for i in range(m):
    element=int(input('Element qo\'shing:'))
    l.append(element)
print (l)
a=int(input("Indexni kiriting:"))
if a < m:
    l.remove(l[a])
else:
    print("Index kiritishd xatolik!")
print(l)