# Ques
# Write a program to find smallest integer value b for a given value of a . If we multiply the digits of b ,
# We should get exact value of a
# Result b must contain more than one digit.

n = int(input())

def sol(n):
    if n < 10:
        return n + 10
    num = []
    i = 9
    while i > 1:
        while n % i == 0:
            num.append(i)
            n //= i
        i -= 1
    if n > 1:
        return -1
    num.sort()  
    res = int("".join(map(str, num)))
    return res

result = sol(n)
print(result)
