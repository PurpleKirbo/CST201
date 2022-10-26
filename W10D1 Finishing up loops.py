#this program demonstrates multiple loops for tuition increases 
import sys

def main():
    #declare variables 
    count = 0 
    tuition = 0.00 
    total = 0.00
    total = 0.00 
    years = 0 
    rate = 0.00 
    pause = ""
    startTuition = 0.00

    #you would use exception handling below 
    print("\n\**Enter in the prompt below only numeric data and do not leave empty**")
    tuition = float(input("Wat is the current tuition at the college:  $"))
    years = int(input("Enter the number of years to project ou the tuition increase: "))
    print("\n\tIn the prompt below enter a percent as a decimal (such sa .05 for 5%). Do not use the % sign: ")
    rate = float(input("What is the projected rate of tuition increase for the next " + str(years) + "years: "))
    if ((tuition <= 0.0 or (years <= 0) or rate <= 0.00)):
        print("\n\tDATA ENTERED IS NOT CORRECT BECAUSE IT IS EITHER A NEGATIVE NUMBER OR ZERO")
        pause = str(input("Hit enter to terminate the program"))
        sys.exit()
    while (count < years): #loop to calculate the tuition increase 
        tuition = tuition * (1 + rate)
        count = count + 1 #this will increment the condition control loop variable 
    startTuition =tuition #this will put the variable amount of tuition after the years while loop
    total = tuition #this puts into the total variable the amount of tuition at the end of the input years
    for  i in range(0, 4, 1): #this will add three more years to the total variable tuition 
        tuition = tuition * (1 + rate)
        total = total + tuition 

    print("\n\n\tAnnual tuition pre year in " + str(years) + " years is ${0:,.2f}".format(startTuition))
    print("\tTotal tuition of a bachelor degree starting in {0:,d} years at a rate of {1:,.1%} is ${2:,.2f}".format(years, rate, total))
    pause = str(input("Hit Enter to terminate the program: "))



main()


