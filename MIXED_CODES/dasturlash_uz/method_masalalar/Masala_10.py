def raqam_sum(n):
    sum=0
    while n!=0:
        l=n%10
        sum+=l
        n=n//10
    return sum
m=int(input())
print(raqam_sum(m))
