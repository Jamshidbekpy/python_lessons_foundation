# Misol Sharti
# n soni berilgan.
#
# Geometrik shaklni ekranga chiqaring.
#
# n nechta bo'lsa bo'yiga  chiqadigan  yulduzchalar soni ham shuncha bo'lishi kerak.
#
# Namuna
#
# Masalan: n = 5
#
#  *****
#  ****
#  ***
#  **
#  *
variable="*"
n=5
j=n
for i in range(n):
    print(j*variable,end="")
    print()
    j-=1;