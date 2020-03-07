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

w = make_window('lightgreen', 'Square')
tess = make_turtle('blue','2')

size = 2

for i in range(99):
    
    tess.right(90)
    tess.forward(size)
    tess.right(90)
    size = size +2
    tess.left(91)
tess.right(90)

w.mainloop()