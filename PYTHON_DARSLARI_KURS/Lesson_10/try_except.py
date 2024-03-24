try:
    a = int(input('a = '))
    b = int(input('b = '))
    print(a / b)
except ZeroDivisionError:
    print('b ne 0    bolib bo\'lmadi!')
except ValueError:
    print('a va b ga sonlar kiriting!')