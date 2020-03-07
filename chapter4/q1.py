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
    t = draw_square(t, 20)
    t.penup()
    t.forward(40)
    t.pendown()

w.mainloop()

