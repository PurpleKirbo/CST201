#this program calculates someones paycheck. 

#variables
name = ""
hoursWorked = 0.00
hourlyRate = 0.00
overtime = 0.00
doubletime = 0.00
grossPay = 0.00
overtimeHours = 0.00
doubletimeHours = 0.00
netPay = 0.00
tax = 0.00

#get user inputs 
print("\t\t\t\t-------Miller LLC--------")
print("\n")
name = str(input("Please enter the name of the empolyee: "))
print("\n")
print("***IN THE PROMPT BELOW ONLY ENTER NUMERIC DATA AND DO NOT LEAVE EMPTY!***")
print("\n")
while True: 
    try: 
        hoursWorked = float(input("\tEnter the amount of hours worked: "))
        hourlyRate = float(input("\tEnter the hourly wage rate for the employee: $"))
    except ValueError:
        print("\n\tYou did not enter a numeric value! Please try again and only use numeric data.") 
        continue
    else:
        break



#set overtime and double time 
overtime = (hourlyRate * 1.5)
doubletime = (hourlyRate * 2)

#pay calculations
if (hoursWorked <= 40): #calculates normal hours
    grossPay = (hoursWorked * hourlyRate)
else: 
    if (hoursWorked < 50 or hoursWorked > 40): #calculates overtim pay
        overtimeHours = (hoursWorked - 40)
        grossPay = (40 * hourlyRate) + (overtimeHours * overtime)
    else: 
        if (hoursWorked > 50): #doubletime hours
            doubletimeHours = (hoursWorked - 50)
            grossPay = (40 * hourlyRate) + (10 * overtime) + (doubletimeHours * doubletime)

#tax calculations
if (grossPay <= 400.00):   #calculates tax for gross pay under 400
    tax = (grossPay * .0225)
    netPay = (grossPay - tax)
elif (grossPay <= 950.00):   #calculates tax for gross pay under 950
    tax = (grossPay - 400.00) * .03
    netPay = (grossPay - tax) + 9 
elif (grossPay <= 1550.00): # calculates tax for gross pay under 1550
    tax = (grossPay - 950.00) * .0375
    netPay = (grossPay - tax) + 25.50
elif (grossPay > 1550.00):    #calculates tax for gross pay over 1550
    tax = (grossPay - 1550.00) * .0450
    netPay = (grossPay - tax) + 48


#outputs i guess 
print("\n\n\n")
print("\t\t\t--------------------")
print("\t\t\tMiller LLC")
print("\t\t\tPayroll Information")
print("\t\t\t--------------------")
print("\t\tEmployee Name: " + name)
print("\t\tHours worked: " + str(format(hoursWorked)))
print("\t\tHourly Rate: $" + str(format(hourlyRate)))
print("\t\tGross Pay: $" + str(format(grossPay, ',.2f')))
print("\t\tIncome Tax: $" + str(format(tax, ',.2f')))
print("\t\tNet Pay: $" + str(format(netPay, ',.2f')))









           
