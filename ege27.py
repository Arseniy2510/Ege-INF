from math import *
f = open('27_A_23209.txt')

data = [list(map(float, x.replace(',','.').split())) for x in f]
clusters = []

while len(data) > 0:
    clusters.append([data.pop()])
    for t in clusters[-1]:
        for e in data.copy():
            if dist(t, e) < 1:
                clusters[-1].append(e)
                data.remove(e)

def centr(cl1):
    res = []
    for p in cl1:
        sm = 0
        x1, y1 = p
        for m in cl1:
            x2, y2 = m
            sm += ((x2-x1)**2 + (y2-y1)**2)**0.5
        res.append([sm, p])
    return min(res)

print(centr(clusters[0]))
print(centr(clusters[1]))
