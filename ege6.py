from turtle import *
screensize(2000,2000)
tracer(0)
k=15
lt(90)

# Сюда пишешь задачу для робота. Например:
# for i in range(2):
#     fd(4*k)
#     rt(90)
#     fd(10*k)
#     rt(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(2,'red')
done()