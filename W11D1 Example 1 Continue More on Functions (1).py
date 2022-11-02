#This program will calculate a bonus using functions
#Declare global varibale
CONTRIBUTIONRATE = 0.05

def main():
    #Declare local varibales
    grossPay = 0.00
    bonus = 0.00
    totalContribution = 0.00
    contribution = 0.00
    grossPay, bonus = GetInput(grossPay, bonus)
    ShowPayContribution(grossPay, "gross pay")
    ShowContribution(bonus, "bonus")
    ShowTotalContribution(grossPay, bonus)


def ShowTotalContribution(gp, b):
    #this function will calculate the total contribution for the 401k
    #declare local variables
    total = 0.00
    total = total + Contribution(gp)
    total = total + Contribution(b)
    print("\n\tThe total amount contributed to the 401k is: ${0:,.2f}".format(total))

def ShowContribution(val, word):
    #this function calculates and shows the contribution for gross pay to a 401k plan
    print("\n\tContributions from the " + word +  "pay amount of ${0:,.2f} is: {1:,.2f}".format(val, Contribution(val)))
    

def Contribution(val):
    #this function is for calculating the contribution to a 401k
    #declare local variable
    contribution = 0.00
    contribution = val * CONTRIBUTIONRATE
    return contribution 


def GetInput(gp, b):
    #This function gets input for the program
    print("\n\t**Enter in the prompts below only numeric data and do not leave empty**")
    gp = ExHandling("Enter the gross pay: $", b, 1)
    b = ExHandling("Enter the Amount of the bonus: $", b, 1)
    return gp, b 


def ExHandling(prompt, val, test): 
    #this function is used for exception handling 
    while True:
        try: 
            if(test == 1):
                val = float(input(prompt))
            elif(test ==2):
                val = int(input(prompt))
            else:
                val = str(input(prompt))
        except ValueError: 
                print("\n\tYou did not enter the correct data. Try again!")
                continue
        else:
            break
    return val 


main()#Call main function
    














































































































































































































#Start file for 10/31/22 Monday
