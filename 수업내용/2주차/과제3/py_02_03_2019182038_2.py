import turtle
turtle.speed(0)
x=0
y=0
count=0
length=100
size=5-1

while(y<=size):
    x=0
    turtle.penup()
    turtle.goto(x*length,y*length) 
    while(x<=size):
        turtle.penup()
        turtle.goto(x*length,y*length)
        turtle.pendown()
        count=0
        while(count<=3):
            turtle.forward(length)
            turtle.left(90)
            count=count+1
        x=x+1
    y=y+1
turtle.exitonclick()
