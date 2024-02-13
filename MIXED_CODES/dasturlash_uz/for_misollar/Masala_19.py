n = int(input())
i = 0
a = 10
while a > 9:
    a = n // (10 ** i)
    i += 1
m = 0
summa = 0
for j in range(1, i+1):
    m = (n % (10**j))//(10**(j-1))
    summa += m
print(summa)