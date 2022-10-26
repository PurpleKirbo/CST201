#this is an example program on function
#declare global variables
STATETAXRATE = .05
COUNTYTAXRATE = 0.025


def main(): 
    #declare local variables to this function 
    purchase = 0.00
    stateTax = 0.00
    countyTax = 0.00 
    #Call a value returning function to get input
    purchase = GetInput(purchase) #This is a function call and anything in the parentheses are arguments for the function










def GetInput(p): #this is a function header. the parameters of the header must match with the arguments of the functions call
    #they must match in number and order but do not need to match in name
    #declare local variable for this function 
    prompt = "Enter the purchase amount: $"
