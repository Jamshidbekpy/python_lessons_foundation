n = int(input())
a = 0
h_0 = 0
h_1 = 1
summa = 0
for i in range(1, n):
    summa += h_1
    a = h_0
    h_0 = h_1
    h_1 = h_1+a
print(summa)


