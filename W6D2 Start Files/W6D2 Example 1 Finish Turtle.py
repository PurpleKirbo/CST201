#This is a game to hit a target
import turtle
#Constant variables
SCREENWIDTH = 600
SCREENHEIGHT = 600
TARGETLEFTX = 100
TARGETLEFTY = 250
TARGETWIDTH = 25
FORCEFACTOR = 30
PROJECTILESPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
#Declare variables and initialize
angle = 0.0
force = 0.0
distance = 0.00
#Set the turtle window
turtle.setup(SCREENWIDTH,SCREENHEIGHT)
#Draw target for game
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGETLEFTX,TARGETLEFTY)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGETWIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGETWIDTH)
turtle.setheading(WEST)
turtle.forward(TARGETWIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGETWIDTH)
turtle.penup()
#Move turtle to center screen
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILESPEED)
#Get the angle and forse for turtle to hit target from user
angle = float(input("Enter the projectile angle you want to move the turtle: "))
force = float(input("Enter the launch force to move turtle towards target (1 - 10): "))
#Calculate the distance of the projectile
distance = force * FORCEFACTOR
#Set the angle of the turtle based on user input
turtle.setheading(angle)
#Set the launch of the turtle projectile
turtle.pendown()
turtle.forward(distance)
#Give the user output based on their input
if ((turtle.xcor() >= TARGETLEFTX and turtle.xcor() <= (TARGETLEFTX + TARGETWIDTH)) and
    (turtle.ycor() >= TARGETLEFTY and turtle.ycor() <= (TARGETLEFTY + TARGETWIDTH))):
    print("YOU HIT THE TARGET!!")
else:
    print("YOU MISSED TARGET!! SORRY ABOUT YOUR LUCK")
    #Give some hints
    if (turtle.xcor() > (TARGETLEFTX + TARGETWIDTH)):
        print("\n\tTry a greater angele!")
    elif (turtle.xcor() < (TARGETLEFTX + TARGETWIDTH)):
        print("\n\tTry a lesser angle")
    elif(turtle.ycor() < (TARGETLEFTY + TARGETWIDTH)):
        print("\n\tTry a lesser Force!")
    elif (turtle.ycor() < TARGETLEFTY):
        print("\n\tTry more force!")









































































































#Start File Wednesday 9-28-22

    











