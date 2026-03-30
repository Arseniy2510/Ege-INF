# from sys import *
# setrecursionlimit(4000)
#
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * f(n-1) + 2 + n
# print(f(3000))

from functools import *

@lru_cache(None)
def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return 3 * f(n-1) + f(n-2) + n

for i in range(1,3001):
    f(i)

print(f(3000))