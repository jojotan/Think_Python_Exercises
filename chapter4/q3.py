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
    
    return t

def draw_poly(t,n,size):
    degree = 360 / n
    for i in range(n):
        t.forward(size) 
        t.left(degree)

    return t

w = make_window('lightgreen', 'Square')
tess = make_turtle('pink','5')
draw_poly(tess,8,50)


w.mainloop()