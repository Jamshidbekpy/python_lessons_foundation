def daraja(n):
    return lambda x:x**n
while True:
    b = input('Kiring:')
    if b =='1':
        a = int(input('a = '))
        kvadrat = daraja(2)
        print(kvadrat(a))    # a -> x
    else:
        break
def mult(k):
    mult = 1
    for i in range(len(k)):
        mult *= k[i]
    return mult
multp = lambda *args: mult([args[i] for i in range(len(args))])
print(multp(1, 2, 3, 4, 5))



