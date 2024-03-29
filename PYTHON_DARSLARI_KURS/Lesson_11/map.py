from math import sqrt
print(list(map(sqrt, [3, 9, 2, 4, 6, 8, 10])))
print(list(map(lambda x: x**2, [3, 9, 2, 4, 6, 8, 10])))
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])))
print(list(map(pow, [2, 3, 4], [3, 2, 3])))
