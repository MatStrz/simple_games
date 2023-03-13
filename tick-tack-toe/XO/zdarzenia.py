import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()
t.pensize(7)
t.shape('turtle')

def up():
    t.color(random.choice(['red','blue','yellow','green']))
    t.forward(100)

def left():
    t.left(30)

def right():
    t.right(30)

def bye():
    turtle.bye()

def click(x,y):
    t.color(random.choice(['red','blue','yellow','green']))
    t.goto(x,y)


window.onkey(up,'Up')
window.onkey(left,'Left')
window.onkey(right,'Right')
window.onkey(bye,'q')

window.onclick(click)

window.listen()
window.mainloop()