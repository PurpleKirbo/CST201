#This program prompts the user for an items price and weight and gives output of price per ounce

#Declare and initialize variables
item = ""
pounds = 0
ounces = 0
price = 0.00
pricePerOunce = 0.00
convertToOunces = 0
totalOunces = 0

POUNDCON = 16 #This is a constant variable

#Get our input
item = str(input("Enter the item name you wish to purchase: "))
while True:
    try:
        print("\n\n***In the prompt below enter the price of the " + item + "***")
        price = float(input("\n\tEnter price (only enter numeric values and do not leave empty): $"))

        print("\n\n***In the prompts below enter the weight of the " + item + "***")
        print("***Make sure you enter numeric values and do not leave the prompts empty***")
        pounds = int(input("\n\tEnter the weight in pounds (e.i. if weight is 2 lbs 5 ozs enter '2'): "))
        ounces = int(input("\tEnter the weight in ounces (e.i. if weight is 2 lbs 5 ozs enter '5'): "))
    except ValueError:
        print("\n\tThere is a error in the numeric input. Pleas try again")
        continue
    else: 
        break

                

#Processing
convertToOunces = pounds * POUNDCON 
totalOunces = convertToOunces + ounces
pricePerOunce = price/totalOunces
#pricePerOunce = price/((pounds * POUNDCON) + ounces)

#Show output 
print("\n\n\tPRICE PER OUNCE", item.upper())
print("\t-----------------------")
print("The price of the item is: $(0:,.2f)" .format(price))
print("The weight of the", + item, + "is",  format(pounds, '.d'),  "lbs and", format(ounces, '.d'), "ozs")
print("Total ounces of the", item, "are", format(totalOunces, ',d'))
print("The price per ounce of the", + item + ": $" + str(format(pricePerOunce, ',.2f')))























































































































































































#Start file Wednesday 9-7-22
