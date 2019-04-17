def square(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    


import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.color('pink')
i=0
while i<90:
    square(100)
    turtle.right(5)
    i+=1
turtle.exitonclick()

