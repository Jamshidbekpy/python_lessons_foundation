#Ushbu shaklni ekranga chiqaring
#*
# ***
# *****
# *******
# *********
# ***********
# *********
# *******
# *****
# ***
# *
"""1-yo'li"""
def romb(n):
    for i in range(n):
        print((2 * (n - (n - i)) - 1) * "*")
    for i in range(n):
        print((2 * (n - i) - 1) * "*")
n=6
romb(n)
"""2-yo'li"""
def romb_2(n):
    for i in range(2 * n - 1):
        if i <= n:
            print((2 * (n - (n - i)) - 1) * "*")
        if i >= n:
            print((2 * (2 * n - i) - 3) * "*")
romb_2(n)