import  turtle

wn = turtle.Screen()
tess = turtle.Turtle()

tess.shape('turtle')

tess.penup()

degree = 0
for i in range(12):
    print("i:", i)
    degree = i*30
    tess.right(30)
    tess.forward(100)
    tess.stamp()
    tess.backward(100)
    print('degree:', degree)

wn.mainloop()
