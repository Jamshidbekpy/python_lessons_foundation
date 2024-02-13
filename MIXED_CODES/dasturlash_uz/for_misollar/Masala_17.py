n = int(input())
tub_son = True
for i in range(2, n//2+1):
    if n % i == 0:
        tub_son = False
        break
if tub_son == True:
    print('true')
else:
    print('false')

