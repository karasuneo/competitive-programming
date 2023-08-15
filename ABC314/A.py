# import math
# from decimal import Decimal, getcontext

# getcontext().prec = 101

# py = Decimal(
#     "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
# )


# x = int(input())

# if x >= 100:
#     x = 100


# ans = math.floor(py * Decimal(10 ** (x + 1)))

# if x == 100:
#     print(py)
# elif ans % 10 == 0:
#     print(ans / Decimal(10**x))
# else:
#     print(str(ans / Decimal(10 ** (x + 1)))[:-1])


pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
N = int(input())

for i in range(N + 2):
    print(pi[i], end='')
