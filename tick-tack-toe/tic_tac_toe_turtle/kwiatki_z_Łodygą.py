import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)


def kwiatek(środek, płatki, color_środek="yellow", color_płatki="red"):
    t.color(color_środek)
    t.begin_fill()
    t.circle(środek)
    t.end_fill()
    for _ in range(płatki):
        t.penup()
        t.circle(środek, extent=360/płatki)
        t.pendown()
        t.color(color_płatki)
        t.begin_fill()
        t.circle(-środek)
        t.end_fill()
    t.right(90)
    t.forward(2 * środek)


def łodyga(środek):
    t.color("green")
    t.forward(5 * środek)
    t.right(180)
    t.forward(2*środek)
    t.right(90)
    t.circle(3 * środek, extent=90)
    t.left(90)
    t.circle(3 * środek, extent=90)
    t.left(135)
    for i in range(5):
        if i % 2 == 0:
            t.forward(środek/2)
            t.right(30)
            t.forward(środek)
            t.back(środek)
            t.left(30)
        else:
            t.forward(środek/2)
            t.left(30)
            t.forward(środek)
            t.back(środek)
            t.right(30)

    t.forward(środek)
    t.right(45)


def kwiatek_z_łodygą(środek):
    kwiatek(środek, 6)
    łodyga(środek)



x= -300
y= -200
while True:
    if x < 1 and y < 1:
        t.penup()
        t.goto(x,y)
        t.pendown()
        kwiatek_z_łodygą(7)
        x += 50
    elif x >= 1:
        y += 100
        x = -300
    else:
        break


turtle.exitonclick()