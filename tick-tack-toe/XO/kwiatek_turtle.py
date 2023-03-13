import turtle

t = turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("black")
t.color("white")
t.speed(0.5)
t.pensize(2)

def kwiatek(środek,płatki):
    t.color('yellow')
    t.circle(środek)
    for _ in range(płatki):
        t.penup()
        t.circle(50, extent = 360/płatki)
        t.pendown()
        t.color("red")
        t.circle(-50)
t.penup()

t.goto(-300,0)
t.color('white')
t.pendown()
t.write("Cześć", font =  ('Arial', 30, "bold"))
t.hideturtle()

turtle.exitonclick()


