#this program calculates the sales tax and the markup for a item. 

#Variables
storesCost = 0.00
markup = .00 
shelfPrice = 0 
totalSalesTax = 0.00
finalPrice = 0.00 
salesTaxPercent = 0.00 
markupPercent = 0.00

#constants
salesTax = .05

#information prompts
while True: 
    try: 
        storesCost = float(input("\n\tEnter the orginal price of the item: $"))
        markup = float(input("\n\tEnter the percent of markup to be applied to the item as a decimal: "))
    except ValueError: 
        print("\n\tNumeric Data was not entered or a decimal was not entered. Please try again!")
        continue
    else:
        break



#processing of some sort. 
shelfPrice = (storesCost * markup) + storesCost #this calculates the marked up price
totalSalesTax = salesTax * shelfPrice  #this calculates the total sales tax
salesTaxPercent = "{:.0%}".format(salesTax) #this turns the sales tax into a percent for the output
markupPercent = "{:.0%}".format(markup) #this turns the markup decimal into a percent for the output
finalPrice = shelfPrice + totalSalesTax  #this calculates the fine price of a item

#outputs
print("The original cost of the item is: " + str(format(storesCost, ',.2f'))) 
print("The amount of markup that is being applied is: " + markupPercent)  
print("The Shelf price of the item is: " + str(format(shelfPrice, ',.2f')))  #1 
print("The sales tax rate that is being applied is: " + salesTaxPercent) 
print("The Total amount of sales tax for the item is: $ " + str(format(totalSalesTax, ',.2f'))) 
print("The Final Price of the item is: $ " + str(format(finalPrice, ',.2f'))) 
