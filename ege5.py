def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s
res = []
for N in range(1,1000):
    s = f(N)
    if (s.count('2')*2 + s.count('1')) % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    R = int(s, 3)
    if R > 100:
        res.append(R)
print(min(res))