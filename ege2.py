print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x<=(z==w)) or not (y<=w)
                if F == 0 :
                    print(x,y,z,w)
"""
from itertools import *

def f(x, y, z, w):
    return ((x and y) <= (z and w)) and ((not y and z) == (not x or w))

for x1, x2, x3, x4, x5, x6 in product([0,1], repeat=6):
    t = [(x1,1,x2,x3), (1,1,x4,x5), (1,1,1,x6)]

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [1, 1, 1]:
                print(p)
"""