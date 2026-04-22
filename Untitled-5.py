pen.color("orange")
for i in range(6):
    pen.forward(100)
    pen.left(60)

angle = 360/49
pen.pu()
pen.sety(-1)
pen.pd()
for i in range(49)