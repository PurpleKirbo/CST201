#this is an a example of a for loop in a program 

import math


def main():
    #declare variables and initalize
    number = 0
    fName = ""
    lName = ""
    name = ""
    flag = "N" #this is a while loop control variable 
    #input validation with a while loop
    while (flag.upper() == "N"):
        fName = str(input("\nEnter the first name of the customer: "))
        lName = str(input("Enter the last ame of the customer " + fName + ": "))
        name = fName + " " + lName
        print("\n\tYou Have entered the name " + name)
        flag = str(input("If this is not correct type n/N if it is correct hit any other key: "))
    number = int(input("\nEnter a number that you want to see the square root values: "))
    for i in range(0, number +1):
        print("{0:2s}{1:<15,d}{2:2s}{3:<15,.2f}".format("", i, "", math.sqrt(i))



main()