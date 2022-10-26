#this program calculates a sales forecast 
import sys  #this imports sys functions to make my life easier


def main():
    #Variables 
    productName = "" 
    currentAnnual = 0.00
    growthRate = 0.00
    numYears = 0
    flag = "N" #input validation 

    #get Inputs 
    print("\t\t-------------------------------------------")
    print("\t\t***Miller Company Sales Forecast Program***")
    print("\t\t-------------------------------------------")
    while (flag.upper() == "N"): #input validation loop 
        productName = str(input("\nWhat is the name of the product: "))
        print("\nThe Name of the Product you entered is: " + productName)
        flag = str(input("\nIf this is the not the correct product enter 'n' or 'N'. Otherwise hit any other key"))
    print("\n\t**Enter Only Numeric Data Below**")
    while True: #exception handling
        try: 
            currentAnnual = float(input("\nEnter Current annual sales for the product " + productName + ": $"))
            growthRate = float(input("Enter expected annual growth rate (in decimal form such as 7% is .07) : "))
            numYears = int(input("Enter the Number of years you want to project sales growth (in whole years such as 3): "))
        except ValueError():
            print("\n\tYou did not enter a numeric value. Try again")
            continue
        else:
            break 










