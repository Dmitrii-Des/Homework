from turtle import*

lt(90)
m = 10
tracer(0)
for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(9):
    fd(77*m)
    rt(90)
    fd(66*m)
    rt(90)
up()
for x in range(-20, 40):
    for y in range(-20, 40):
        goto(x * m, y * m)
        dot(3, 'white')
update()
done()