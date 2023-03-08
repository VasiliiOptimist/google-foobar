from math import floor
import decimal

def s(a, n):
    if n == 0 or n == 1:
        return floor(n*a)

    new_n = floor((a - 1) * n)
    return ((n + new_n) * (n + new_n + 1) // 2
            -new_n*(new_n + 1) - s(a, new_n))


def solution(str_n):
    decimal.getcontext().prec = 200
    sqrt2 = decimal.Decimal(2).sqrt()
    return s(sqrt2, int(str_n))


str_n = str(10**100)
print(solution(str_n))
