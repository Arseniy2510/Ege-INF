"""
f = open('17.txt')
res = []
s = [int(x) for x in f]
s37 = [x for x in s if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 37]

for i in range(len(s)-1):
    if (10000 <= abs(s[i]) <= 99999) + (10000 <= abs(s[i+1]) <= 99999) == 1:
        if (s[i] + s[i+1])**2 > max(s37)**2:
            res.append(s[i] + s[i+1])

print(len(res), max(res))
"""

