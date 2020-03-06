import  turtle

wn = turtle.Screen()
tess = turtle.Turtle()

size = 100

for i in range(5):
    tess.hideturtle()
    tess.forward(size)
    tess.right(145)
wn.mainloop()