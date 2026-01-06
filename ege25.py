# from fnmatch import *
# for x in range(2025,10**8 + 1, 2025):
#     if fnmatch(str(x),'12*34?5'):
#         print(x, x//2025)

# def delit(x):
#     s = set()
#     for d in range(1,int(x**0.5)+1):
#         if x % d == 0:
#             s.add(d)
#             s.add(x//d)
#     return s
#
# def pr(x):
#     if x > 1:
#         d = delit(x)
#         if len(d) == 2:
#             return True
#     return False
"""
def pr(x):
    return x > 1 and all(x % d != 0 for d in range(2, int(x**0.5)+1))

def delit(x):
    s = set()
    for d in range(1,int(x**0.5)+1):
        if x % d == 0 and pr(d) and str(d).count('5') == 1:
            s.add(d)
        if x % (x // d) == 0 and pr(x // d) and str(x // d).count('5') == 1:
            s.add(x//d)
    return s

for x in range(1324728,1400000):
    D5 = delit(x)
    if len(D5) == 2 and min(D5) * max(D5) == x:
        print(x, max(D5))
    if len(D5) == 1 and min(D5) * max(D5) == x:
        print(x, max(D5))
"""

# def p(x):
#     if x == 1:
#         return False
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return False
#     return True

# a=20
# b=16
# while a != 0 and b != 0:
#     if a >= b:
#         a %= b
#     else:
#         b %= a
# print(a+b)
'''
Алгоритм Евклида (Функция по поиску НОД):

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(20,16))
'''

