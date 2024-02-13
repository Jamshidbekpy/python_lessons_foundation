n = int(input())
a=[]
for i in range(n):
    element=int(input("Element qo'shing:"))
    a.append(element)

print("Index:",end="")
index=int(input())
if index < n:
    print(a[index])
else:
    print(0)