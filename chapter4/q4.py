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
    t.speed(20)

    
    return t

def draw_unit(t, size):
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(2*size)
    t.left(90)
    t.forward(2*size)
    t.left(90)
    t.forward(2*size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)


w = make_window('lightgreen', 'Square')
tess = make_turtle('blue','2')


rotation = 360/20
for i in range(20):
    tess.left(rotation)
    draw_unit(tess, 100)

    


w.mainloop()