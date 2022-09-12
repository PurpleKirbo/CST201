#this program calculates a cookie recipe based on the number of cookies needed 


#declare variables and initalize
cookies = 0.00
sugar = 0.00 
butter = 0.00
flour = 0.00


#constant variable 
COOKIERECIPE = 48.0 
SUGARRECIPE = 1.5 #this is the amount of sugar needed for 48 cookies 
BUTTERRECPE = 1.0 #this is the amount of butter needed for 48 cookies
FLOURRECPE = 2.75 #this is the amount of flour needed for 48 cookies 


#get inputs 
print("\t\t***In the Prompt Below only enter numeric data and do not leave empty!***")
while True: #exception handling 
    try: 
        cookies = int(input("Enter the number of cookies you would like to make: "))
    except ValueError: 
        print("\n\tNumeric Data was not entered or a decimal was entered. Please try again!")
        continue 
    else:
        break 

#processing 
sugar = (cookies * SUGARRECIPE) / COOKIERECIPE 
butter = (cookies * BUTTERRECPE) / COOKIERECIPE 
flour = (cookies * FLOURRECPE) / COOKIERECIPE 

#show output 
print("\n\n\tRECIPE FOR", cookies, "COOKIES")
print("\t--------------------")
print("Sugar needed for", cookies, "cookies: ", format(sugar, ',.2f'))
print("Butter needed for {0:,d} cookies: {1:,.2f} cups".format(cookies, butter))
print("Flour needed for {0:,d} cookies: {1:,.2f} cups".format(cookies, butter, flour))
