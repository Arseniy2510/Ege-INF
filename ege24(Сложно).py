"""
s = open('24_23281.txt').readline()

mx = 0
for l in range(len(s)):
    for r in range(l + mx, len(s)):
        kusok = s[l:r+1]
        if kusok.count('Y') > 80:
            break
        if kusok.count('Y') == 80 and kusok.count('2025') >= 90:
            mx = max(mx,len(kusok))
print(mx)
"""

from re import *

s = open('24_17563.txt').readline()

num = r'[789][0789]*'

pattern = rf'{num}(?:[-*]{num})*'

res = findall(pattern, s)
print(res)
print(max(len(x) for x in res))
