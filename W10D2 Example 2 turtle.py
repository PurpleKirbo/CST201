#this program will be an example of using turtle in loops 
import turtle 

def main():
    #Constants 
    STARTINGX = -4
    STARTINGY = 4
    STARTINGSIZE = 8 
    NUMSQUARES = 50 
    STEP = 4 
    NUMOFSIDES = 4 
    ANGLE = 90
    ANIMATIONSPEED = 0 
    size = 0 
    x = 0 
    y = 0 


    turtle.speed(ANIMATIONSPEED) #this function set the speed of turtle 
    turtle.hideturtle()
    #set the initial x and y variables (coordinates) and starting size
    x = STARTINGX
    y = STARTINGY 
    size = STARTINGSIZE
    for count in  range(0, NUMSQUARES, 1): #this will draw the pattern 
        #position turtle at the starting point
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        #draw a square each time through the loop
        for s in range(0, NUMOFSIDES, 1): #this loop draws a square
            turtle.forward(size)
            turtle.right(ANGLE)
        #prepare for the next square 
        x = x - STEP 
        y = y + STEP 
        size = size + STEP

main()