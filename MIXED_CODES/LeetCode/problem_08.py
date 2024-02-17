# 50.
# Pow(x, n)
# Solved
# Medium
# Topics
# Companies
# Implement
# pow(x, n), which
# calculates
# x
# raised
# to
# the
# power
# n(i.e., xn).
#
# Example
# 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example
# 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example
# 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2 - 2 = 1 / 22 = 1 / 4 = 0.25
#
# Constraints:
#
# -100.0 < x < 100.0
# -231 <= n <= 231 - 1
# n is an
# integer.
# Either
# x is not zero or n > 0.
# -10**4 <= x**n <= 10**4
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a=x**n
        if (x>-100.0 and x<100.0):
            if n>=-2**31 and n<=2**31-1:
                if a>=-10**4 and a<=10**4:
                    return a
new_object=Solution()
x=2
n=-2
print(new_object.myPow(x, n))