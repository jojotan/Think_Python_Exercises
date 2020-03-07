import turtle


def make_window(color,title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.speed(2)
    return t

def make_star(t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)


w = make_window('lightgreen', 'Square')
tess = make_turtle('pink','2')

for i in range(5):
    make_star(tess,100)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

w.mainloop()