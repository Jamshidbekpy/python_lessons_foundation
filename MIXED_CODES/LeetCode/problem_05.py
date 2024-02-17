# 507.
# Perfect
# Number
# Solved
# Easy
# Topics
# Companies
# A
# perfect
# number is a
# positive
# integer
# that is equal
# to
# the
# sum
# of
# its
# positive
# divisors, excluding
# the
# number
# itself.A
# divisor
# of
# an
# integer
# x is an
# integer
# that
# can
# divide
# x
# evenly.
#
# Given
# an
# integer
# n,
# return true if n is a
# perfect
# number, otherwise
# return false.
#
# Example
# 1:
#
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14
# are
# all
# divisors
# of
# 28.
# Example
# 2:
#
# Input: num = 7
# Output: false
#
# Constraints:
#
# 1 <= num <= 10**8
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<1 and num>99999999:
            return False
        elif num==1:
            return False
        else:
            Sum=1
            divisor=2
            while divisor*divisor<=num:
                if num%divisor==0:
                    Sum+=divisor
                    if divisor*divisor!=num:
                        Sum+=num//divisor
                divisor+=1
            return Sum==num
new_object=Solution()
new1=28
new2=7
print(new_object.checkPerfectNumber(new1))
print(new_object.checkPerfectNumber(new2))
