#this program calculates a sales forecast 

def main():
    #Variables 
    productName = "" 
    currentAnnual = 0.00 #Starting value 
    growthRate = 0.00 #yearly growth rate
    numYears = 0 #count loop control 
    growth = 0.00 # for calculation the amount of growth in a year
    endSales = 0.00 #ending value
    beginValue = 0.00 #starting value for the loop
    finalSalesGrowth = 0.00 
    flag = "N" #input validation 
    flag2 = "R" #flag to restart the program 

    while (flag2.upper() == "R"): #to restart the program 

        #get Inputs
        flag = "N" #resets the flag when restarted 
        print("\t\t-------------------------------------------")
        print("\t\t***Miller Company Sales Forecast Program***")
        print("\t\t-------------------------------------------")
        while (flag.upper() == "N"): #input validation loop 
            productName = str(input("\nWhat is the name of the product: "))
            print("\nThe Name of the Product you entered is: " + productName)
            flag = str(input("\nIf this is the not the correct product enter 'n' or 'N'. Otherwise hit any other key"))
        print("\n\t**Enter Only Numeric Data Below**")
        #More user inputs
        while True: #exception handling
            try: 
                currentAnnual = float(input("\nEnter Current annual sales for the product " + productName + ": $"))
                growthRate = float(input("Enter expected annual growth rate (in decimal form such as 7% is .07) : "))
                numYears = int(input("Enter the Number of years you want to project sales growth (in whole years such as 3): "))
            except ValueError:
                print("\n\tYou did not enter a numeric value. Try again")
                continue
            else:
                break 


        #output
        #restating of the inputs
        print("\n\n\t\t**** " + productName + " Sales Information ****")
        print("\n\tCurrent Annual Sales: ${0:,.2f}".format(currentAnnual))
        print("\tNumber of years of expected growth: " + str(numYears) + " years")
        print("\tThe interest rate to calculate for the growth: " + format(growthRate, '.0%'))
        #loop headings 
        print("\n\n{0:9s}{1:>9s}{2:>10s}{3:>9s}".format("", "Beginning", "", "Ending"))    
        print("{0:9s}{1:>9s}{2:>10s}{3:>9s}".format("Year", "Sales", "Growth", "Sales"))
        print("{0:7s}{1:>9s}{2:>10s}{3:>9s}".format("---------", "---------", "--------------", "---------"))
        beginValue = currentAnnual #preserves the current annual variable 
        #loop 
        for i in range(1, numYears + 1, 1):
            growth = beginValue * growthRate
            endSales = beginValue + growth 
            print("{0:3d}{1:>15,.2f}{2:>10,.2f}{3:>13,.2f}".format(i, beginValue, growth, endSales))
            beginValue = endSales 
            finalSalesGrowth = finalSalesGrowth + endSales 

        #the rest of the final output 
        print("\n\nTotal sales growth for " + str(numYears) + " years is: ${0:,.2f}".format(endSales - currentAnnual))
        print("Percent Growth of the Initial $ " + str(currentAnnual) + " Sales is: " + format((endSales - currentAnnual) / currentAnnual, '.0%'))
        print("The total amount of sales for the " + str(numYears) + " year period is: ${0:,.2f}".format(finalSalesGrowth))


    
        flag2 = str(input("\nDo you want to restart the program? If yes enter r or R. Otherwise hit any other key. "))






main()





