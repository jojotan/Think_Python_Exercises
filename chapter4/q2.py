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

def draw_square(t,r):
    t.forward(r) 
    t.left(90)
    t.forward(r)
    t.left(90)
    t.forward(r)
    t.left(90)
    t.forward(r)
    t.left(90)

    return t

w = make_window('lightgreen', 'Square')
t = make_turtle('pink','5')

for i in range(5):
    size = (i+1)*20
    t = draw_square(t, size)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

w.mainloop()