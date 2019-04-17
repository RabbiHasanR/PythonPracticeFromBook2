def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    


import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.color('pink')
count=0
while count<90:
    square(100)
    turtle.right(4)
    count+=1
turtle.exitonclick()
