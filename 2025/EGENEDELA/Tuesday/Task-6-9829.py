from turtle import*

m = 18
lt(90)
tracer(0)
rt(90)
for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)
for i in range(2):
    rt(90)
    fd(10*m)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'magenta')
update()
done()