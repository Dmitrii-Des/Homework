from turtle import*

m = 20
lt(90)
tracer(0)
rt(30)
screensize(10_000, 10_000)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'magenta')
update()
done()