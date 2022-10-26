#This is an example program on functions
#Declare global variables
STATETAXRATE = 0.05
COUNTYTAXRATE = 0.025

def main():
    #Declare local variables to this function
    purchase = 0.00
    stateTax = 0.00
    countyTax = 0.00
    #Call a value-returning function to get input
    purchase = GetInput(purchase)#This is a function call and anything in the parentheses are arguments for the function
    print(purchase) #this will print the above function
    #call a value returning function to calculate tax
    stateTax, countyTax, = CalculateTax(purchase, stateTax, countyTax)
    #call a void function to show output
    ShowSales(purchase, stateTax, countyTax)

def ShowSales(p, st, ct): #this function header for the ShowSales function
    #this function is for output
    #Declare local Variables 
    total = 0.00 
    total = p + st + ct
    #show output
    print("\n\nPurchase Amount: ${0,.2f}".format(p))
    print("State Tax: ${0,.2f}".format(st))
    print("County Tax: ${0,.2f}".format(ct))
    print("Total Tax: ${0,.2f}".format(TotalTax(st,  ct))) #this outputs a value-returning function of TotalTax
    print("Total Purchase Amount: ${0,.2f}".format(total))


def TotalTax(s, c): #this is a function header for the TotalTax function 
    #this is called from the ShowSales Function and its purpose is to total All Taxes
    #declare variables
    totalTax = 0.00
    totalTax = s + c
    return totalTax 


def CalculateTax(p, st, ct): #this is the function header
    #this function calculates tax
    st = p * STATETAXRATE
    ct = p * COUNTYTAXRATE
    return st, ct 

def GetInput(p):#This is a function header, the parameters of the header must match the arguments of the function call
    #The must match in number and order but do not need tomatch in name
    #Declare local variable for this function
    prompt = "Enter the purchase amount: $"
    p = ExHandling(prompt, p, 1) #this is a function call for a function named Exhandling 
    return p #This returns the variable 'p' to the main functiion and is accepted into the variable "purchase"in the main function





def ExHandling(pr, purchase, check): #this is a function header for the ExHandling function 
    #this function is for exception handling
    while True:
        try:
            if (check == 1):
                purchase = float(input(prompt))
            else:
                purchase = int(input(prompt))
        except ValueError():
            print("\n\tYou did not enter a numeric value. Try Again!")
            continue 
        else:
            break 
    return purchase #this returns "purchase" to the GetInput function into the variables "p"
 






main()

























































#Start file for Wednesday 10-26-22
