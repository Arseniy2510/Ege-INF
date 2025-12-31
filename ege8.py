# from itertools import *
# c = 0
# for x in product('01234567', repeat = 5):
#     s = ''.join(x)
#     if s[0] != '0' and s.count('2') == 2 and '23' not in s:
#         c+=1
# print(c)

from itertools import *
c = 0
for x in product('01234567', repeat = 5):
    s = ''.join(x)
    if s[0] != '0' and s.count('5') == 1:
        s = s.replace('1','*')
        s = s.replace('3', '*')
        s = s.replace('5', '*')
        s = s.replace('7', '*')

        if '**' not in s:
            c += 1
            print(c, s)

print(c)