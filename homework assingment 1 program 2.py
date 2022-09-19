#this program will calculate the cost of car repairs. 


#variables
customerName = ""
carMake = ""
date = ""
hoursOfLabor = 0
costOfSupplies = 0.00 
laborCost = 0.00
totalCost = 0.00 

#consants 
LABORCOST = 40 

#user prompts
while True: 
    try:
        customerName = str(input("\n\tIn the prompt Please enter the name of the Customer  (Do not enter any Numerical data):"))
        carMake = str(input("\n\tIn the prompt please enter the make of the car (Do not enter numerical data): "))
        date = str(input("\n\t In the prompt please enter the current date: "))
        hoursOfLabor = float(input("\n\tPlease Enter the number of hours of Labor: ")) 
        costOfSupplies = float(input("\n\tPlease Enter the cost of the supplies used: $"))
    except ValueError:
        print("You have entered a incorrect Value. Please try again.")    
        continue    
    else: 
        break     


#processing of some sort
laborCost = hoursOfLabor * LABORCOST 
totalCost = laborCost + costOfSupplies

#outputs 
print("\n\t**Customer Information**")
print("\n\t")
print("Name of Customer: " + customerName)
print("Car Make: " + carMake)
print("Date of Service: " + date)
print("Cost of supplies used during Service: $" + str(format(costOfSupplies, ",.2f")))
print("Hours of Labor: " + str(format(hoursOfLabor, ',.0f')))
print("Labor Rate: $" + str(format(LABORCOST, ',.0f')))
print("The total cost of labor is: $" + str(format(laborCost, ',.2f')))
print("The total cost of Service is: $" + str(format(totalCost, ',.2f')))
