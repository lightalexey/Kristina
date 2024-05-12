# from turtle import *
speed(10)
k = 10
for i in range(2):
    forward(16 * k)
    right(90)
    forward(9 * k)d
    right(90)
up()
forward(5 * k)
right(90)
forward(11* k)
right(90)
done()
for i in range(2):
    forward(20 * k)
    right(90)
    forward(8 * k)
    right(90)
up()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(3, 'red')
done()







