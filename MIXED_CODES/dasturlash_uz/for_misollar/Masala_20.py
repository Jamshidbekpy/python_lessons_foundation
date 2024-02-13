n = int(input())
temp = 0
reverse_n = 0
while n != 0:
    temp = n % 10
    reverse_n = reverse_n*10+temp
    n=n//10
print(reverse_n)
