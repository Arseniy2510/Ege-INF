"""
f = open('9.txt')
c = 0
for i in f:
    s = [int(x) for x in i.split()]

    pov = [x for x in s if s.count(x) > 1]
    nepov = [x for x in s if s.count(x) == 1]

    if len(pov) == 3 and len(nepov) == 3:
        if sum(nepov)/len(nepov) >= sum(pov):
            c += 1
print(c)
"""
f = open('9.txt')
c = 0
for i in f:
    s = [int(x) for x in i.split()]
    pov = [x for x in s if s.count(x) > 1]
    nepov = [x for x in s if s.count(x) == 1]
    if len(pov) == 4 and len(set(pov)) == 1 and len(nepov) == 2:
        if sum(nepov)/len(nepov) < sum(pov):
            c += 1
print(c)