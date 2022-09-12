#using the turtle library 
import turtle

#hide the turtle
#turtle.hideturtle()

#set the fill color to blue
turtle.fillcolor("blue")
#set the pen color to red
turtle.pencolor('red')
#set the size of the pen
turtle.pensize(5)
#set the background color of the screen
turtle.bgcolor ('green')
#draw a daimond
turtle.begin_fill ()
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill ()

turtle.penup ()
turtle.goto(-120,120)
turtle.pendown()
turtle.write('Center Screen')