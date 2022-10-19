#this program is for displaying depreciation of a capitol asset


def main(): 
    #declare variables
    item = ""
    purYr = 0 
    cost = 0.00 
    numYrs = 0 #this will be our count control variable 
    salvage = 0.00
    totalDep = 0.00 
    slDep = 0.00
    beginValue = 0.00
    endValue = 0.00 
    flag = "N" #this is out input validation condition loop control

    #get input
    print("\n\t******DEPRECIATION PROGRAM FOR CAPTITOL GAIN ASSET********")
    while (flag.upper() == "N"): #this is our string input validation loop
        item = str(input("\nEnter the name of the captiol asset: "))
        print("\n\tThe name of your asset is: " + item)
        flag = str(input("\nIf this is not the correct name of the asset type 'n' or 'N'. Otherwise it any other key: "))
    while True: #this is execption handling
        try:
            purYr = int(input("\n Enter the year of purchase for the capitol asset: "))
            cost = float(input("Enter the orginal cost of the capital assest: $"))
            salvage = float(input("Enter the salvage value of the capital asset at the end of its useful life: $"))
            numYrs = int(input("Enter the useful life of the asset (in whole years such as 5): "))
        except ValueError():
            print("\n\t You did not enter numeric value for one or more prompts. Try again!")
        else: 
            break 
    
    print("{0:5s}{1:>15s}{2:>15s}{3:>18s}{4:>18s}".format("", "Beginning", "Amount Of", "Total", "Ending"))





main() 