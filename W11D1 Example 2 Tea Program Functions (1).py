#This program prompts for a tea order and give the customer output on their order
#global variables
SALESTAX = .05 #This is a constant for the tax rate

def main():
    #Declare Variables nd initialize
    chai = 0
    breakfastBlend = 0
    cham = 0
    earlGrey= 0
    fName = ""
    lName = ""
    price = 0.00
    sbt = 0.00
    tax = 0.00
    sat = 0.00
    shipping = 0.00
    totalOrder = 0.00
   
    #Get Input
    chai, breakfastBlend, cham, earlGrey = GetInputTea(chai, breakfastBlend, cham, earlGrey)    
   
    #Processing
   #Decision to get price
    if (TotalBoxes(chai, bb, cham, eg) < 6):
        price = 6.95
    else:
        if ((TotalBoxes(chai, bb, cham, eg) > 5) and (TotalBoxes(chai, bb, cham, eg) < 11)):
            price = 5.95
        else:
            price = 4.95
    sbt = totalBoxes * price #This subtotals the tea order before tax
    tax = sbt * SALESTAX #This calculates tax based on the subtotal before tax
    sat = sbt + tax #This calculates the subtotal with tax added
    #Decision to get shipping
    if (sat < 20): #This test for and order of less than $20 and set shipping
        shipping = 2.00
    elif ((sat >=20) and (sat < 40)):
        shipping = 1.50
    elif ((sat >= 40) and (sat < 50)):
        shipping = 1.00
    else:
        shipping = 0.00
    totalOrder = sat + shipping #This totals the order with the shipping cost
    #Show Output
    print("\n\n\t\t####Customer Sales Receipt####")
    print("\t\t------------------------------")
    print("\n\tCustomer Name: {0:s}".format(fName + " " + lName))
    print("\tChai Tea Ordered: {0:,d}".format(chai))
    print("\tBreakfast Blend Tea Ordered: {0:,d}".format(breakfastBlend))
    print("\tChamomile Tea Ordered: {0:,d}".format(cham))
    print("\tEarl Grey Tea Ordered: {0:,d}".format(earlGrey))
    print("\tThe total boxes of tea ordered: ",format(totalBoxes, ',d'))
    print("\tThe subtotal of order before tax: ${0:,.2f}".format(sbt))
    print("\tThe tax rate on the order prior to shipping: {0:,.1%}".format(SALESTAX))
    print("\tThe total tax on the order: ${0:,.2f}".format(tax))
    print("\tThe subtotal of order after tax: ${0:,.2f}".format(sat))
    print("\tThe amount of shipping cost: ${0:,.2f}".format(shipping))
    print("\tThe final cost of the order: ${0:,.2f}".format(totalOrder))


def GetInputName(fn, ln):
    #this function gets the name of the customer 
    fName, lName = GetInputName(fName, lName)
    print("\n\t\t********MILLER TEA COMPANY*********")
    print("\t\t-----------------------------------")
    fn = str(input("\nEnter your first name: "))
    ln = str(input("Enter your last name: "))
    print("\n\tThe customer name entered is:", fName + " " + lName)
    return fn, ln 


def GetInputTea(chai, bb, cham, eg):
    #this gets the tea inputs 
    print("\n\t**Below enter numeric data for the boxes ordered. Do not leave empty**")
    while True:
        try:
            chai = int(input("\nEnter the number of boxes of Chai tea desired: "))
            breakfastBlend = int(input("Enter the number of boxes of Breakfast Blend tea desired: "))
            cham = int(input("Enter the number of boxes of Chamomile tea desired: "))
            earlGrey = int(input("Enter the number of boxes of Earl Grey tea desired: "))
        except ValueError:
            print("\n\tYou did not enter a numeric value for one of the tea prompts. Try again!")
            continue
        else:
            break
    return chai, bb, cham, eg



def TotalBoxes(chai, bb, cham, eg):
    #this function totals the order of the tea boxes 
    #declare local variables
    totalBoxes = 0
    totalBoxes = chai + bb + cham + eg
    return 


main() #This calls the main function 
































































































































































#start file for Monday 9-26-22


