#this circle module has functions related to a circle 
import math

def Area(radius):
    #this function calculates the area of a circle
    #Declare local variables
    area = 0.00 
    area = math.pi * radius**2 
    return area 



def Circumference(radius):
    #this calculates the circumference of a circle 
    circumference = 0.00
    circumference = 2 * math.pi * radius
    return circumference 