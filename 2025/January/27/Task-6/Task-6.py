from turtle import*
m = 10
left(90)
up()
tracer(0)
screensize(2000, 2000)
for i in range(9):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
bk(10*m)
rt(90)
down()
for i in range(8):
    fd(15*m)
    lt(90)
    fd(25*m)
    lt(90)
up()
fd(6*m)
lt(90)
down()
for i in range(7):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
for x in range(-20, 50):
    for y in range(-20, 70):
        goto(x*m, y*m)
        dot(3, 'magenta')
update()
done()