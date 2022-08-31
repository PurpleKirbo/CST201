#This program prompts the user for an items price and weight and gives the output in price per pound

#Declare and Initalize variables
item = ""
pounds = 0 
ounces = 0
price = 0.00
pricePerOunce = 0.00
convertToOunces = 0 
totalOunces = 0 

POUNDCON = 16 #this is a constant variable

#get the input
item = str(input("Enter the Item you wish to purchase: "))
print("\n\n***In the prompt below enter the price of the  " + item + "***")
price = float(input("\n\tEnter Price (Only enter numeric values and do not leave empty) : $"))
print("\n\n***In the prompt below enter the weight of the " + item + ".")
print("**Make sure that you enter a numeric Values and do not leave the prompt Empty***")
pounds = int(input("\n\tEnter the weight in pounds(i.e. if weight is 2 lbs 5 ozs enter '2'): "))
ounces = int(input("\n\tEnter the weight in ounces(i.e. if weight is 2 lbs 5 ozs enter '5'): "))


#Processing
convertToOunces = pounds * POUNDCON 
totalOunces = convertToOunces + ounces 
pricePerOunce = price/totalOunces
#pricePerOunce = price/((pounds * POUNDCON) + ounces)