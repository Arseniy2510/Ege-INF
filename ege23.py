def f(x, end):
    if x == end:
        return 1
    if x > end or x == 7 or x == 11:
        return 0
    if x < end:
        return f(x+1,end) + f(x+3, end) + f(x*2, end)

print(f(3,16))