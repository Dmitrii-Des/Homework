from turtle import*
screensize(10_000, 10_000)
m = 10
lt(90)
tracer(0)
for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 50):
        goto(x * m, y * m)
        dot(3, 'magenta')
update()
done()